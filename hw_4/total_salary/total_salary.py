import math
from pathlib import Path
import re

def total_salary(path):
    total = 0
    average = 0
    lines_len = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                pattern = r"\w+\,+\d+"
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    lines_len = lines_len + 1 # Буде рахувати тільки ті строки, що пройшли перевірку
                    total = total + int(line.split(',')[1])
                    average = math.ceil(total / lines_len)
            return total, average

    except FileNotFoundError:
        print("Не вдалося знайти файл.")
        return total, average

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")