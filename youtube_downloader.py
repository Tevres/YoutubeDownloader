import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def is_yt_dlp_installed():
    """Checks whether yt-dlp is installed."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False

def download_video_or_playlist(url, destination, file_format):
    """
    Downloads a YouTube video or playlist and saves it with channel name.
    :param url: The URL of the video or playlist
    :param destination: The destination folder for the download
    :param file_format: The desired format ('mp3', 'mp4', 'flac', 'best')
    """
    if not is_yt_dlp_installed():
        messagebox.showerror("Fehler", "yt-dlp ist nicht installiert. Installiere es mit 'pip install yt-dlp'.")
        return

    os.makedirs(destination, exist_ok=True)
    filename = "%(title)s - %(uploader)s.%(ext)s" 
    new_filename = filename.replace(' - Topic', '') # Try to Remove ' - Topic' from the file name
    output_template = os.path.join(destination, new_filename) 

    command = ["yt-dlp", "-o", output_template, url]

    if file_format in ["mp3", "flac"]:
        command.extend(["-x", "--audio-format", file_format])
    elif file_format == "mp4":
        command.extend(["-f", "bestvideo+bestaudio[ext=m4a]", "--merge-output-format", "mp4"])
    elif file_format == "best":
        command.extend(["-f", "bestaudio"])

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Erfolg", "Download abgeschlossen!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"Fehler beim Herunterladen: {e}")
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def on_download_click():
    """Funktion, die ausgeführt wird, wenn der Download-Button geklickt wird."""
    url = url_entry.get().strip()
    file_format = format_var.get().strip().lower()

    if not url:
        messagebox.showwarning("Warnung", "Bitte gib einen YouTube-Link ein.")
        return

    if file_format not in ["mp3", "mp4", "flac", "best"]:
        messagebox.showwarning("Warnung", "Bitte wähle ein gültiges Format (mp3, mp4, flac, best).")
        return

    dirname = os.path.dirname(__file__)
    destination = os.path.join(dirname, "downloads")
    download_video_or_playlist(url, destination, file_format)

# Create the GUI
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x300")

# URL input field
url_label = tk.Label(root, text="YouTube-URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

# Format selection
format_label = tk.Label(root, text="Wähle das Format:")
format_label.pack(pady=10)
format_var = tk.StringVar(value="mp3")
format_menu = tk.OptionMenu(root, format_var, "mp3", "mp4", "flac", "best")
format_menu.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download starten", command=on_download_click)
download_button.pack(pady=20)

# Start the GUI
root.mainloop()
