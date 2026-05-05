import os
from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Читає файл про котів з повною валідацією даних та перевіркою файлу.
    """
    cats_list: List[Dict[str, str]] = []
    
    # 1. Перевірка, чи файл існує
    if not os.path.exists(path):
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []

    # 2. Перевірка, чи файл не пустий
    if os.path.getsize(path) == 0:
        print(f"Помилка: Файл '{path}' порожній.")
        return []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Рядок {line_num}: Помилка формату (очікується 3 значення).")
                    continue
                
                cat_id, name, age_str = parts
                
                # Валідація ID (24 символи)
                if len(cat_id) != 24:
                    print(f"Рядок {line_num}: Некоректний ID (має бути 24 символи).")
                    continue
                
                # Валідація віку (число від 0 до 55)
                try:
                    age_int = int(age_str)
                    if not (0 <= age_int <= 55):
                        print(f"Рядок {line_num}: Некоректний вік {age_int} (дозволено 0-55).")
                        continue
                except ValueError:
                    print(f"Рядок {line_num}: Вік '{age_str}' не є числом.")
                    continue
                
                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": str(age_int)
                })
                
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        
    return cats_list
