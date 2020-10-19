import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *
#GUI WINDOW
root=Tk()
root.minsize(300,300)

listofsongs=[]
v=StringVar()
songlabel=Label(root,textvariable=v,width=40)
index=0
#UPDATING SONG NAME
def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    #return  songname
#NEXT SONG
def nextsong(event):
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
#PREVIOUS SONG
def prevsong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
#STOP SONG
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return  songname
#START SONG
def start(event):
    pygame.mixer.music.play()
#ASKING FOR FOLDER
def directorychooser():
    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])


directorychooser()

#WINDOW DESIGN
label=Label(root,text="Music Player",font=('AR DELANEY',28))
label.pack()

listbox=Listbox(root)
listbox.pack()
listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)
listofsongs.reverse()

startbutton=Button(root,text="Start",fg="green")
startbutton.pack()
nextbutton=Button(root,text="Next Song",fg="blue")
nextbutton.pack()
previousbutton=Button(root,text="Previous Song",fg="blue")
previousbutton.pack()
stopbutton=Button(root,text="Stop",fg="red")
stopbutton.pack()
startbutton.bind("<Button-1>",start)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()