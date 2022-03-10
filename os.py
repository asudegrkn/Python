
# os kütüphanesi

import os
print(os.name)

currentDir= os.getcwd()
print(currentDir)

#new folder

folder_name = "new folder"
os.mkdir(folder_name)

#dosya ismi değiştirme

new_folder_name = "new_folder_2"
os_rename(folder_name , new_folder_name)

os.chdir(currentDir)
print(os.getcwd())

files =os.listdir()

for f in files:
    if f.endswith(".py"):
        print(f)

os.rmdir(new_folder_name)

for i in os.walk(currentDir):
   print(i)
   
   
