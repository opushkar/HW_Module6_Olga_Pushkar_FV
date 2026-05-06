import os
from modules.salary_logic import total_salary

def main():
    # Використовуємо відносний шлях
    file_path = os.path.join("data", "salaries.txt")
    
    total, average = total_salary(file_path)
    
    if total > 0:
        print(f"Загальна сума: {total}, Середня: {average}")
    else:
        print("Дані не знайдено або файл пошкоджено.")

if __name__ == "__main__":
    main()
