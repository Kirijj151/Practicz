students = [
    {"name": "Анна", "age": 20, "group": "A", "scores": [90, 85, 95]},
    {"name": "Борис", "age": 22, "group": "B", "scores": [70, 75, 80]},
    {"name": "Вера", "age": 19, "group": "A", "scores": [88, 92, 84]},
    {"name": "Глеб", "age": 21, "group": "B", "scores": [60, 70, 65]},
    {"name": "Дина", "age": 20, "group": "A", "scores": [100, 95, 90]},
    {"name": "Егор", "age": 23, "group": "B", "scores": [78, 82, 80]},
]

top_students = sorted(
    map(
        lambda s: {
            "name": s["name"],
            "group": s["group"],
            "average": sum(s["scores"]) / len(s["scores"]),
        },
        filter(lambda s: sum(s["scores"]) / len(s["scores"]) >= 80, students),
    ),
    key=lambda s: s["average"],
    reverse=True,
)

print("Топ-3 студента:")
for s in top_students[:3]:
    print(f'{s["name"]} — средняя оценка: {s["average"]:.1f}')