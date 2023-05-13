from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("scene",  ["scene.py"]),
    Extension("raster",  ["raster.py"]),
    Extension("vector",  ["vector.py"]),
]

setup(
    name='SceneFromGIS',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
