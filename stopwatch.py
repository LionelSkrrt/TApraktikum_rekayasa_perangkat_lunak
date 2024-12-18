import tkinter as tk
from datetime import timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")

        self.running = False
        self.time = timedelta()

       
        self.label = tk.Label(
            root, 
            text="00:00:00", 
            font=("Helvetica", 36, "bold"), 
            fg="white", 
            bg="#282c34"
        )
        self.label.pack(pady=30)

        
        button_frame = tk.Frame(root, bg="#282c34")
        button_frame.pack(pady=20)

        
        self.start_button = tk.Button(
            button_frame, 
            text="Start", 
            command=self.start, 
            font=("Helvetica", 14), 
            bg="#4CAF50", 
            fg="white", 
            width=10
        )
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(
            button_frame, 
            text="Stop", 
            command=self.stop, 
            font=("Helvetica", 14), 
            bg="#f44336", 
            fg="white", 
            width=10
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(
            root, 
            text="Reset", 
            command=self.reset, 
            font=("Helvetica", 14), 
            bg="#555555", 
            fg="white", 
            width=10
        )
        self.reset_button.pack(pady=10)

        self.checkpoint_button = tk.Button(
            root, 
            text="Checkpoint", 
            command=self.checkpoint, 
            font=("Helvetica", 14), 
            bg="#FFA500", 
            fg="white", 
            width=10
        )
        self.checkpoint_button.pack(pady=10)

        self.checkpoint_text = tk.Text(
            root, 
            height=5, 
            width=40, 
            font=("Helvetica", 12), 
            bg="#333333", 
            fg="white"
        )

        self.checkpoint_text.pack(pady=10)
        self.checkpoint_text.insert("1.0", "waktu checkpoint: \n")
        self.checkpoint_text.config(state="disabled")

        self.exit_button = tk.Button(
        root,
        text="Exit",
        command=self.exit,
        font=("Helvetica", 14),
        bg="#000000",
        fg="white",
        width=10
        )
        self.exit_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


        self.update_time()

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        
            self.stop()
            self.time = timedelta()
            self.label.config(text="00:00:00")
            self.checkpoint_text.config(state="normal")
            self.checkpoint_text.delete("1.0", "end")
            self.checkpoint_text.insert("1.0", "waktu checkpoint: \n")
            self.checkpoint_text.config(state="disabled")

    def checkpoint(self):
        
        formatted_time = str(self.time).split(".")[0]
        print(f"Checkpoint: {formatted_time}")  
        self.checkpoint_text.config(state="normal")
        self.checkpoint_text.insert("end", f"{formatted_time}\n")
        self.checkpoint_text.config(state="disabled")
        self.checkpoint_text.see("end")  

    def exit(self):
        self.root.quit()

    def update_time(self):
        if self.running:
            self.time += timedelta(seconds=1)
            formatted_time = str(self.time).split(".")[0]  
            self.label.config(text=formatted_time)
            self.root.after(1000, self.update_time)


root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()