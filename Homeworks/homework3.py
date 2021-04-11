students_concisedictionary={}
students_generaldictionary={}
grades_list=[]
def calculategrade(x,y,z):
 return 0.3*(x+y) + 0.4*(z)
for i in range(0,5):
 nameofthestudent=input("Please enter the name of the student: ")
 midtermgrade = float(input("Now please enter her/his midterm grade: "))
 projectgrade = float(input("Now please enter her/his project grade: "))
 finalgrade = float(input("Now please enter her/his final grade: "))
 passinggradeofthestudent=calculategrade(midtermgrade,projectgrade,finalgrade)
 students_generaldictionary[nameofthestudent] = [midtermgrade,projectgrade,finalgrade]
 students_concisedictionary[nameofthestudent] = passinggradeofthestudent
 grades_list.append(passinggradeofthestudent)  
 grades_list[i]=passinggradeofthestudent


grades_list.sort() 
grades_list = grades_list[::-1]
max_grade = grades_list[0]
max_grade = "{:.2f}".format(max_grade)
print(f'The maximum passing grade in this group is {max_grade}')
