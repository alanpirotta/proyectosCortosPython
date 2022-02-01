import os
import shutil

source = 'proyectosCortosPython/a_mover'
destination = 'proyectosCortosPython/'

files = os.listdir(source)
for file in files:
    file_name = os.path.join(source, file)
    shutil.move(file_name, destination)
print("Files Moved")