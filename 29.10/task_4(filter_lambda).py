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

older_20 = list(map(lambda s: s["name"], filter(lambda s: s["age"] > 20, students)))
print("Старше 20:", older_20)

group_b = list(map(lambda s: s["name"], filter(lambda s: s["group"] == "B", students)))
print("Группа B:", group_b)

high_avg = list(map(lambda s: s["name"], filter(lambda s: avg(s) >= 85, students)))
print("Средняя >= 85:", high_avg)

best_a = list(map(
    lambda s: s["name"],
    filter(lambda s: s["group"] == "A" and avg(s) >= 90, students),
))
print("Группа A, средняя >= 90:", best_a)