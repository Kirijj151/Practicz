students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

# 1. Количество студентов
print("Количество студентов:", len(students))

# 2. Список имён
names = [s["name"] for s in students]
print("Имена:", names)

# 3. Множество уникальных групп
groups = {s["group"] for s in students}
print("Группы:", groups)

# 4. Список кортежей (имя, возраст)
name_age_tuples = [(s["name"], s["age"]) for s in students]
print("Кортежи (имя, возраст):", name_age_tuples)

# 5. Словарь {имя: возраст}
name_age_dict = {s["name"]: s["age"] for s in students}
print("Словарь имя->возраст:", name_age_dict)

# 6. Самый младший и самый старший
youngest = min(students, key=lambda s: s["age"])
oldest = max(students, key=lambda s: s["age"])
print(f'Младший: {youngest["name"]} ({youngest["age"]})')
print(f'Старший: {oldest["name"]} ({oldest["age"]})')