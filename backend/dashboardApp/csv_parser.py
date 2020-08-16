from uploadApp.models import Employee, Student, Course, Centre
import csv

def employee_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Employee.objects.get_or_create(
                name=row[0]
                )

def student_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0]
                )

def centre_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0]
                )

def course_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0],
                teacher=Employee.objects.get(name=row[1]),
                )