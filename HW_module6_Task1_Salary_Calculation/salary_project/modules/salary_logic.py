from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    """
    Обчислює загальну та середню зарплату з файлу.
    """
    total: float = 0.0
    count: int = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_no, line in enumerate(file, 1):
                line = line.strip()
                if not line: continue
                
                parts = line.split(',')
                if len(parts) != 2:
                    print(f"L{line_no}: Помилка формату.")
                    continue
                
                name, sal_str = parts[0].strip(), parts[1].strip()

                # Валідація: ім'я не пусте і не цифри, ЗП не пуста
                if not name or name.isdigit() or not sal_str:
                    print(f"L{line_no}: Некоректні дані (ім'я або ЗП).")
                    continue

                try:
                    total += float(sal_str)
                    count += 1
                except ValueError:
                    print(f"L{line_no}: Зарплата має бути числом.")
        
        return (total, total / count) if count > 0 else (0.0, 0.0)

    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено.")
        return 0.0, 0.0
