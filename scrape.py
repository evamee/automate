import pymysql
import webbrowser
import time
import itertools

connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="", database="trial")
cursor = connection.cursor()

all_students = "select * from tbl_biodata_attach"
cursor.execute(all_students)
students = cursor.fetchall()

p = []
tbl = "<tr><td>Title</td><td>Surname</td><td>Firstname</td><td>Othername</td><td>First Choice</td>"
p.append(tbl)

for row in students:
    all_halls = cursor.execute("select * from halls")
    halls = cursor.fetchall()
    if row[7] == "Male" and row[30] != "ATE":
        male = "update tbl_biodata_attach set hall_id = 1 where GENDER = 'Male'"
        cursor.execute(male)
        all_male = cursor.fetchall()
        title = "<tr><td>%s</td>" % row[2]
        p.append(title)
        surname_name = "<td>%s</td>" % row[3]
        p.append(surname_name)
        first_name = "<td>%s</td>" % row[4]
        p.append(first_name)
        other_name = "<td>%s</td>" % row[5]
        p.append(other_name)
        firstChoice = "<td>%s</td>" % row[30]
        p.append(firstChoice)
        # print(row[2], " ", row[3], " ", row[4], " ", row[5], " ", row[30])

    elif row[7] == "Female" and row[30] != "ATE":
        female = "update tbl_biodata_attach set hall_id = 2 where GENDER = 'Female'"
        cursor.execute(female)
        all_female = cursor.fetchall()
        title = "<tr><td>%s</td>" % row[2]
        p.append(title)
        surname_name = "<td>%s</td>" % row[3]
        p.append(surname_name)
        first_name = "<td>%s</td>" % row[4]
        p.append(first_name)
        other_name = "<td>%s</td>" % row[5]
        p.append(other_name)
        firstChoice = "<td>%s</td>" % row[30]
        p.append(firstChoice)
        # all_female_students = [row[2], " ", row[3], " ", row[4], " ", row[5], " ", row[30]]
        # print(all_female_students)
    else:
        choice = "update tbl_biodata_attach set hall_id = 5 where FIRST_CHOICE = 'ATE'"
        cursor.execute(choice)
        all_choice = cursor.fetchall()
        title = "<tr><td>%s</td>" % row[2]
        p.append(title)
        surname_name = "<td>%s</td>" % row[3]
        p.append(surname_name)
        first_name = "<td>%s</td>" % row[4]
        p.append(first_name)
        other_name = "<td>%s</td>" % row[5]
        p.append(other_name)
        firstChoice = "<td>%s</td>" % row[30]
        p.append(firstChoice)
        # first_choice = [row[2], " ", row[3], " ", row[4], " ", row[5], " ", row[30]]

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type">
    <title>Python Webbrowser</title>
    </head>
    <body>
        <table>
            %s
        </table>
    </body>
</html>
'''%(p)

filename = "webbrowser.html"


def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)

cursor.close()
connection.close()

