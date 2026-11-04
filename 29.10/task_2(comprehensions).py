students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

group_a = [s["name"] for s in students if s["group"] == "A"]
print("Группа A:", group_a)

ages = [s["age"] for s in students]
print("Возрасты:", ages)

older_20 = [s["name"] for s in students if s["age"] > 20]
print("Старше 20:", older_20)

averages = [sum(s["scores"]) / len(s["scores"]) for s in students]
print("Средние оценки:", [round(a, 1) for a in averages])

descriptions = [f'{s["name"]} — {s["age"]} лет' for s in students]
print("Описания:", descriptions)