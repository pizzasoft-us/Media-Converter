import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import os

global tasks
tasks = []
global taskdirs
taskdirs = []
global videoformats
videoformats = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "mpg", "mpeg", "mts", "gif"]
global audioformats
audioformats = ["mp3", "wav", "flac", "ogg", "aac", "wma", "m4a"]
global imageformats
imageformats = ["jpg", "jpeg", "jfif", "gif", "png", "bmp", "tiff", "tif", "heic", "webp"]

window = tk.Tk()
#make the window size 50% screen resolution
window.geometry("%dx%d+%d+%d" % (window.winfo_screenwidth()/2, window.winfo_screenheight()/2, window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
#maximize the window
#window.state('zoomed')
window.title("PizzaSoft Media Converter v22.0.1")
#set icon to icon.png
try:
    img = tk.Image("photo", file="./assets/icon.png")
    window.iconphoto(False, img)
except:
    pass

style = ttk.Style()
styles = style.theme_names()
menu = tk.Menu(window)

fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

tasksMenu = tk.Menu(menu, tearoff=0)
tasksMenu.add_command(label="Run All Tasks", state="disabled")
tasksMenu.add_command(label="Cancel All Tasks", state="disabled")
tasksMenu.add_command(label="Remove All Tasks", state="disabled")

themesSub = tk.Menu(tasksMenu, tearoff=0)
#add all available themes to the themes submenu
for theme in styles:
    themesSub.add_command(label=theme, command=lambda theme=theme: style.theme_use(theme))

viewMenu = tk.Menu(menu, tearoff=0)
viewMenu.add_cascade(label="Theme", menu=themesSub)

editMenu = tk.Menu(menu, tearoff=0)
editMenu.add_command(label="Preferences")

window.config(menu=menu)
menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit", menu=editMenu)
menu.add_cascade(label="Tasks", menu=tasksMenu)
menu.add_cascade(label="View", menu=viewMenu)
menu.add("command", label="Help", command=lambda: os.startfile("https://pizzasoft.us/helpcenter/"))

#make a frame for the buttons at the top
buttons = tk.Frame(window)
buttons.pack(side="top", fill="x")

def import_file():
    #open a file dialog and get the file
    file = tkfd.askopenfilename(filetypes=[("Video Files", videoformats), ("Audio Files", audioformats), ("Image Files", imageformats)])
    #if the file is not empty, add it to the list
    tasks.append(file)
    return file

def add_directory():
    #open a file dialog and get the file
    directory = tkfd.askdirectory()
    #if the file is not empty, add it to the list
    taskdirs.append(directory)

def add_task():
    file = import_file()
    if file == "":
        return
    
    #make a popup window to get info like the output file name and the conversion format
    popup = tk.Toplevel(window)
    popup.geometry("500x300")
    #add the icon to the popup
    try:
        img = tk.Image("photo", file="./assets/icon.png")
        window.iconphoto(False, img)
    except:
        pass
    popup.title("Add Task")
    
    pathchooser_frame = tk.Frame(popup)
    pathchooser_frame.pack(side="top", fill="x")
    
    pathchooser = ttk.Button(pathchooser_frame, text="Choose File", command=add_directory)
    pathchooser.pack(side="left")
    
    pathchooser_label = ttk.Label(pathchooser_frame, text="No file chosen")
    pathchooser_label.pack(side="left")
    
    pathchooser.bind("<Button-1>", lambda event: pathchooser_label.config(text=taskdirs))

#make the buttons
importButton = ttk.Button(buttons, text="Import", command=add_task)

rat = ttk.Button(buttons, text="Run All Tasks", state="disabled") #you can tell who made this variable name (it was me, lewolfyt)
cat = ttk.Button(buttons, text="Cancel All Tasks", state="disabled")
rmat = ttk.Button(buttons, text="Remove All Tasks", state="disabled")

importButton.pack(side="left")
rat.pack(side="left")
cat.pack(side="left")
rmat.pack(side="left")

#make the task list frame
tasklframe = tk.Frame(window)
tasklframe.pack(side="top", fill="both", expand=True)

#the task list will be a table
tasklist = ttk.Treeview(tasklframe, columns=("File", "Status", "Conversion Type", "Output file"), show="headings")
tasklist.heading("File", text="File")
tasklist.heading("Status", text="Status")
tasklist.heading("Conversion Type", text="Conversion Type")
tasklist.heading("Output file", text="Output file")
tasklist.pack(side="top", fill="both", expand=True)

window.mainloop()
