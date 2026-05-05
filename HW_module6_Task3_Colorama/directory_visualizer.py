import pathlib
from colorama import init, Style

# Инициализация colorama для корректной работы ANSI в терминале
init(autoreset=True)

# Константы цветов RGB (используем TrueColor ANSI)
FOLDER_COLOR = "\033[38;2;110;163;248m"  # RGB(110, 163, 248)
FILE_COLOR = "\033[38;2;185;237;149m"    # RGB(185, 237, 149)

def visualize_tree(path: pathlib.Path, indent: str = "") -> None:
    """
    Рекурсивно визуализирует структуру директории.
    Папки: Синие (110, 163, 248) + '/'
    Файлы: Зеленые (185, 237, 149)
    """
    try:
        # Сортировка: папки вверху, файлы внизу
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        return

    for item in items:
        if item.is_dir():
            # Печать папки с отступом и слешем
            print(f"{indent}{FOLDER_COLOR}{item.name}/{Style.RESET_ALL}")
            # Рекурсивный вызов для вложенных элементов (+ 4 пробела)
            visualize_tree(item, indent + "    ")
        else:
            # Печать файла с отступом
            print(f"{indent}{FILE_COLOR}{item.name}{Style.RESET_ALL}")
