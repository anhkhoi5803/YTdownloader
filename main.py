
from cgitb import text
from select import select
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    path= filedialog.askdirectory()
    path_label.config(text=path)


def download():
    get_link=link_field.get()
    user_path=path_label.cget("text")
    screen.title('downloading..')

    mp4vid = YouTube(get_link).streams.get_highest_resolution().download()
    vidclip = VideoFileClip(mp4vid)
    vidclip.close()
    shutil.move(mp4vid,user_path)
    screen.title('download completed!')


screen=Tk()
title = screen.title('YT downloader') 
canvas = Canvas(screen, width=500,height=500)
canvas.pack()

logo=PhotoImage(file='yt.png')
logo=logo.subsample(2,2)
canvas.create_image(250,80,image=logo)

link_field=Entry(screen,width=50)
link_label=Label(screen, text="Enter Download Link:",font=('Arial',15))

path_label = Label(screen, text="Select path",font=('Arial',15))
select_btn=Button(screen,text="Select",command=select_path)

canvas.create_window(250,280,window=path_label)
canvas.create_window(250,320,window=select_btn)


canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)

download_btn = Button(screen, text="Download file", command=download)
canvas.create_window(250,390,window=download_btn)


screen.mainloop()