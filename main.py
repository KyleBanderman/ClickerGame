import tkinter as tk
from PIL import Image, ImageTk
import sys
from upgrades import UpgradeModel
from errorModels import *

def close_window():
    try:
        save_data(*gather_data())
    except:
        with open("error.txt", "a") as file:
            file.write("----------\n")
            file.write("Save Data failed to gather\n")
    else:
        root.quit()
        sys.exit()
    finally:
        with open("error.txt", "a") as file:
            file.write("Game failed to close. Check previous errors\n")
            file.write("----------\n")

def increment_counter():
    global clicker_counter
    clicker_counter += 1
    if clicker_counter < 1000000:
        counter_label.configure(text = clicker_counter)
    else:#TODO:replace this format with the cookie clicker format, i.e 1.456a, 2.679b
        counter_label.configure(text = format(clicker_counter, 'e'))

def open_settings():
    test = "test"

def on_mousewheel(event):
    canvas.yview_scroll(-1*event.delta//120, "units")

def read_data_startup():
    with open("save.txt", "r+") as file:
        save_data = file.readlines()
        return save_data

def save_data(current_counter, current_upgrades):
    #writes the save data into save.txt
    with open("save.txt", "w+") as file:
        for line in input_data:
            file.write(line)

def gather_data():
    #will gather the data needed to save the game
    return clicker_counter, upgrade_list

#global variable to store the upgrades
global upgrade_list
upgrade_list = read_data_startup()

#create fullscreen root without top bar
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.attributes('-fullscreen', True)
root.configure(bg="#D4D4D4")

#create and position frames
name_frame = tk.Frame(root, width=screen_width / 2 - 10, height=40, bg="red")
name_frame.grid_rowconfigure(0, weight=1)
name_frame.grid_columnconfigure(0, weight=1)
name_frame.grid_propagate(False)
name_frame.grid(row=0, column=0, pady=(10, 10), padx=(10, 3))

counter_frame = tk.Frame(root, width=screen_width / 2 - 10, height=40, bg="orange")
counter_frame.grid_rowconfigure(0, weight=1)
counter_frame.grid_columnconfigure(0, weight=1)
counter_frame.grid_propagate(False)
counter_frame.grid(row=1, column=0, pady=(10,10), padx=(10,3))

clicker_frame = tk.Frame(root, width=screen_width / 2 - 10, height = screen_height - 145, bg="yellow")
clicker_frame.grid_rowconfigure(0, weight=1)
clicker_frame.grid_columnconfigure(0, weight=1)
clicker_frame.grid_propagate(False)
clicker_frame.grid(row=2, column=0, pady=(10,10), padx=(10,3))

settings_frame = tk.Frame(root, width=screen_width / 2 - 10, height=40, bg="green")
settings_frame.grid_rowconfigure(0, weight=1)
settings_frame.grid_columnconfigure(0, weight=1)
settings_frame.grid_propagate(False)
settings_frame.grid(row=0, column=1, pady=(10, 10), padx=(3, 10))

upgrade_frame = tk.Frame(root, width=screen_width / 2 - 10, height = screen_height - 80, bg="blue")
upgrade_frame.grid_rowconfigure(0, weight=1)
upgrade_frame.grid_columnconfigure(0, weight=1)
upgrade_frame.grid_propagate(False)
upgrade_frame.grid(row=1, rowspan=2, column=1, pady=(10,10), padx=(3, 10))

#load image for close window button
close_image = Image.open("close_window_image.png")
close_photo = ImageTk.PhotoImage(close_image)
#create the close window button
close_window_button = tk.Button(settings_frame, command=close_window, image=close_photo, height=30, width=30)
close_window_button.configure(bg="white", fg="blue")
close_window_button.grid(row=0, column=0, sticky="NE", padx=(5, 5), pady=(5,5))

#load image for settings button
settings_image = Image.open("settings_icon.jpg")
settings_photo = ImageTk.PhotoImage(settings_image)
#create the settings button
settings_button = tk.Button(settings_frame, command=open_settings, image=settings_photo, height=30, width=30)
settings_button.configure(bg="white", fg="blue")
settings_button.grid(row=0, column=0, sticky="NE", padx=(5, 40), pady=(5,5))

#create label for name of clicker run
name_label = tk.Label(name_frame, text="Welcome to Clicker Game", font=("Arial", 30), bg="#D4D4D4")
name_label.grid(row=0, sticky="NW")

#create counter and label
global clicker_counter
clicker_counter = 0
counter_label = tk.Label(counter_frame, text = clicker_counter, font=("Arial", 30), bg="#D4D4D4")
counter_label.grid(row=0, column=0)

counter_button = tk.Button(clicker_frame, command=increment_counter, text="Click", height=30, width=30, font=("Arial", 30))
counter_button.grid(row=0, column=0)

#create passive increment global for upgrades
global passive_increment
passive_increment = 0

#create scrollable frame
upgrade_canvas = tk.Canvas(upgrade_frame, height=100, bg="blue")
canvas_frame = tk.Frame(upgrade_canvas)
upgrade_scrollbar = tk.Scrollbar(upgrade_frame,orient="vertical", command=upgrade_canvas.yview)
upgrade_canvas.create_window((0,0), window=canvas_frame, anchor="nw")
canvas_frame.rowconfigure(0, weight=1)
canvas_frame.columnconfigure(1, weight=1)

#create upgrade buttons on startup
incremental_var = 0
for item in upgrade_list:
    button = tk.Button(canvas_frame, text=f"Upgrade {incremental_var+1}", command=save_data, height=5, width=105)
    button.grid(row=incremental_var, column=0, sticky="news")
    incremental_var += 1

#update the frame to reset the height
canvas_frame.update()
upgrade_canvas.configure(yscrollcommand=upgrade_scrollbar.set, scrollregion="0 0 0 %s" % canvas_frame.winfo_height())

upgrade_canvas.grid(row=0, column=0, sticky="news")
upgrade_scrollbar.grid(row=0, column=10, sticky="ns")
canvas_frame.bind("<MouseWheel>", on_mousewheel)

root.mainloop()