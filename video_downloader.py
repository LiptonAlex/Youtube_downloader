import tkinter
import customtkinter
from pytube import YouTube


# Downloading function
def downloader():
    try:
        url = YouTube(link.get(), on_progress_callback=on_progress)
        video = url.streams.get_highest_resolution()

        title.configure(text=url.title)
        finishLabel.configure(text="")
        video.download(output_path="Downloads\Videos")
        finishLabel.configure(text="Download Complete!")
    except:
        finishLabel.configure(text="Download Error. Check the link and try again!")


# Progress bar function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + "%")
    progress.update()
    progressbar.set(float(percentage_of_completion) / 100)


# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube video link")
title.pack(padx=20, pady=20)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress bar
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=20)

# Main button
download = customtkinter.CTkButton(app, text="Download", command=downloader)
download.pack(padx=10, pady=20)

app.mainloop()

