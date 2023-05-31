import tkinter as tk # Alias is used as it is more concise
from tkinter import ttk # Improved tkinter module 


class Program(tk.Tk): # Main program window that instantiates all the child classes and runs the mainloop() of its tk.Tk instance

    def __init__(self, title, size): # Core initialisation parameters
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # Program elements split into widget type
        self.entries = Entries(self) # Deferred initialisation is used to keep the main class's __init__ constructure cleaner
        self.output = Output(self)
        self.buttons = Buttons(self, self.entries, self.output)
    
        # Run file menu function
        self.createFileMenu()

    def createFileMenu(self):
        # Creating main menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Creating accessibility options menu
        self.helpMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Accessibility Options", menu=self.helpMenu)

        # Creating options within the accessibility menu
        self.helpMenu.add_command(label="Toggle high contrast") # Add commands later
        self.helpMenu.add_separator()

        # Creating font size menu and adding 3 presets
        self.sizeMenu = tk.Menu(self.helpMenu) 
        self.helpMenu.add_cascade(label="Font Size", menu=self.sizeMenu)  # Adding cascade to sizeMenu

        self.sizeMenu.add_command(label="Large") # Add commands later
        self.sizeMenu.add_command(label="Medium")
        self.sizeMenu.add_command(label="Small")

        # Run program
        self.mainloop()
    


class Entries(ttk.Frame):
    
    def __init__(self, parent): # Second argument allows the main instance (self) of Program() to be passed to Entries() for inheritance
        super().__init__(parent) # Ensures proper inheritane of parent class (in this case, Program())
        self.place(x = 0, y = 0) # Placing window in which this class's widgets will be stored (like a subfolder)

        # Calling widget generator and placer functions
        self.entryGen() 
        self.entryPlacer()
    
    def entryGen(self): # Create entry widgets
        self.firstTerm = ttk.Entry(self) # Make widgets members of the object and not stay in the local scope of the function
        self.commonDifference = ttk.Entry(self)
        self.numberOfTerms = ttk.Entry(self)
    
    def entryPlacer(self): # Place entry widgets
        self.firstTerm.pack()
        self.commonDifference.pack()
        self.numberOfTerms.pack()


class Output(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 70) # Must place accurately later !!!

        self.outputGen()
        self.outputPlacer()

    def outputGen(self):
        self.sum = tk.Text(self)

    def outputPlacer(self):
        self.sum.pack()
    


class Buttons(ttk.Frame):

    def __init__(self, parent, entries, output):
        super().__init__(parent)
        self.place(x = 0, y = 0)

        self.entries = entries # Saving passed arguments of Entries and Output classes
        self.output = output

        self.buttonGen()
        self.buttonPlacer()
        
    def buttonGen(self):
        self.clear = ttk.Button(self, text = "Clear", command = self.clear)
        self.calculate = ttk.Button(self, text = "Calculate", command = self.calculate)
    
    def buttonPlacer(self):
        self.clear.pack()
        self.calculate.pack()
    
    def clear(self):
        pass
        
    def calculate(self):
        try:
            pass
        
        except Exception as ex:
            print(ex)


# Instantiating the Program() class
Program("Calculator", (500, 500))