# This program will take a csv file, parse it manually, print out the averages of the students, and if determine they're eligible for diplomas

def average_calculator(student_grades):
	total = 0
	for grade in student_grades:
		total += grade
		average = total / float(len(student_grades))
	return round(average, 2)

def diploma_eligible(average):
	if average >= 78.0:
		return "is eligible for a diploma!" 
	else:
		return "is not eligible for a diploma."

def main():
	grades = open('grades.csv')
	names = []
	averages = []

	# skip the first line 
	next(grades)

	# for every student in data
	for lines in grades:

		# split the data up
		data = lines.split(',')

		# append names column to the names list
		names.append(data[0])

		# pop off the student names from data set
		data.pop(0)

		# list comprehension, iterate over every line and make it an int
		data = [int(i) for i in data]

		# append average of line to averages list
		averages.append(average_calculator(data))

	# iterate both lists simultaneously
	for name, average in zip(names,averages):
		print average, name, diploma_eligible(average)

main()
