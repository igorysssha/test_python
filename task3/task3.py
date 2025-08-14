
import json
import sys

def main():
    if len(sys.argv) != 4:
        print("Надо три файла: 1)values, 2)tests, 3)report")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Загрузка данных из файлов
    values = load_json(values_file)
    tests = load_json(tests_file)

    # преобразуем в словарь {id: value}, а tests.json может быть {"tests": [...]}
    if isinstance(values, dict) and 'values' in values and isinstance(values['values'], list):
        values = {item['id']: item['value'] for item in values['values']}

    if isinstance(tests, dict) and 'tests' in tests and isinstance(tests['tests'], list):
        tests = tests['tests']

    # Обновление значений в тестах
    update_tests_values(tests, values)

    # Сохранение обновленной структуры в файл report.json
    with open(report_file, 'w') as file:
        json.dump(tests, file, indent=4)

    print("Файл report.json успешно создан.")

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Неверный формат JSON в файле {file_path}.")
        sys.exit(1)

def update_tests_values(tests, values):
    for test in tests:
        if isinstance(test, dict) and 'id' in test:
            test_id = test['id']
            if isinstance(test_id, int) and test_id in values:
                test['value'] = values[test_id]
        if isinstance(test, dict) and 'values' in test:
            update_tests_values(test['values'], values)

if __name__ == "__main__":
    main()