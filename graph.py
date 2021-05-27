#pip install matplotlib
import matplotlib.pyplot as plt

# x-axis and for pie charts it wolud be considered as label.
year = ['day-1', 'day-3', 'day-5', 'day-7']

#y-axis
plts = plt
#for simple graph
plt.plot(year,[2.0,3.56,4.54,5.0])
plt.ylabel("Level of happiness")

plt.xlabel("Number of Days")


plt.show()
#for bar graph
plts.bar(year,pop)

#for pie charts
#plt.pie(pop,labels=year)


#to display the graph


'''import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "GOGO ASSISTANT")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = "TRUE")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Create Chat window
        ChatLog = tk.Text(container, bd=0, bg="white", height="20", width="80", font="Arial",)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()       


app = SeaofBTCapp()
app.mainloop()'''