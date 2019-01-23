""" Sam is a professor at the university and likes to round each student's
grade according to these rules:

    - If the difference between the grade and the next multiple of 5 is less
    than 3, round grade up to the next multiple of 5.
    - If the value of grade is less than 38, no rounding occurs as the result
    will still be a failing grade.
"""

multiples_5 = [n for n in range(1, 101) if n % 5 == 0]

grades = [33, 38, 67, 73]

print("Grades: ", grades)

for idx, grade in enumerate(grades[:]):
    for m in multiples_5:
	# all numbers above 38, where the current multiple is greather than
        if m >= 38 and m > grade:
            # calculating difference between the current multiple
            # and the current grade
            diff = m - grade
            # if the difference between the current multiple
            # and the current grade is less than 3
            if diff < 3:
                # the current grade is rounded with the difference,
                # moving the grade automatically to the next multiple
                grades[idx] = grade + diff


print("Grades (rounded): ", grades)
