
def get_cats_info(path):
    cats_info = [] #створемо список для інф про котів
    try:
        with open(path, 'r', encoding= 'utf-8') as file: #відкриєм файл для читання
            for line in file: #пройдемось по кожному рядку у нашому файлі
                cat_data = line.strip().split(',') # розділем рядок на окремі поля з комою
                if len(cat_data) == 3: #перевіримо чи є всі поля для кожного кота                    
                    cat_info = { #створимословник для інф про кота(ід,імя, вік)
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat_info) #жодаємо інф про кота до списку
                else:
                    print(f"Неправильний формат даних у рядку", line) #виводимо інф про неправильний формат даних
    except FileNotFoundError: #якщо файл не знайдний
        print("Файл не знайдено.")
    except Exception as e:
        print("Виникал помилка:", str(e))# інші помилки
    return cats_info # вертаєм список словників з інф про котків

cats_info = get_cats_info("C:\\Users\\liljo\\OneDrive\\Documents\\My_repos\\First_repo\\Homework\\hw_module_3\\with_cats_file.txt")#викликаємо ф-цію

print(cats_info)