from pathlib import Path
import json

def convert_students_to_csv(json_path, csv_path):
    csv = ["id;name;area;year"]
    students = json.loads(Path(json_path).read_text(encoding="utf-8"))["students"]
    
    for student in students:
        text = ""
        for i in student.keys():
            text += str(student[i])
            if i != "year":
                text += ";"
        csv.append(text)
        text = ""

    Path(csv_path).write_text("\n".join(csv), encoding="utf-8")

if __name__ == "__main__":
    convert_students_to_csv("students.json", "students.csv")
    convert_students_to_csv("students2.json", "students2.csv")

    

