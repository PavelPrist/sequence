def print_sequence(n):
    sequence = ""
    for i in range(1, n+1):
        sequence += str(i) * i
    print(sequence[:n])

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    print_sequence(n)