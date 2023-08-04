from tkinter import *
from tkinter import ttk
from random import shuffle
import BubbleSort as Bubble
import MergeSort as Merge
import QuickSort as Quick

# Initialize the main application window
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 800)
root.config(bg='lightsteelblue')

# Global variables
selected_alg = StringVar()
data = []

# Function to draw the data on the canvas
def draw_data(data_list, color_arr):
    canvas.delete("all")
    c_height = 380
    c_width = 800
    x_width = c_width / (len(data_list) + 1)
    offset = 10
    spacing = 10
    normalize_data = [i / max(data_list) for i in data_list]
    for i, height in enumerate(normalize_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_arr[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data_list[i]))
    root.update_idletasks()

# Function to generate random data
def generate():
    global data
    data = []
    numb_entered = int(sizeEntry.get())
    data = [i + 1 for i in range(int(numb_entered))]
    shuffle(data)
    draw_data(data, ['deep sky blue' for _ in range(len(data))])

# Function to run the sorting algorithm
def run():
    global data
    if not data:
        return

    # Sort using Quick sort
    if algMenu.get() == 'Quick Sort':
        Quick.quick_sort(data, 0, len(data) - 1, draw_data, get_speed())

    # Sort using Bubble sort
    elif algMenu.get() == 'Bubble Sort':
        Bubble.bubble_sort(data, draw_data, get_speed())

    # Sort using Merge sort
    elif algMenu.get() == 'Merge Sort':
        Merge.merge_sort(data, draw_data, get_speed())

    draw_data(data, ['lime' for x in range(len(data))])

# Function to get the selected speed as a numeric value
def get_speed():
    speed_option = speed_scale.get()
    if speed_option == 'Slow':
        return 0.5  # Adjust this value as needed for slower speed
    elif speed_option == 'Medium':
        return 0.2  # Adjust this value as needed for medium speed
    elif speed_option == 'Fast':
        return 0.1  # Adjust this value as needed for faster speed

    return 0.1  # Default speed value if none of the options match

# Frame/Base layout
UI_frame = Frame(root, width=800, height=100, bg='lightsteelblue')
UI_frame.grid(row=0, column=0, padx=50, pady=10)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=50, pady=10)

# User Interface Area
Label(UI_frame, text="Step 1: Choose Algorithm", bg='lightsteelblue').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'], state='readonly')
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Label(UI_frame, text="Step 2: Generate Data", bg='lightsteelblue').grid(row=0, column=2, padx=5, pady=5)
sizeEntry = Scale(UI_frame, from_=3, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=0, column=3, padx=5, pady=5)
Button(UI_frame, text="Generate Data", command=generate, bg='slategrey', fg='white', padx=10).grid(row=0, column=4, padx=5, pady=5)

# Separate row for Step 3
Label(UI_frame, text="Step 3: Run Algorithm", bg='lightsteelblue').grid(row=1, column=0, columnspan=2, padx=5, pady=5)
speed_scale = ttk.Combobox(UI_frame, values=['Slow', 'Medium', 'Fast'], state='readonly', width=10)
speed_scale.grid(row=1, column=2, padx=5, pady=5)
speed_scale.current(2)

Button(UI_frame, text="Run Algorithm", command=run, bg='slategrey', fg='white', padx=10).grid(row=1, column=4, padx=5, pady=5)

root.mainloop()
