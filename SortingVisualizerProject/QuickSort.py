from random import randint
import time

'''
def quick_sort(data, draw_data, wait_time):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(data) < 2:
        return data

    low, same, high = [], [], []

    pivot = data[randint(0, len(data) - 1)]  # Select your `pivot` element randomly
    draw_data(data, ['crimson' if _ == pivot else 'deep sky blue' for _ in range(len(data))])
    time.sleep(wait_time)
    for item in data:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
            draw_data(data, ['yellow' if low else 'deep sky blue' for _ in range(len(data))])

        elif item == pivot:
            same.append(item)
            draw_data(data, ['crimson' if same else 'deep sky blue' for _ in range(len(data))])

        elif item > pivot:
            high.append(item)
            draw_data(data, ['black' if high else 'deep sky blue' for _ in range(len(data))])

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    quick_sort(low, draw_data, wait_time) + same + quick_sort(high, draw_data, wait_time)
    return data
'''


def partition(data, head, tail, draw_data, wait_time):
    border = head
    pivot = data[tail]

    draw_data(data, get_color_arr(len(data), head, tail, border, border))
    time.sleep(wait_time)

    for j in range(head, tail):
        if data[j] < pivot:
            # draw
            draw_data(data, get_color_arr(len(data), head, tail, border, j, True))
            time.sleep(wait_time)

            data[border], data[j] = data[j], data[border]
            border += 1
        # draw
        draw_data(data, get_color_arr(len(data), head, tail, border, j, True))
        time.sleep(wait_time)

        # swapping pivot with border value.
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, draw_data, wait_time):
    if head < tail:
        partition_index = partition(data, head, tail, draw_data, wait_time)

        # Left Partition
        quick_sort(data, head, partition_index - 1, draw_data, wait_time)
        # Right Partition
        quick_sort(data, partition_index + 1, tail, draw_data, wait_time)


def get_color_arr(data_length, head, tail, border, current_index, is_swapping=False):
    color_array = []
    # base color
    for i in range(data_length):
        if head <= i <= tail:
            color_array.append('deep sky blue')
        else:
            color_array.append('gainsboro')

        if i == tail:
            color_array[i] = 'light coral'
        elif i == border:
            color_array[i] = 'crimson'
        elif i == current_index:
            color_array[i] = 'deep sky blue'

        if is_swapping:
            if i == border or i == current_index:
                color_array[i] = 'yellow'

    return color_array






