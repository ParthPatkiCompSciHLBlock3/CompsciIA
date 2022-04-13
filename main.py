from tkinter import * #used for GUI
from tkinter import ttk
import solver_UI

if __name__ == "__main__":
    window = Tk()
    window.title("Rubik's Cube Solver")
    window.geometry("1400x800")
    tabctrl = ttk.Notebook(window)
    tabA = ttk.Frame(tabctrl)
    tabB = ttk.Frame(tabctrl)
    solver_UI.main(tabA)
    x = Frame(tabB,width = 950, height = 670)
    x.place(relx=0.5, rely=0.5,anchor = "center")
    tabctrl.add(tabA,text = "Solve")
    tabctrl.pack()
    window.mainloop()