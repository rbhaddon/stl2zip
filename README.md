# stl2zip
Find and compress 3D models files on your system

## Motivation
I have thousands of 3D model files on my system. Many of them come with
text and pictures describing the models. I don't want to compress those because
A) I like easy access to browsing the pictures, and B) most computer graphics
are already compressed. So compressing entire directory structures is not what
I want, but neither do I want to spend the time compressing each model file.
This script does that for me. See `Example` below for a better idea of what I
am talking about.

## Usage
`stl2zip /path/to/models`

`stl2zip --ascii-only /path/to/models`
Only compress ASCII formatted STL files. These compress down really well, like
~90%, whereas binary formatted STL files compress down around 30%.

`stl2zip --delete /path/to/models`
Deletes the 3D model files after they have been successfully zipped.

## Installation

You just need Python3 installed.  I used 3.8, but it might work on anything
newer than 3.3.

It should work on Linux, macOS, and Windows but I have only tested on macOS.

## Example
Let's say I have this directory structure for my models. I actually have
thousands more models from many designers, but this is good for illustraton.

```
.
└── patreon
    ├── README.md
    └── duncanlouca
        ├── README.md
        ├── ceratosaurus
        │   ├── README.md
        │   ├── ceratosaurus.png
        │   ├── ceratosaurus_arm1.stl
        │   ├── ceratosaurus_arm2.stl
        │   ├── ceratosaurus_body.stl
        │   ├── ceratosaurus_leg1.stl
        │   └── ceratosaurus_leg2.stl
        ├── goblins
        │   ├── Armoured_Goblin1.stl
        │   ├── Armoured_Goblin2.stl
        │   ├── Armoured_Goblin3.stl
        │   ├── Goblin1.stl
        │   ├── Goblin2.stl
        │   ├── Goblin3.stl
        │   ├── README.md
        │   └── goblins.png
        ├── hill_giant
        │   ├── HillGiant_body.stl
        │   ├── HillGiant_left.stl
        │   ├── HillGiant_right.stl
        │   ├── README.md
        │   ├── giant_hill_solid.stl
        │   └── hill_giant.png
        ├── knight
        │   ├── Knight.stl
        │   ├── Knight_base.stl
        │   ├── README.md
        │   └── knight.png
        └── plague_knight
            ├── PlagueKnight_No_tongue.stl
            ├── PlagueKnight_body.stl
            ├── PlagueKnight_tongue.stl
            ├── README.md
            └── plague_knight.png
```            

I have documents and reference pictures scattered throughout this directory
structure. I want to compress all the STLs while leaving the rest untouched for
quick and easy access. These files currently weigh in at 369 MB.

```
% ~/wd/stl2zip/stl2zip.py --delete .
Using path: .
Compressing patreon/duncanlouca/ceratosaurus/ceratosaurus_arm1.stl
Compressing patreon/duncanlouca/ceratosaurus/ceratosaurus_arm2.stl
Compressing patreon/duncanlouca/ceratosaurus/ceratosaurus_body.stl
Compressing patreon/duncanlouca/ceratosaurus/ceratosaurus_leg1.stl
Compressing patreon/duncanlouca/ceratosaurus/ceratosaurus_leg2.stl
Compressing patreon/duncanlouca/goblins/Armoured_Goblin1.stl
Compressing patreon/duncanlouca/goblins/Armoured_Goblin2.stl
Compressing patreon/duncanlouca/goblins/Armoured_Goblin3.stl
Compressing patreon/duncanlouca/goblins/Goblin1.stl
Compressing patreon/duncanlouca/goblins/Goblin2.stl
Compressing patreon/duncanlouca/goblins/Goblin3.stl
Compressing patreon/duncanlouca/hill_giant/giant_hill_solid.stl
Compressing patreon/duncanlouca/hill_giant/HillGiant_body.stl
Compressing patreon/duncanlouca/hill_giant/HillGiant_left.stl
Compressing patreon/duncanlouca/hill_giant/HillGiant_right.stl
Compressing patreon/duncanlouca/knight/Knight.stl
Compressing patreon/duncanlouca/knight/Knight_base.stl
Compressing patreon/duncanlouca/plague_knight/PlagueKnight_body.stl
Compressing patreon/duncanlouca/plague_knight/PlagueKnight_No_tongue.stl
Compressing patreon/duncanlouca/plague_knight/PlagueKnight_tongue.stl
Elapsed Time: 23.4s.
*.stl:
    Files found      : 20
    Files compressed : 20
Total space saved due to compression: 8.2e+01 MB
```

I got back 82 MB out of 369 MB, or 22%. Not great, but not terrible either.

And the directory structure now looks like:

```
.
└── patreon
    ├── README.md
    └── duncanlouca
        ├── README.md
        ├── ceratosaurus
        │   ├── README.md
        │   ├── ceratosaurus.png
        │   ├── ceratosaurus_arm1.zip
        │   ├── ceratosaurus_arm2.zip
        │   ├── ceratosaurus_body.zip
        │   ├── ceratosaurus_leg1.zip
        │   └── ceratosaurus_leg2.zip
        ├── goblins
        │   ├── Armoured_Goblin1.zip
        │   ├── Armoured_Goblin2.zip
        │   ├── Armoured_Goblin3.zip
        │   ├── Goblin1.zip
        │   ├── Goblin2.zip
        │   ├── Goblin3.zip
        │   ├── README.md
        │   └── goblins.png
        ├── hill_giant
        │   ├── HillGiant_body.zip
        │   ├── HillGiant_left.zip
        │   ├── HillGiant_right.zip
        │   ├── README.md
        │   ├── giant_hill_solid.zip
        │   └── hill_giant.png
        ├── knight
        │   ├── Knight.zip
        │   ├── Knight_base.zip
        │   ├── README.md
        │   └── knight.png
        └── plague_knight
            ├── PlagueKnight_No_tongue.zip
            ├── PlagueKnight_body.zip
            ├── PlagueKnight_tongue.zip
            ├── README.md
            └── plague_knight.png
```

So that's it.  Pretty simple idea and script, but I hope others find it useful.

