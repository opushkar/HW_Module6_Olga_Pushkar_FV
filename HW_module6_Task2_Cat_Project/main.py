from cat_processor import get_cats_info

def main():
    # Вказуємо шлях до нашого текстового файлу
    path = "cats_data.txt"
    
    # Отримуємо результат
    cats_info = get_cats_info(path)
    
    # Виводимо результат у консоль
    for cat in cats_info:
        print(cat)

if __name__ == "__main__":
    main()
