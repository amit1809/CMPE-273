import os
import time

OUTPUT_SORTED_FILE = "output/sorted.txt"


def sort(arr, filename):
    """
	This is Merge Sort implementation
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves
        sort(L, filename)  # Sorting the first half
        sort(R, filename)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    with open("output/temp/" + filename, "w") as file:
        for item in arr:
            file.write('%s\n' % item)


def mergeSortedToFile(arr):
    """
	This function to merge sorted list to final output sorted file.
    """
    # list the elements of sorted text file
    # print(arr)
    sortedFileList = []
    with open(OUTPUT_SORTED_FILE) as file:
        for line in file:
            line = int(line.strip())
            sortedFileList.append(line)
    l1 = len(arr)
    l2 = len(sortedFileList)
    l3 = l1 + l2
    m = 0
    i = 0
    j = 0
    out2 = [0] * l3
    while (i < l1 and j < l2):
        if (arr[i] < sortedFileList[j]):
            out2[m] = arr[i]
            m += 1
            i += 1
        else:
            out2[m] = sortedFileList[j]
            m += 1
            j += 1
    while (i < l1):
        out2[m] = arr[i]
        m += 1
        i += 1
    while (j < l2):
        out2[m] = sortedFileList[j]
        m += 1
        j += 1
    # writing merged sorted output list to tht output file
    with open(OUTPUT_SORTED_FILE, "w") as file:
        for item in out2:
            file.write('%s\n' % item)


def mergeAllSortedFiles():
    """
	This function to make list of all temp sorted files and call mergeSortedToFile()
	to merge it to final sorted file.
    """
    entries = os.listdir('output/Temp/input')
    for entry in entries:
        arr = []
        with open("output/Temp/input/" + entry) as file:
            for line in file:
                line = int(line.strip())
                arr.append(line)
        mergeSortedToFile(arr)


def sortFile(filename):
    inpList = []
    with open(filename) as file:
        for line in file:
            line = int(line.strip())
            inpList.append(line)
    sort(inpList, filename)
    time.sleep(0.1)


def main():
    # Cleaning out content of the final output file before start.
    open(OUTPUT_SORTED_FILE, "w").close()
    sortFile("input/unsorted_1.txt")
    sortFile("input/unsorted_2.txt")
    sortFile("input/unsorted_3.txt")
    sortFile("input/unsorted_4.txt")
    sortFile("input/unsorted_5.txt")
    sortFile("input/unsorted_6.txt")
    sortFile("input/unsorted_7.txt")
    sortFile("input/unsorted_8.txt")
    sortFile("input/unsorted_9.txt")
    sortFile("input/unsorted_10.txt")
    mergeAllSortedFiles()


if __name__ == '__main__':
    main()
