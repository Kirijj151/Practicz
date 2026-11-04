import copy

students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

def avg(s):
    return sum(s["scores"]) / len(s["scores"])

original_order = [s["name"] for s in students]

by_age = sorted(students, key=lambda s: s["age"])
print("По возрасту:", [(s["name"], s["age"]) for s in by_age])

by_name = sorted(students, key=lambda s: s["name"])
print("По имени:", [s["name"] for s in by_name])

by_avg = sorted(students, key=lambda s: avg(s), reverse=True)
print("По средней оценке (убыв.):", [(s["name"], round(avg(s), 1)) for s in by_avg])

by_group_age = sorted(students, key=lambda s: (s["group"], s["age"]))
print("По группе и возрасту:",
      [(s["group"], s["name"], s["age"]) for s in by_group_age])

print("\n-- sorted() --")
print("До:", [s["name"] for s in students])
new_list = sorted(students, key=lambda s: s["age"])
print("Результат sorted():", [(s["name"], s["age"]) for s in new_list])
print("Оригинал после sorted():", [s["name"] for s in students])

print("\n-- sort() на копии --")
copy_students = copy.deepcopy(students)
result = copy_students.sort(key=lambda s: s["age"])
print("Возвращает sort():", result)
print("Копия после sort():", [(s["name"], s["age"]) for s in copy_students])

print("\nИсходный список не изменился:",
      original_order == [s["name"] for s in students])