import os


def count_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return len(files)
    except:
        return 0


def read_txt(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    row = {
                        '№': int(parts[0]),
                        'наименование блюда': parts[1],
                        'время размещения заказа': parts[2],
                        'время приготовления': int(parts[3]),
                        'отзыв': parts[4]
                    }
                    data.append(row)
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='cp1251') as file:
            lines = file.readlines()[1:]
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 5:
                    row = {
                        '№': int(parts[0]),
                        'наименование блюда': parts[1],
                        'время размещения заказа': parts[2],
                        'время приготовления': int(parts[3]),
                        'отзыв': parts[4]
                    }
                    data.append(row)
    return data


def save_txt(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('№,наименование блюда,время размещения заказа,время приготовления,отзыв\n')
        for row in data:
            file.write(
                f"{row['№']},{row['наименование блюда']},{row['время размещения заказа']},{row['время приготовления']},{row['отзыв']}\n")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("Текущая директория:", current_dir)
    print("Файлов:", count_files(current_dir))

    data = read_txt("data.txt")

    if data:
        print("\nПо названию:")
        for item in sorted(data, key=lambda x: x['наименование блюда']):
            print(f"{item['наименование блюда']} - заказ в {item['время размещения заказа']}")

        print("\nПо времени приготовления:")
        for item in sorted(data, key=lambda x: x['время приготовления']):
            print(
                f"{item['наименование блюда']} - {item['время приготовления']} мин, заказ в {item['время размещения заказа']}")

        print("\nВремя приготовления > 30 мин:")
        for item in data:
            if item['время приготовления'] > 30:
                print(
                    f"{item['наименование блюда']} - {item['время приготовления']} мин, заказ в {item['время размещения заказа']}")

        save_txt(data, "data_new.txt")
        print("\nСохранено в data_new.txt")
    else:
        print("Файл data.txt не найден или пуст")


if __name__ == "__main__":
    main()