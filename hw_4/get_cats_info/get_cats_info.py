import re

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                pattern = r"\w+\,+\w+\,+\d"
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    l = line.split(',')
                    one_cat_info = {'id' : l[0], 'name' : l[1], 'age' : l[2].removesuffix('\n')}
                    cats_info.append(one_cat_info)
                    
            return cats_info

    except FileNotFoundError:
        print("Не вдалося знайти файл.")
        return cats_info

    

cats_info = get_cats_info("cats_info.txt")
print(cats_info)