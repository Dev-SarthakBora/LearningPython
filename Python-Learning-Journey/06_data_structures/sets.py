# sets.py

skills_a = {"Python", "SQL", "Tableau", "Excel"}
skills_b = {"Python", "R", "PowerBI", "Excel"}
skills_c = {"C++", "Python", "SQL"}

common_all = skills_a & skills_b & skills_c
unique_to_a = skills_a - (skills_b | skills_c)
rare_skills = (skills_a ^ skills_b) - skills_c
all_skills = set.union(skills_a, skills_b, skills_c)
has_python = all("Python" in s for s in [skills_a, skills_b, skills_c])
print(common_all)
print(unique_to_a)
print(rare_skills)
print(all_skills)
print(has_python)
