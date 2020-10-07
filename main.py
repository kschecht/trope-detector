import tkinter as tk
# import classifier

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def res_to_message(res):
        return "Placeholder"

    def create_widgets(self):
        message = "Welcome to Trope Detector 2020! Please enter a movie to see if it contains the following tropes:"
        trope_list = ["Orientalism", "Gambit Pileup", "White Savior"]

        self.intro = tk.Label(self, text=message)
        self.intro.pack()
        self.trope_list = tk.Label(self, text=', '.join(trope_list))
        self.trope_list.pack()

        self.movie_entry = tk.Entry(self)
        self.movie_entry.pack()
        self.moviename = tk.StringVar()
        self.movie_entry["textvariable"] = self.moviename

        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.classify
        self.submit.pack()

        self.response = tk.Label(self)
        self.response.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def classify(self):
        error_message = "Sorry, Link! I can't GIVE tropes. Come back when you're a little.... mmmmmmm... tropier!"
        try:
            res = classifier.classify(self.moviename.get())
            self.response.configure(text=res_to_message(res))
        except ValueError as e:
            print("Oops! There was an issue processing the movie")
        except Exception as e:
            self.response.configure(text=error_message)
            print(e)

root = tk.Tk()
app = Application(master=root)
app.mainloop()