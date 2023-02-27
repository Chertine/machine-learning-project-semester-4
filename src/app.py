import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import array
from pandas import DataFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.__createWidgets()
        self.__getValue()
        self.__dfInit()
        
    def __createWidgets(self):
        self.canvas1 = tk.Canvas(self, width=1200, height=800)
        self.canvas1.pack()
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.fig1, self.ax1 = plt.subplots(figsize=(4, 4))
        self.w = FigureCanvasTkAgg(self.fig1, self).get_tk_widget()
        self.fig2, self.ax2 = plt.subplots(figsize=(4, 4))
        self.e = FigureCanvasTkAgg(self.fig2, self).get_tk_widget()
        
    def __getValue(self):
        self.age = self.entry1.get()
        self.salary = self.entry2.get()
        
    def __dfInit(self):
        self.array = array([[self.age, self.salary]])
        self.df = DataFrame(data=self.array, index=[400], columns=['Age', 'EstimatedSalary'])
        