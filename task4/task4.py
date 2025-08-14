import sys

# чтобы привести все числа к одному (ход = +1 или -1 к любому числу).

def load_nums(file_path):
    try:
        with open(file_path, 'r') as file:
            nums = [int(num) for num in file.read().split()]
            return nums
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except ValueError:
        print(f"Неверный формат данных в файле {file_path}. Ожидались целые числа.")
        sys.exit(1)

def min_moves_to_equal(nums):
    # Чтобы привести все числа к одному, минимальное суммарное отклонение даёт медиана
    median = sorted(nums)[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves

def main():
    if len(sys.argv) != 2:
        print("Использование: python3 task4/task4.py task4/nums.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = load_nums(file_path)

    moves = min_moves_to_equal(nums)

    print(f"Минимальное количество ходов: {moves}")

if __name__ == "__main__":
    main()