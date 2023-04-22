import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

class SuperformulaGUI:
    def __init__(self, master):
        # Create main window
        self.master = master
        self.master.title("Superformula Plotter")

        # Create a Frame for parameter inputs
        self.parameters_frame = tk.Frame(self.master)
        self.parameters_frame.pack(side='left', padx=20)

        # Create parameter labels and entry widgets
        tk.Label(self.parameters_frame, text='a1:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.a1_entry = tk.Entry(self.parameters_frame)
        self.a1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.parameters_frame, text='a2:').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.a2_entry = tk.Entry(self.parameters_frame)
        self.a2_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.parameters_frame, text='m:').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.m_entry = tk.Entry(self.parameters_frame)
        self.m_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.parameters_frame, text='n1:').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.n1_entry = tk.Entry(self.parameters_frame)
        self.n1_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.parameters_frame, text='n2:').grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.n2_entry = tk.Entry(self.parameters_frame)
        self.n2_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.parameters_frame, text='n3:').grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.n3_entry = tk.Entry(self.parameters_frame)
        self.n3_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create a Frame for the plot
        self.plot_frame = tk.Frame(self.master)
        self.plot_frame.pack(side='right', padx=20)

        # Create the figure and canvas for the plot
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.plot_frame)
        self.canvas.get_tk_widget().pack()

        # Create the plot button
        self.plot_button = tk.Button(self.master, text="Plot", command=self.plot)
        self.plot_button.pack(side='bottom', pady=10)

    def plot(self):
        a1 = float(self.a1_entry.get())
        a2 = float(self.a2_entry.get())
        m = float(self.m_entry.get())
        n1 = float(self.n1_entry.get())
        n2 = float(self.n2_entry.get())
        n3 = float(self.n3_entry.get())

        t = np.linspace(0, 2*np.pi, 500)
        r = ((np.power(np.abs(np.cos(m*t/4)/a1), n2) + np.power(np.abs(np.sin(m*t/4)/a2), n3))) ** (-1/n1)

        # Calculate polar coordinates
        x = r*np.cos(t)
        y = r*np.sin(t)

        # Clear the figure
        self.figure.clear()

        # Create a new axis and plot the superformula curve
        ax = self.figure.add_subplot(111, polar=True)
        ax.plot(t, r, color='black', linewidth=2)

        # Set axis limits
        r_max = max(r)
        ax.set_rlim(0, r_max)

        # Set axis labels
        ax.set_xlabel('')

        # Draw the canvas to update the plot
        self.canvas.draw()


def main():
    root = tk.Tk()
    app = SuperformulaGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()