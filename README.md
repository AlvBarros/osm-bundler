# osm-bundler for Windows 64 bits
3D geometry reconstruction for OpenStreetMap

> We research and develop software to reconstruct 3D geometry from a set of photos. Our software can be used in a variety of ways, in particular in the OpenStreetMap project.
> You can subscribe to [our blog](http://opensourcephotogrammetry.blogspot.com/).
> License: GNU GPL v3

> The core tools in our system are 
> - Bundler;
> - PMVS;
> - VS.

# Installing / Running Application 

The easiest way to install osm-bundler is described here. Alternatively you can compose it yourself from several pieces. See CreateDistributionYourself for the details.

# Installation
- Install Python 2.7
- Install Pillow library for Python

It's that easy.

# Running
Normally you would run osm-bundler in the following way:
```
python path_to/RunBundler.py --photo="path_to/photos" 
```
With the following results folder, you can run:
```
python path_to/RunPMVS.py --bundlerOutputPath="path_to/previous_command_results"
```
And finnaly, with the same path:
```
python path_to/RunCMVS.py --bundlerOutputPath="same_path/as_before"
```

To see help just run:
```
python path_to/RunBundler.py
```

# Photo test set
You could try our photo test set: http://osm-bundler.googlecode.com/files/example_OldTownHall.zip
