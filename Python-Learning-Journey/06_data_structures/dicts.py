# dicts.py
employees = {
    "A": {"dept": "HR", "salary": 55000},
    "B": {"dept": "Tech", "salary": 85000},
    "C": {"dept": "Tech", "salary": 95000},
    "D": {"dept": "Finance", "salary": 65000},
    "E": {"dept": "HR", "salary": 72000}
}

by_dept = {}
for name, info in employees.items():
    by_dept.setdefault(info["dept"], []).append(info["salary"])

avg_salary = {d: sum(s)/len(s) for d, s in by_dept.items()}
top_earners = {k: v for k, v in employees.items() if v["salary"] > 70000}
sorted_employees = dict(sorted(employees.items(), key=lambda x: x[1]["salary"], reverse=True))
merged = {**employees, "F": {"dept": "Tech", "salary": 88000}}
print(by_dept)
print(avg_salary)
print(top_earners)
print(sorted_employees)
print(merged)

