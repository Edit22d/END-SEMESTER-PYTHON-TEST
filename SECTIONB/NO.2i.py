# student detials and mark
def student_detials ():
    student_name = input('Enter the student name:\t')
    student_number = input('Enter the student number:\t')
    programming = int(input('Enter the programming mark:\t'))
    data_science = int(input('Enter the data science mark:\t'))
    computer_application = int(input('Enter the computer application mark:\t'))
    number_subject = 3
    average_mark =programming + data_science + computer_application / number_subject
    print(f'The average mark of {student_name}, reg no {student_number},in {programming},{data_science} and {computer_application} is {average_mark:.3f}')
student_detials()
     
    
    