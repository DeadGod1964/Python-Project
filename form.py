from tkinter import *

class Form:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack()

        self.name_label = Label(self.frame, text="Name:")
        self.name_label.pack()

        self.name_entry = Entry(self.frame)
        self.name_entry.pack()

        self.job_label = Label(self.frame, text="Job Description:")
        self.job_label.pack()

        self.job_entry = Entry(self.frame)
        self.job_entry.pack()

        self.submit_button = Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        name = self.name_entry.get()
        job = self.job_entry.get()
        print("Hello, {}!".format(name))
        print("Your job is, {}!".format(job))

if __name__ == "__main__":
    root = Tk()
    form = Form(root)
    root.mainloop()
