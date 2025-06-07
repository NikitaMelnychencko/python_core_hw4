from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r' , encoding='utf-8') as file:
        #line_count = sum(1 for line in file) (good way)
        for line in file:
            name, salary = line.split(',')
            count += 1
            try:
                total += int(salary)
            except ValueError:
                print(f"{salary} is not a number")

    return (total, total/count)

file_name = Path(__file__).parent / 'sallary.txt'

result = total_salary(file_name)

print("Total salary:", result[0])
print("Average salary:", result[1])
