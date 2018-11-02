#==============================================================================
#Project Modules
#==============================================================================
import tkinter as tk
from tkinter import filedialog
#==============================================================================

def selectFolder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

#==============================================================================
def selectFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfile()
    return file_path
 