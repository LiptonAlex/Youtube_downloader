import tkinter
import customtkinter
import os
from pytube import YouTube


def downloader():
    try:
        url = YouTube(link.get(), on_progress_callback=on_progress)
        audio = url.streams.get_audio_only()
        path = "Downloads\Audios"

        title.configure(text=url.title)
        finishLabel.configure(text="")
        audio.download(output_path=path)


        #command = f"ffmpeg -i {file_name} {file_without_ext}.mp3"
        #os.system(command)
        #os.remove(file_name)

        finishLabel.configure(text="Download Complete!")
    except:
        finishLabel.configure(text="Something was wrong... \n Check the link and try again!")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    perc = str(int(percentage_of_completion))
    progress.configure(text=perc + "%")
    progress.update()
    progress_bar.set(float(percentage_of_completion) / 100)


# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Audio Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube video link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Bar
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progress_bar = customtkinter.CTkProgressBar(app, width= 400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=20)

# Main button
download = customtkinter.CTkButton(app, text="Download", command=downloader)
download.pack(padx=10, pady=20)

app.mainloop()