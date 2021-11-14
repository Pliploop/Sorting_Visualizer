from tkinter import *
from tkinter import ttk
import random
from colors import *
import numpy as np


from sorting_algos.bubbleSort import bubble_sort
from sorting_algos.mergeSort import merge_sort

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sorting Algorithms Visualization")
        self.window.maxsize(1000, 700)
        self.window.config(bg = WHITE)

        self.algorithm_name = StringVar()
        self.algo_list = ['Bubble Sort', 'Merge Sort']

        self.speed_name = StringVar()
        self.speed_list = ['Fast', 'Medium', 'Slow']

        self.data = []

        
        self.UI_frame = Frame(self.window, width= 900, height=300, bg=WHITE)
        self.UI_frame.grid(row=0, column=0, padx=10, pady=5)


        self.l1 = Label(self.UI_frame, text="Algorithm: ", bg=WHITE)
        self.l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.algo_menu = ttk.Combobox(self.UI_frame, textvariable=self.algorithm_name, values=self.algo_list)
        self.algo_menu.grid(row=0, column=1, padx=5, pady=5)
        self.algo_menu.current(0)


        self.l2 = Label(self.UI_frame, text="Sorting Speed: ", bg=WHITE)
        self.l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.speed_menu = ttk.Combobox(self.UI_frame, textvariable=self.speed_name, values=self.speed_list)
        self.speed_menu.grid(row=1, column=1, padx=5, pady=5)
        self.speed_menu.current(0)

        self.l3 = Label(self.UI_frame, text="Data size", bg = WHITE)
        self.l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.data_size_entry = ttk.Entry(self.UI_frame, textvariable='Enter your data size here')
        self.data_size_entry.grid(row=2, column=1, padx=5, pady=5)

        self.b1 = Button(self.UI_frame, text="Sort", command=lambda : self.sort(), bg=LIGHT_GRAY)
        self.b1.grid(row=2, column=2, padx=5, pady=5)


        self.b3 = Button(self.UI_frame, text="Generate Array", command=lambda: self.generate(int(self.data_size_entry.get())), bg=LIGHT_GRAY)
        self.b3.grid(row=2, column=3, padx=5, pady=5)

        self.canvas = Canvas(self.window, width=800, height=400, bg=WHITE)
        self.canvas.grid(row=1, column=0, padx=10, pady=5)


    def drawData(self,data, colorArray):
        self.canvas.delete("all")
        canvas_width = 800
        canvas_height = 400
        x_width = canvas_width / (len(data) + 1)
        offset = 4
        spacing = 2
        normalizedData = [i / max(data) for i in data]

        for i, height in enumerate(normalizedData):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 390
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

        self.window.update_idletasks()





    def generate(self,size):
        global data

        data = np.random.rand(size)

        self.drawData(data, [BLUE for x in range(len(data))])

    def set_speed(self):
        if self.speed_menu.get() == 'Slow':
            return 0.1
        elif self.speed_menu.get() == 'Medium':
            return 0.01
        else:
            return 0.0001

    def sort(self):
        global data
        timeTick = self.set_speed()
        
        if self.algo_menu.get() == 'Bubble Sort':
            bubble_sort(data, self.drawData, timeTick)
        elif self.algo_menu.get() == 'Merge Sort':
            merge_sort(data, 0, len(data)-1, self.drawData, timeTick)




        

    def mainloop(self):
        self.window.mainloop()

if __name__ == "__main__":
    sorter_instance = Window()
    sorter_instance.mainloop()