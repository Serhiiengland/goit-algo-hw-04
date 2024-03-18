
def total_salary(path): #створюємо ф-цію
    try:        
        with open(path, 'r', encoding='utf-8') as file: # Відкриваємо файл за вказаним шляхом і використовуєм кодування utf-8
            total_salary = 0  # робимо змінні для обчислення загальної з/п та кількості розробників
            num_developers = 0            
            for line in file: # проходим через кожен рядок у файлі                
                developer_info = line.strip().split(',') # Розділяєм рядки за комою
                if len(developer_info) == 2:
                    salary = int(developer_info[1]) # отримуємо з/п розробника і додаємо до загальної з/п
                    total_salary += salary
                    num_developers += 1
            
            if num_developers == 0: # середня з/п
                return 0, 0  # Повертаємо 0,0, якщо в файлі немає ніякої інф про з/п
            average_salary = total_salary / num_developers           
            return total_salary, average_salary # Повертаємо результат у вигляді кортежу зі значеннями загальної суми та середньої з/п

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None  # Повертаємо None,None якщо файл не знайдено
    except ValueError:
        print("Некоректні дані в файлі.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None  # Повертаємо None,і None у разі, якщо сталася будь-яка друга помилка
    

total, average = total_salary("C:\\Users\\liljo\\OneDrive\\Documents\\My_repos\\First_repo\\Homework\\hw_module_3\\salary_file.txt") # запускаємо ф-цію:
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#else:
   #print("Не вдалося обчислити загальну та середню зарплату.")