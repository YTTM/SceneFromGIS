# SceneFromGIS <img src="SfGicon.png" height="32">

Create scenes for video game maps from real geographic data.


### Installation
#### Users
Download prebuild binaries for Windows x64.  
Current version : 
[Alpha 1](https://mega.nz/file/2boFkIoS#UjOyj_9bzGoYU5mm9uPliZqP9tSONVScmpnghK4FtKE)

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
todo, see [Todo / Not implemented yet](#todo--not-implemented-yet) section.

`> SceneFromGIS.exe data/alti.tif --building-polygon data/building-polygon.shp`


### How to use it for video game maps ?
To create maps for games, you will need to go through the following steps :
1. [Get geographic data](#get-geographic-data)
2. [Prepare geographic data](#prepare-geographic-data)
3. [Convert geographic data using SceneFromGIS](#convert-geographic-data-using-SceneFromGIS)
4. [Import scene data to game editor](#import-scene-data-to-game-editor)

#### Get geographic data
todo

#### Prepare geographic data
todo

#### Convert geographic data using SceneFromGIS
todo

#### Import scene data to game editor
todo


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


### Todo / Not implemented yet
* CLI
  * Implement CLI interface
* Input data
  * Simplify the system of area / multiple heightmap
* Generate 2D object
  * Block size
* Generate paths as vector data
* Generate 3D object
  * Terrain as 3D obj
  * Roads as 3D obj
  * Buildings as 3D obj
  * Forest as 3D obj (trees)
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

