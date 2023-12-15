import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog

class VideoTrimmerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Video Trimmer")

        self.start_time_label = tk.Label(master, text="Start Time (s):")
        self.start_time_label.grid(row=0, column=0)
        self.start_time_entry = tk.Entry(master)
        self.start_time_entry.grid(row=0, column=1)

        self.end_time_label = tk.Label(master, text="End Time (s):")
        self.end_time_label.grid(row=1, column=0)
        self.end_time_entry = tk.Entry(master)
        self.end_time_entry.grid(row=1, column=1)

        self.choose_file_button = tk.Button(master, text="Choose Video File", command=self.choose_file)
        self.choose_file_button.grid(row=2, column=0, columnspan=2)

        self.trim_button = tk.Button(master, text="Trim Video", command=self.trim_video)
        self.trim_button.grid(row=3, column=0, columnspan=2)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            self.video_path = file_path

    def trim_video(self):
        start_time = float(self.start_time_entry.get())
        end_time = float(self.end_time_entry.get())

        video = VideoFileClip(self.video_path).subclip(start_time, end_time)

     
        transform = transforms.Compose([transforms.ToTensor(), transforms.Resize((224, 224))])

        frames = [transform(frame) for frame in video.iter_frames()]

       

   
        processed_video = video.set_sequence(frames)
        processed_video.write_videofile("output_processed.mp4", codec="libx264", fps=video.fps)

        video.reader.close()
        del video

def main():
    root = tk.Tk()
    app = VideoTrimmerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
