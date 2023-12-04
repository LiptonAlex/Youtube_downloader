from tkinter import *
from pytube import YouTube

root = Tk()
root.resizable(0,0)
root.geometry('500x500')
root.configure(bg='red')
root.title('YouTube Downloader')

Label(root,text='Youtube Video Downloader\n Enter Link to download video below...', font='arial 15 bold', bg='red', fg='black').pack()

photo=PhotoImage(file="Youtube.png")
lbl=Label(image=photo).pack()

link=StringVar()

enter_link=Entry(root, width=70, textvariable=link).place(x=50, y=100)

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root, text='Downloaded').place(x=215, y=390)

Button(root, text='Download here', command=downloader, fg='white', bg='black').place(x=200, y=360)

mainloop()
