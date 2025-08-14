import sys


def main():
    # Для запуска нужны два файла
    if len(sys.argv) != 3:
        print("Использование: python3 task2/task2.py task2/circle.txt task2/points.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Читаем файл с центром и радиусом
    try:
        with open(circle_file, 'r') as f:
            lines = f.readlines()
            x_center, y_center = map(float, lines[0].split())
            radius = float(lines[1])
    except FileNotFoundError:
        print("Файл с координатами и радиусом окружности не найден.")
        sys.exit(1)
    except ValueError:
        print("Неверный формат данных в файле с координатами и радиусом окружности.")
        sys.exit(1)

    # Читаем файл с точками
    points = []
    try:
        with open(points_file, 'r') as f:
            for line in f:
                x, y = map(float, line.split())
                points.append((x, y))
    except FileNotFoundError:
        print("Файл с координатами точек не найден.")
        sys.exit(1)
    except ValueError:
        print("Неверный формат данных в файле с координатами точек.")
        sys.exit(1)

    # 0 — точка лежит на окружности, 1 — точка внутри окружности, 2 — точка снаружи окружности
    for p in points:
        x_point, y_point = p
        distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
        if distance_squared == radius ** 2:
            print(0)
        elif distance_squared < radius ** 2:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()