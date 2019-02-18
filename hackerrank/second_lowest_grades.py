# Given the names and grades for each student in a Physics class of N students,
# store them in a nested list and print the name(s) of any student(s) having
# the second lowest grade.

# Input Format
# ------------
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines;
# the first line contains a student's name, and the second line
# contains their grade. 

# Sample Input
# ------------
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output
# -------------
# Berry
# Harry

students = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
grades = [37.21, 37.21, 37.2, 41, 39]

#if __name__ == '__main__':
#    scores = dict()
#    for _ in range(int(input())):
#        name = input()
#        score = float(input())
#	 <by @ivanleocnz>
#	 students.append(name)
#	 grades.append(score)

# find second lowest score + possible repetitions
# forming a list of indexes for each repetition
second_lowest_scores = list()
# second lowest grade found
sorted_grades = sorted(grades)
lowest_score = [n for n in sorted_grades if sorted_grades[0] < n][0]
for k, v in enumerate(grades):
    if v == lowest_score:
        second_lowest_scores.append(k)

# finds the students which have the second lowest grades
# based on the indexes of lowest scorres (repetition)
score_students = [students[idx] for idx in second_lowest_scores]

# printing students (alphabetical order)
for student in sorted(score_students):
    print(student)
