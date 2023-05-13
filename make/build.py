import os
import glob
import shutil

path = r'../*.py'
files = glob.glob(path)

# copy all modules

for file in files:
    src = file
    dst = os.path.basename(file)
    shutil.copyfile(src, dst)

# cython compile modules
os.system('python build_cython.py build_ext --inplace')

# delete compiled modules
for file in ['scene.py', 'raster.py', 'vector.py']:
    os.remove(file)

# pyinstaller build
os.system('python build_pyinstaller.py')

# cleanup
for file in files:
    dst = os.path.basename(file)
    if os.path.isfile(dst):
        os.remove(dst)

for file in glob.glob(r'./*.c'):
    os.remove(file)
for file in glob.glob(r'./*.pyd'):
    os.remove(file)
