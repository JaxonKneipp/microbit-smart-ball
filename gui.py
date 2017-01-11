import tkinter as tk

class Application(tk.Frame):
    
    def __init__(self, master=None):
        
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.geometry("1000x500")
        self.create_widgets()

    def create_widgets(self):
        
        self.smartSoccerLabel = tk.Label(self, text="Smart ball", font=("Monospace", 25), pady=10)
        self.smartSoccerLabel.pack()

        self.attributionLabel = tk.Label(self, text="by Jaxon Kneipp, Sean Hall, Kim Armstrong and Alice Cao", font=("Monospace", 10))
        self.attributionLabel.pack()

        self.welcomeLabel = tk.Label(self, text="Welcome, Please enter the name of your team.", font=("Monospace", 12))
        self.welcomeLabel.pack()
        
        self.teamNameEntry = tk.Entry(self)
        self.teamNameEntry.pack()

        b = tk.Button(self, text="OK", command=self.submit_text)
        b.pack()

        
    def submit_text(self):
        print(self.teamNameEntry.get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
