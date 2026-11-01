#!/usr/bin/python3

with open("student_output", "r") as f:
    first = f.readline().strip()

name = "Ervin Howell"

if name in first:
    print("Employee Name: OK")
else:
    print("Employee Name: Incorrect")
