from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r' , encoding='utf-8') as file:
            for line in file:
                uuid, name, age = line.split(',')
                formatted_age = None
                try:
                    formatted_age = int(age)
                except ValueError:
                    print(f"{age} is not a number")
                cats_info.append({
                    'id': uuid,
                    'name': name,
                    'age': formatted_age
                })
    except FileNotFoundError:
        print("File not found")
        return []

    return cats_info

if __name__ == "__main__":

    file_name = Path(__file__).parent / 'cats.txt'

    result = get_cats_info(file_name)

    print(result)