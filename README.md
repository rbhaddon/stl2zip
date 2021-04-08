# stl2zip
Find and compress 3D models files on your system

## Motivation
I have thousands of 3D model files on my system. Many of them come with
text and pictures describing the models. I don't want to compress those because
A) I like easy access to browsing the pictures, and B) most computer graphics
are already compressed. So compressing entire directory structures is not what
I want, but neither do I want to spend the time compressing each model file.
This script does that for me.

## Examples
`stl2zip /path/to/models`

`stl2zip --ascii-only /path/to/models`
Only compress ASCII formatted STL files. These compress down really well, like
~90%, whereas binary formatted STL files compress down around 30%.

`stl2zip --delete /path/to/models`
Deletes the 3D model files after they have been successfully zipped.
