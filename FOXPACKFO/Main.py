
import WindowManager
import os
import pathlib
import shutil

from tkinter import messagebox

Directory = ""
Files = []
Extensions = []
SubDirBhvr = ""
SubDirCollection = []

def Start():
    if WindowManager.DirectoryPath["text"] == "":
        messagebox.showerror("Error","No Directory Set")
        return
    
    global Directory
    Directory = str(WindowManager.DirectoryPath["text"])
    global Files
    Files = []
    global Extensions
    Extensions = []
    global SubDirBhvr
    SubDirBhvr = WindowManager.SubDirSelect.get()
    global SubDirCollection
    SubDirCollection = []

    ScanDir()

def ScanDir():
    WindowManager.Log["text"] = "Scanning Files..."
    WindowManager.OverallText["text"] = "Scanning"

    for File in os.listdir(Directory):
        if os.path.isfile(os.path.join(Directory,File)):
            Files.append(File)
        else:
            SubDirCollection.append(File)

    if len(Files) == 0:
        messagebox.showwarning("Invalid","No Files in selected Directory \nCanceling")
        Finished()
        return()
    
    WindowManager.OverallProgress.step(1)
    WindowManager.Log["text"] += "\n" + str(len(Files)) + " Files found"

    FileExtensions()

def FileExtensions():
    WindowManager.Log["text"] += "\nGathering Filetypes..."
    WindowManager.OverallText["text"] = "Gathering Filetypes"
    WindowManager.ProcessProgress["value"] = 0
    WindowManager.ProcessProgress["maximum"] = 100
    WindowManager.ProcessText["text"] = ""

    P = 100 / len(Files)

    for File in Files:
        WindowManager.ProcessText["text"] = "Gathering Filetypes (" + File + ")"
        Extension = pathlib.Path(os.path.join(Directory,File)).suffix
        if Extension not in Extensions:
            Extensions.append(Extension)
        WindowManager.ProcessProgress.step(P)
    
    WindowManager.OverallProgress.step(1)
    WindowManager.Log["text"] += "\n" + str(len(Extensions)) + " Extensions found"

    Cleanup()

def Cleanup():
    WindowManager.Log["text"] += "\nPacking..."
    WindowManager.OverallText["text"] = "Packing"
    WindowManager.ProcessProgress["value"] = 100
    WindowManager.ProcessProgress["maximum"] = 100
    WindowManager.ProcessText["text"] = ""

    P = 100 / len(Files)

    os.mkdir(os.path.join(Directory,"FOXPACKFO_Packaged"))

    for ExtensionType in Extensions:
        CurrentPackPath = os.path.join(Directory,"FOXPACKFO_Packaged",ExtensionType)
        os.mkdir(CurrentPackPath)
        for File in Files:
            WindowManager.ProcessText["text"] = "Packing [" + ExtensionType + "] (" + File + ")"
            if pathlib.Path(os.path.join(Directory,File)).suffix == ExtensionType:
                shutil.move(os.path.join(Directory,File),os.path.join(CurrentPackPath,File))
        WindowManager.ProcessProgress.step(P)

    if SubDirBhvr == "Create SubDir Folder":
        SubdirPath = os.path.join(Directory,"FOXPACKFO_Packaged","dir")
        os.mkdir(SubdirPath)
        for Dir in SubDirCollection:
            shutil.move(os.path.join(Directory,Dir),os.path.join(SubdirPath,Dir))

    WindowManager.OverallProgress.step(1)
    WindowManager.Log["text"] += "\n" + "Packed Files in " + os.path.join(Directory,"FOXPACKFO_Packaged")

    Finished()
    
def Finished():
    WindowManager.Log["text"] += "\nFinished"
    WindowManager.OverallText["text"] = "Finished"
    WindowManager.ProcessProgress["value"] = 1
    WindowManager.ProcessProgress["maximum"] = 1
    WindowManager.ProcessText["text"] = "Packed"

    WindowManager.Log["text"] += "\nFOXPACKFO by Wolfintank"

    messagebox.showinfo("Done","Packing Finished")


    