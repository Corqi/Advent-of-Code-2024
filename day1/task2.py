from collections import Counter

if __name__ == "__main__":
    file = open ('input_task1.txt', 'r')

    array1 = []
    array2 = []
    for line in file:
        array1.append(int(line.split("   ")[0]))
        array2.append(int(line.split("   ")[1]))
    
    dict = Counter(array2)
    
    output = 0
    for num in array1:
        output += num * dict[num]

    print(output)
    file.close()