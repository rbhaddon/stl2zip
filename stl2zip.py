#!/usr/bin/env python3
"""
    stl2zip

    Walks the given path searching for 3D models files and compresses them into
    a zip file.

    Edit PATTERNS below to work on different 3D model file extensions

    Author: rbhaddon

"""
import click
import os
from pathlib import Path
import re
import time
from zipfile import ZipFile, ZIP_DEFLATED

KB = 1024
MB = KB * KB
MiB = 1000 * KB
GB = KB * MB
GiB = 1000 * MB

#PATTERNS = [".stl", ".obj", ".3mf"]
PATTERNS = [".stl"]

COMPRESSION = ZIP_DEFLATED

def gen_stats(source, counter, ascii_only):
    for filename in source:
        if ascii_only:
            # test filename is ascii
            try:
                with filename.open('r') as fd:
                    six_bytes = fd.read(6)
            except:
                print(f"Skipping (non-ASCII) {filename}")
                continue

        counter['count'] += 1
        counter['uncompressed_bytes'] += os.path.getsize(filename)
        yield filename


def gen_zip(source, counter, delete):
    """ To avoid zipping the whole source path, we chdir first before zipping
    """
    for filename in source:
        zipname = filename.with_suffix(".zip")
        print(f"Compressing {filename}")
        curdir = os.getcwd()
        try:
            with ZipFile(zipname, 'w', compression=COMPRESSION) as myzip:
                os.chdir(filename.parent)
                myzip.write(filename.name)
                counter['compressed_count'] += 1
        except Exception:
            print(f"Failed to create {zipname}")
            raise
        else:
            os.chdir(curdir)
            if delete:
                filename.unlink()

        yield filename, zipname


def gen_stats2(source, counter):
    for filename, zipname in source:
        counter['compressed_bytes'] += os.path.getsize(zipname.absolute())
        yield filename, zipname


@click.command()
@click.argument('path')
@click.option('--ascii-only', is_flag=True, default=False,
        help="Only compress ASCII-formatted models")
@click.option('--delete', is_flag=True, default=False,
        help="Delete models after compressing")
def main(path, ascii_only, delete, patterns=PATTERNS):
    top_dir = Path(path)
    counters = {x: {'count': 0, 'compressed_count': 0, 'uncompressed_bytes': 0, 'compressed_bytes': 0} for x in patterns}
    regex = re.compile(r'^(\s+)$')

    print(f"Using path: {top_dir}")

    start = time.time()
    for pattern in patterns:
        # Setup pipeline:
        filtered_files = top_dir.glob(f"**/*{pattern}")
        stat_files = gen_stats(filtered_files, counters[pattern], ascii_only)
        zip_files = gen_zip(stat_files, counters[pattern], delete)
        pipeline = gen_stats2(zip_files, counters[pattern])

        # 'Pull' the pipeline 
        [x for x in pipeline]
    elapsed = time.time() - start

    # Report
    print(f"Elapsed Time: {elapsed:.1f}s.")
    for pattern in patterns:
        print(f"*{pattern}:")
        print(f"    Files found      : {counters[pattern]['count']}")
        print(f"    Files compressed : {counters[pattern]['compressed_count']}")
    total_ubytes = sum([counters[x]['uncompressed_bytes'] for x in patterns])
    total_cbytes = sum([counters[x]['compressed_bytes'] for x in patterns])
    print(f"Total space saved due to compression: {(total_ubytes - total_cbytes)/MB:.1e} MB")


if __name__ == "__main__":
    main()
