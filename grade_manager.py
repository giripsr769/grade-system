from modules.grade import student_grade

def final_result(mark, grade):
    print(f'You earned an "{grade}" grade for scoring {int(mark)} marks!')

try:
    mark = float(input("Enter the mark: "))
    if mark >= 0 and mark <= 100:
        grade = student_grade(mark)
        final_result(mark, grade)   
    else:
        print("The mark is should be between 0 and 100.")
except:
    print("Invalid input. Please enter a numeric value for the mark.")
finally:
    print("Thank you for using the grade manager!")
