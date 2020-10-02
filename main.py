import os
import shutil

src = "./dependincies"

targetPath = '/Among Us_Data/Plugins/X86'


def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result


print("Welcome To Cosmong Us!")
try:
    gamePath = find_files("Among Us.exe", "D:/Program Files (x86)")

except:
    print("Directory was unable to be found")
    gamePath = input("Where is the Among Us Folder Located")

os.rename("D:/Program Files (x86)/Steam/steamapps/common/Among Us/Among Us_Data/Plugins/X86/steam_api.dll",
          "D:/Program Files (x86)/Steam/steamapps/common/Among Us/Among Us_Data/Plugins/X86/steam_api_o.dll")
for file in os.listdir(src):
    print(file)
    shutil.copy2(src + '/' + file, gamePath + targetPath)
