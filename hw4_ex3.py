import sys
from pathlib import Path
from colorama import init, Fore

#ініціалізуємо colorama для підтримки кольорів в консолі
init(autoreset=True)

def display_directory_structure(directory_path, indent=''):
    directory = Path(directory_path)
    if not directory.is_dir():
        print(Fore.RED + f"Шлях '{directory_path}' не є директорією або не існує.")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"{indent}📁 {item.name}")  #виводимо ім'я директорії з синім кольором
            display_directory_structure(item, indent + '    ')  #рекурсивно виводимо її структуру
        else:
            print(Fore.GREEN + f"{indent}📄 {item.name}")  #виводимо ім'я файлу з зеленим кольором

if __name__ == "__main__":
    #виведемо аргументи командного рядка для відлагодження
    #print("Аргументи командного рядка:", sys.argv)

    if len(sys.argv) != 2:
        print(Fore.RED + "Введіть лише один аргумент - шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)