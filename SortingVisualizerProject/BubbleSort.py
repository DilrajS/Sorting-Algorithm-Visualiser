import time


def bubble_sort(data, draw_data, wait_time):
    length_of_array = len(data)
    # Goes through all the elements in the array
    for i in range(length_of_array):
        for j in range(0, length_of_array - i - 1):
            # Swaps if the next element is smaller.
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['crimson' if x == j or x == j + 1 else 'deep sky blue' for x in range(len(data))])
                time.sleep(wait_time)
    draw_data(data, ['lime' for i in range(len(data))])
    return data
