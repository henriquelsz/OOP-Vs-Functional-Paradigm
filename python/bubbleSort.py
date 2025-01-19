import time

def bubble_sort(list):
    l = len(list)
    for i in range(l):
        for j in range(l-i-1):
            if (list[j] > list[j+1]):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
            
    return list


if __name__ == "__main__":
    input = list(range(10000, 0, -1))
    start_time = time.time()
    sortedList = bubble_sort(input)
    end_time = time.time()
    print(f"Python Bubble Sort took {end_time - start_time:.4f} seconds")