from uploadApp.models import Employee, Student, Course, Centre
import csv

def employee_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _, created = Employee.objects.get_or_create(
                name=row[0],
                designation=row[1],
                rating=row[2],
                salary=row[3],
                on_sabbatical=row[4],
                number_of_leaves=row[5],
                )

def studnet_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0],
                dob=row[1],
                attendance=row[2],
                courses=row[3],
                batch=row[4],
                paid_fees=row[5],
                passed=row[6],
                placed=row[7],
                centre=model.objects.get(name=row[8]),
                )

def centre_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0],
                rating=row[1],
                city=row[2],
                state=row[3],
                location=row[4],
                hod=Employee.objects.get(name=row[5]),
                )

def course_csv_parser(model, csv_path):
    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _, created = Student.objects.get_or_create(
                name=row[0],
                teacher=Employee.objects.get(name=row[1]),
                )