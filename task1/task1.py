import sys

def main():
    if len(sys.argv) != 3:
        print("Для запуска вводим только два аргумента")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    # Начальную длину массива получаем из m
    base = []
    for i in range(1, n + 1):
        base.append(i)
    arrays = []
    start = 0

    while True:
        # Тут я создаю массив, чтобы его длина равнялась числу m
        array = []
        for i in range(m):
            num = start + i
            while num >= n:
                num -= n
            array.append(base[num])
        
        arrays.append(array)
        
        # Каждый раз смотрим последний элемент массива
        last_element = array[-1]  # или array[m-1]
        
        # Как только он равен 1, сразу стоп
        if last_element == 1:
            break
        
        # Затем следующий массив, начинается с последнего элемента предыдущего
        next_start = start + m - 1
        while next_start >= n:
            next_start -= n
        start = next_start

    # Собираем результат из первых элементов массивов
    result = ""
    for i in range(len(arrays)):
        result += str(arrays[i][0])
    
    print(result)

if __name__ == "__main__":
    main()