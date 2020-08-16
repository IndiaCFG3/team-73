from django.db import models


class Student(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    attendance = models.IntegerField()
    courses = models.ManyToManyField('Course')
    batch = models.CharField(max_length=200)
    paid_fees = models.BooleanField()
    passed = models.BooleanField()
    placed = models.BooleanField()
    centre = models.ForeignKey('Centre', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    rating = models.IntegerField()
    salary = models.IntegerField()
    on_sabbatical = models.BooleanField()
    number_of_leaves = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Centre(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
