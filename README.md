# SceneFromGIS <img src="SfGicon.png" height="32">

Create scenes for video game maps from real geographic data.


### Installation
#### Users
Download prebuild binaries for Windows x64.  
Current version : 
[Beta 2](https://mega.nz/file/iTxUXIQB#sZQjnKh52rTiwludeLnHIAf-K33mq5LLK6fDHcjpYLs)

#### Developers
Create a virtual environment and install [requirements](#Requirements).

You will probably need to mix pip and conda to install everything depending on
your operating system.  
When using pip to install some dependencies, you need to make sure that all
dependencies are installed correctly.
Depending on your platform, you might need to compile and install
C dependencies manually.
Some dependencies are not available in Anaconda navigator,
so you can use pip for them.

In the rest of the documentation, we will always consider the case of the user.
The launch of the binary `SceneFromGIS.exe [...]` will be replaced by `python main.py [...]`


### Usage
#### Graphical User Interface
`> SceneFromGIS.exe`


#### Command Line Interface
**Minimal usage**
```
> SceneFromGIS.exe elevation_map.tif output_folder [optional layers]
```

**Full details**
```
usage: elevation
       output
       [--block-size BLOCK_SIZE]
       [--crs CRS]
       [--z-factor Z_FACTOR]
       [--elevation-smoothing ELEVATION_SMOOTHING]
       [--path-line PATH_LINE [PATH_LINE ...]]
       [--building-line BUILDING_LINE [BUILDING_LINE ...]]
       [--building-polygon BUILDING_POLYGON [BUILDING_POLYGON ...]]
       [--forest-line FOREST_LINE [FOREST_LINE ...]]
       [--forest-polygon FOREST_POLYGON [FOREST_POLYGON ...]]
       [--forest-point FOREST_POINT [FOREST_POINT ...]]
       [--water-line WATER_LINE [WATER_LINE ...]]
       [--water-polygon WATER_POLYGON [WATER_POLYGON ...]]

positional arguments:
  elevation
  output

optional arguments:
  --z-factor Z_FACTOR
  --elevation-smoothing ELEVATION_SMOOTHING
  
add layer arguments:
  --block-size BLOCK_SIZE
  --crs CRS
  --path-line PATH_LINE [PATH_LINE ...]
  --building-line BUILDING_LINE [BUILDING_LINE ...]
  --building-polygon BUILDING_POLYGON [BUILDING_POLYGON ...]
  --forest-line FOREST_LINE [FOREST_LINE ...]
  --forest-polygon FOREST_POLYGON [FOREST_POLYGON ...]
  --forest-point FOREST_POINT [FOREST_POINT ...]
  --water-line WATER_LINE [WATER_LINE ...]
  --water-polygon WATER_POLYGON [WATER_POLYGON ...]

add layer optional arguments (line and polython only):
  *dilation DILATION
  *flattening FLATTENING
  *elevation-difference ELEVATION_DIFFERENCE
usage: filename [*dilation DILATION] [*flattening FLATTENING] [*elevation-difference ELEVATION_DIFFERENCE]
```

**Some examples**
```
> SceneFromGIS.exe
data/Cardet/ALTI_CLIP_1k5.tif
output/Cardet
--path-line data/Cardet/path-line.shp *dilation 3
--path-line data/Cardet/path-line-important.shp *dilation 5 *flattening 2
--building-line data/Cardet/building-line.shp *dilation 2 *flattening 3
--building-polygon data/Cardet/building-polygon.shp *flattening 3
--forest-line data/Cardet/forest-line.shp
--forest-polygon data/Cardet/forest-polygon.shp
--forest-point data/Cardet/forest-point.shp
--water-line data/Cardet/water-line.shp *dilation 5 *flattening 2 *elevation-difference -5
--water-polygon data/Cardet/water-polygon.shp *dilation 2 *flattening 3 *elevation-difference -5
```


### How to use it for video game maps ?
To create maps for games, you will need to go through the following steps :
1. [Get and prepare geographic data](#get-and-prepare-geographic-data)
3. [Convert geographic data using SceneFromGIS](#convert-geographic-data-using-SceneFromGIS)
4. [Import scene data to game editor](#import-scene-data-to-game-editor)

#### Get and prepare geographic data
[Tutorial](https://docs.google.com/document/d/1kLQgOUDipBHRCMN29pi7MnWtXafHJXnVJtyrRn5T8X4)

#### Convert geographic data using SceneFromGIS
[Tutorial](https://docs.google.com/document/d/1BkWSHitI2b5kh3-Jq66k5U5bj9eadZvMU_zNiOZynt4)

#### Import scene data to game editor
This step really depend on the game you target, for now, good luck !


### Requirements
* PyQt5 (GUI)
* GeoPandas (GIS vector)
* Rasterio (GIS raster)
* PyVista (3D view) and pyvistaqt (PyQt implementation)
* NumPy (data processing)
* SciPy (image processing)
* scikit-image (image processing)
* edt (Euclidean Distance Transform for image processing)
* matplotlib (data view (used in debug))


### About Development Choices
**main** script is used to handle the start of the program.

**scene** module is used to abstract scene management and generation from 
the different user interfaces.

**vector** and **raster** module are used to abstract data sources from data
extraction and conversion.
* *read* : read data from source file, after this call, file is not needed anymore
* *view* : create visual representation of the source data
* *build* : build the layer for output

**mainform** and **importform** modules are Qt generated interface modules for
main form and import (add layer) form.

**ressources_rc** module is Qt generated resource module for GUI icons.

**gui** module implements **mainform** interactions.

**cli** module is used to parse args and interact with scene module.

**logger** module is used to log things, logs are saved in a log file, printed
in console and showed in GUI.

**morphology** module implement auto median morphological filter.

**utils** module implement some simple required function which we decide not to categorize.


### Todo / Not implemented yet
* Generate paths as vector data (work in progress)
* Generate 3D object
  * Terrain as 3D obj
  * Roads as 3D obj
  * Buildings as 3D obj
  * Forest as 3D obj (trees)
* Good 3D objects fit
* Export
  * New export format (e.g. adapted to Unity)

### FAQ
#### Users
Application crash and everything close before I can see any error.
> Run the application using **Command Prompt** to get the full **Traceback**.
With the traceback, you may find the source of the problem, or you can send it to me.

#### Developers
`Process finished with exit code XXXXXXXX (0xXXXXXXXX)` in PyCharm and no **Traceback**.  
> Emulate terminal in output console.

