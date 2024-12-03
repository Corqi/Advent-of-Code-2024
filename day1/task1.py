import numpy as np

if __name__ == "__main__":
    file = open ('input_task1.txt', 'r')

    array1 = []
    array2 = []
    for line in file:
        array1.append(int(line.split("   ")[0]))
        array2.append(int(line.split("   ")[1]))
    
    array1.sort()
    array2.sort()

    combinedArray = np.subtract(array2, array1)
    combinedArray = np.abs(combinedArray)
    output = sum(combinedArray)
    print(output)
    file.close()