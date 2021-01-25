import time


def merge_sort(data, draw_data, wait_time):
    # calls the Merge alg
    merge_alg(data, 0, len(data)-1, draw_data, wait_time)


def merge_alg(data, left, right, draw_data, wait_time):
    # Sort the array by recursively splitting the input into two
    # equal halves, sorting each half and merging them together.
    if left < right:
        midpoint = (left + right) // 2
        merge_alg(data, left, midpoint, draw_data, wait_time)
        merge_alg(data, midpoint+1, right, draw_data, wait_time)
        merge_func(data, left, midpoint, right, draw_data, wait_time)


def merge_func(data, left, midpoint, right, draw_data, wait_time):

    left_part = data[left:midpoint+1]
    right_part = data[midpoint+1: right+1]
    index_left = index_right = 0

    for dataIdx in range(left, right + 1):
        if index_left < len(left_part) and index_right < len(right_part):
            if left_part[index_left] <= right_part[index_right]:
                data[dataIdx] = left_part[index_left]
                index_left += 1
            else:
                data[dataIdx] = right_part[index_right]
                index_right += 1

        elif index_left < len(left_part):
            data[dataIdx] = left_part[index_left]
            index_left += 1
        else:
            data[dataIdx] = right_part[index_right]
            index_right += 1

    draw_data(data, ["deep sky blue" if left <= x <= right else "crimson" for x in range(len(data))])
    time.sleep(wait_time)

