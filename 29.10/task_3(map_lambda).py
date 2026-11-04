students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

upper_names = list(map(lambda s: s["name"].upper(), students))
print("Верхний регистр:", upper_names)

ages_plus_one = list(map(lambda s: s["age"] + 1, students))
print("Возраст + 1:", ages_plus_one)

averages = list(map(lambda s: sum(s["scores"]) / len(s["scores"]), students))
print("Средние оценки:", averages)

name_avg = list(map(
    lambda s: {"name": s["name"], "average": sum(s["scores"]) / len(s["scores"])},
    students,
))
print("name + average:")
for item in name_avg:
    print("  ", item)