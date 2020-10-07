import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.classify
        self.submit.pack()

        self.movie_entry = tk.Entry(self)
        self.movie_entry.pack(side="top")
        self.moviename = tk.StringVar()
        self.movie_entry["textvariable"] = self.moviename

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def classify(self):
        print("hi there, everyone!" + self.moviename.get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()