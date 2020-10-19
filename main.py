import shutil
from tkinter import *
import os
from tkinter import filedialog
from shutil import copyfile
import sys

gamePath = 'C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley'
filename = filedialog.askopenfilename
root = Tk()

def browseFolder():
    global gamePath
    folder_selected = filedialog.askdirectory()
    gamePath = folder_selected


def install():
    global gamePath
    if os.path.isfile(gamePath + "/Among Us_Data/Plugins/X86/steam_api_o.dll"):
        print("Game has been modified")
    else:
        try:
            os.rename("D:/Program Files (x86)/Steam/steamapps/common/Among Us/Among Us_Data/Plugins/X86/steam_api.dll",
                      "D:/Program Files (x86)/Steam/steamapps/common/Among Us/Among Us_Data/Plugins/X86/steam_api_o.dll")
        except:
            print("steam_api not found")

    if os.path.isfile(gamePath + "/Among Us_Data/Plugins/X86/cream_api.ini"):
        print("config installed")
    else:
        if os.path.isfile(os.getcwd() + "/dependencies"):
            for file in os.listdir(os.getcwd()):
                print(file)

    if os.path.isfile(gamePath + "/Among Us_Data/Plugins/X86/cream_api.ini"):
        print("config installed")
    else:
        if os.path.isfile(os.getcwd() + "/dependencies/steam_api.dll"):
            for file in os.listdir(os.getcwd() + "/dependencies"):
                shutil.copy(os.getcwd() + "/dependencies/" + file, gamePath + "/Among Us_Data/Plugins/X86/")
                print(file + " Successfully Copied")


text1 = Label(root, text="Welcome To Cosmong Us!")
BrowseButton = Button(root, text="Browse", command=browseFolder)

installButton = Button(root, text="install", command=install)
installButton.pack(side=BOTTOM)
BrowseButton.pack()
text1.pack()

mainloop()
