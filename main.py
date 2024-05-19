def writeFile(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def digitalRoot(numbers):
    numbersArr = [int(num) for num in numbers]
    n = sum(numbersArr) 

    if n < 10:
        return n
    
    return digitalRoot(str(n))



def main():
    roots = []

    with open('digital.txt', 'r') as file:
        numbers = file.readlines()
    
    for num in numbers:
        if num == "0":
            break

        num = num.strip()
        root = str(digitalRoot(num))
        print(root)

        roots.append(root)
    
    writeFile('output.txt', roots)



if __name__ == "__main__":
    main()