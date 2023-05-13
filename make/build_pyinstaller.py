import PyInstaller.__main__
import pkgutil

# Fixing failed imports
hiddenimport = []

import rasterio
for package in pkgutil.iter_modules(rasterio.__path__, prefix="rasterio."):
    hiddenimport.append(package.name)
import geopandas
for package in pkgutil.iter_modules(geopandas.__path__, prefix="geopandas."):
    hiddenimport.append(package.name)
import shapely
for package in pkgutil.iter_modules(shapely.__path__, prefix="shapely."):
    hiddenimport.append(package.name)
import skimage
for package in pkgutil.iter_modules(skimage.__path__, prefix="skimage."):
    hiddenimport.append(package.name)
import skimage
for package in pkgutil.iter_modules(skimage.__path__, prefix="skimage."):
    hiddenimport.append(package.name)
import skimage.filters
for package in pkgutil.iter_modules(skimage.filters.__path__, prefix="skimage.filters."):
    hiddenimport.append(package.name)
import skimage.morphology
for package in pkgutil.iter_modules(skimage.morphology.__path__, prefix="skimage.morphology."):
    hiddenimport.append(package.name)
import scipy
for package in pkgutil.iter_modules(scipy.__path__, prefix="scipy."):
    hiddenimport.append(package.name)
import scipy.signal
for package in pkgutil.iter_modules(scipy.signal.__path__, prefix="scipy.signal."):
    hiddenimport.append(package.name)

hiddenimport.append('edt')
hiddenimport.append('morphology')
hiddenimport.append('raster')
hiddenimport.append('vector')

# PyInstaller build
args = ['main.py', '--name', 'SceneFromGIS', '--icon', '../SfGicon.ico',
        '--onefile', '-y']
for hi in hiddenimport:
    args.append(f'--hidden-import={hi}')

PyInstaller.__main__.run(args)
