import sys
import pathlib
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Style
from directory_visualizer import visualize_tree, FOLDER_COLOR

def get_path_from_dialog() -> str:
    """Створює діалогове вікно для вибору директорії."""
    root = tk.Tk()
    root.withdraw()  # Ховаємо основне вікно tkinter
    root.attributes('-topmost', True)  # Виводимо вікно поверх інших
    
    # Відкриваємо діалог вибору папки
    selected_path = filedialog.askdirectory(title="Оберіть директорію для візуалізації")
    
    root.destroy()  # Закриваємо вікно після вибору
    return selected_path

def main() -> None:
    init(autoreset=True)

    # Якщо шлях не передано через термінал, відкриваємо діалогове вікно
    if len(sys.argv) < 2:
        path_str = get_path_from_dialog()
        if not path_str:  # Якщо користувач натиснув "Скасувати"
            print(f"{Fore.YELLOW}Вибір скасовано користувачем.{Style.RESET_ALL}")
            return
    else:
        path_str = sys.argv[1]

    target_path = pathlib.Path(path_str)

    if not target_path.exists() or not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Директорію не знайдено за шляхом: {target_path}{Style.RESET_ALL}")
        return
    
    print(f"\n{FOLDER_COLOR}{target_path.name}/{Style.RESET_ALL}")
    visualize_tree(target_path, indent="    ")

if __name__ == "__main__":
    main()
