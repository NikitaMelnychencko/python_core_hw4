from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r' , encoding='utf-8') as file:
            #line_count = sum(1 for line in file) (good way)
            for line in file:
                name, salary = line.split(',')
                try:
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"{salary} is not a number")
    except FileNotFoundError:
        print("File not found")
        return (0, 0)

    return (total, total/count)


if __name__ == "__main__":

    file_name = Path(__file__).parent / 'sallary.txt'

    result = total_salary(file_name)

    print("Total salary:", result[0])
    print("Average salary:", result[1])
