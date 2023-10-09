import os

dir_principal = os.getcwd()
dir_modules = dir_principal + "/modules"
dir_c1 = dir_principal + "/c1"
dir_c2 = dir_principal + "/c2"
dir_readme = dir_modules + "/README.txt"
dir_modules_archivo_c1 = dir_modules + "/archivo_c1.txt"
dir_modules_archivo_c2 = dir_modules + "/archivo_c2.txt"
dir_modules_archivo_c1_copia = dir_modules + "/archivo_c1_copia.txt"
dir_modules_archivo_c2_copia = dir_modules + "/archivo_c2_copia.txt"

os.chdir(dir_c1)
with open("archivo_c1.txt", "w") as archivo_c1:
    archivo_c1.write("texto que va dentro del archivo_c1 bla bla bla")

os.chdir(dir_c2)
with open("archivo_c2.txt", "w") as archivo_c2:
    archivo_c2.write("texto que va dentro del archivo_c2 bla bla bla")

os.chdir(dir_modules)
os.remove(dir_readme)
os.remove(dir_modules_archivo_c1_copia)
os.remove(dir_modules_archivo_c2_copia)
os.chdir(dir_principal)
os.rmdir(dir_modules)
