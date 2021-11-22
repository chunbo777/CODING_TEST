grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:
def scaling(grade):
    if grade <= 4.0:
      grade = grade*25
    return grade
      
# assign the result of your map function to the variable grades_100scale
grades_100scale = map(scaling, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 
grades_100scale = list(grades_100scale)
# print updated_grade_list

print(grades_100scale)

