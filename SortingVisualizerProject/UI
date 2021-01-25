from tkinter import *
from tkinter import ttk

from random import shuffle

import BubbleSort as Bubble
import MergeSort as Merge
import QuickSort as Quick

# size + background color
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(900, 800)
root.config(bg='lightsteelblue')

# variables
selected_alg = StringVar()
data = []


def draw_data(data_list, color_arr):
    # Clears canvas
    canvas.delete("all")
    c_height = 380
    c_width = 800
    x_width = c_width / (len(data_list) + 1)
    offset = 10
    spacing = 10
    normalize_data = [i / max(data_list) for i in data_list]
    for i, height in enumerate(normalize_data):
        # top left corner
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right corner
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_arr[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data_list[i]))
    root.update_idletasks()


def generate():
    # Access global data array
    global data
    # reset the global data array
    data = []
    # Take in the number selected by the user and shuffle that many numbers
    numb_entered = int(sizeEntry.get())
    data = [i + 1 for i in range(int(numb_entered))]
    shuffle(data)
    # Draw the data & color it
    draw_data(data, ['deep sky blue' for _ in range(len(data))])


# Takes the generated data then begins to sort it.
def run():
    # Access global data array
    global data
    if not data: return

    # Sort using Quick sort
    if algMenu.get() == 'Quick Sort':
        Quick.quick_sort(data, 0, len(data) - 1, draw_data, speed_scale.get())

    # Sort using Bubble sort
    elif algMenu.get() == 'Bubble Sort':
        Bubble.bubble_sort(data, draw_data, speed_scale.get())

    # Sort using Merge sort
    elif algMenu.get() == 'Merge Sort':
        Merge.merge_sort(data, draw_data, speed_scale.get())

    # Color the sorted dataset
    draw_data(data, ['lime' for x in range(len(data))])


# Frame/Base layout -------------------------------------------------------------------------------------------------

UI_frame = Frame(root, width=800, height=100, bg='lightsteelblue')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area -------------------------------------------------------------------------------------------------

# Row[0]
# Algorithm Menu
Label(UI_frame, text="Algorithm: ", bg='white smoke').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
# Size of Array to generate
sizeEntry = Scale(UI_frame, from_=3, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=0, column=2, padx=5, pady=5)
# Generate button
Button(UI_frame, text="Generate Data", command=generate, bg='slategrey').grid(row=0, column=3, padx=5, pady=5)

# Row[1]
# Speed scale
speed_scale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL,
                    label="Select Speed [s]")
speed_scale.grid(row=1, column=2, padx=5, pady=5)
# Start algorithm button
Button(UI_frame, text="Run Algorithm", command=run, bg='slategrey').grid(row=1, column=3, padx=5, pady=5, sticky=E)

root.mainloop()
