def bubbleSort(array):
    sorted = False
    while(not sorted):
        sorted = True
        for x in range(len(array)):
            j = x - 1;
            if j >=0 and array[j] > array[x]:
                swap(array, j, x)
                sorted = False
            print(array)
                
def swap(array, fromIndex, toIndex):
    temp = array[toIndex]
    array[toIndex] = array[fromIndex]
    array[fromIndex] = temp

def inersertionSort(array):
    for x in range(1, len(array)):
        curVal = array[x]
        index = x
        while(index > 0 and array[index-1] > curVal):
            array[index] = array[index -1]
            index = index - 1
        array[index] = curVal
        print(array)

def selectionSort(array):
    for slotToFill in range(len(array)-1,0,-1):
        maxIndex = 0
        for index in range(1, slotToFill +1):
            if array[index] > array[maxIndex]:
                maxIndex = index
        swap(array, maxIndex, slotToFill)
        print(array)

        
    
        