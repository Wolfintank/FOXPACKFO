import tkinter
import tkinter.filedialog as FD
import tkinter.simpledialog as SD
import os
import tkinter.ttk

import Main

def ChooseDir():
    DirectoryPath["text"] = FD.askdirectory()

#Main Window Creation
MainWindow = tkinter.Tk(className="FOXPACKFO")
OverallText = tkinter.ttk.Label(MainWindow,text="Progress")
OverallText.grid(row=0,column=1)
OverallProgress = tkinter.ttk.Progressbar(MainWindow,maximum=3)
OverallProgress.grid(row=1,column=1)
ProcessText = tkinter.ttk.Label(MainWindow,text="")
ProcessText.grid(row=2,column=1)
ProcessProgress = tkinter.ttk.Progressbar(MainWindow,maximum=0)
ProcessProgress.grid(row=3,column=1)

DirectoryTitle = tkinter.ttk.Label(MainWindow,text="Directory: ")
DirectoryTitle.grid(row=4,column=0)
DirectoryPath = tkinter.ttk.Label(MainWindow,text="")
DirectoryPath.grid(row=4,column=1)
DirectoryButton = tkinter.ttk.Button(MainWindow,text="Choose Dir",command=ChooseDir)
DirectoryButton.grid(row=4,column=2)

SubDirText = tkinter.ttk.Label(MainWindow,text="Subdirectories")
SubDirText.grid(row=5,column=0)
SubDirSelect = tkinter.ttk.Combobox(MainWindow,values=["Ignore Subdirectories","Create SubDir Folder"],state="readonly")
SubDirSelect.set("Ignore Subdirectories")
SubDirSelect.grid(row=5,column=1)

StartBtn = tkinter.ttk.Button(MainWindow,text="Start",command=Main.Start)
StartBtn.grid(row=6,column=1)

LogTitle = tkinter.ttk.Label(MainWindow,text="Log:")
LogTitle.grid(row=7,column=1)
Log = tkinter.ttk.Label(MainWindow,text="")
Log.grid(row=8,column=1)

MainWindow.mainloop()