import matplotlib.pyplot as plt
import os


##################### Main Menu ################################
dta = []
file_name = ''
def main():

    global dta, file_name
    print('************************* Main Menu *************************')
    print('1. Read CSV file of grades')
    print('2. Generate student report file')
    print('3. Generate student report charts')
    print('4. Generate class report file')
    print('5. Generate class report charts')
    print('6. Quit')
    print('*************************************************************')
    try:
        chosen_option = int(input(''))
        if chosen_option == 1:
            try:
                dta, file_name = option1()
            except:                      # Except block to catch any returns that might cause a problem
                pass
            main()
        elif chosen_option == 2:
            try:                      # Try Except block in-case dta does not exist or wrong type given
                if len(dta) == 0:
                    print(f'No data found')
                    main()
                else:
                    option2(dta)
            except TypeError:
                print(f'No data found')
                main()
        elif chosen_option == 3:
            try:                      # Try Except block in-case dta does not exist or wrong type given
                if len(dta) == 0:
                    print(f'No data found')
                    main()
                else:
                    option3(dta)
            except TypeError:
                print(f'No data found')
                main()

        elif chosen_option == 4:
            try:                      # Try Except block in-case dta does not exist or wrong type given
                if file_name == '':
                    print(f'No data found')
                    main()
                else:
                    option4(dta)
            except TypeError:
                print(f'No data found')
                main()
        elif chosen_option == 5:
            try:                      # Try Except block in-case dta does not exist or wrong type given
                if file_name == '':
                    print(f'No data found')
                    main()
                else:
                    option5(dta)
            except TypeError:
                print(f'No data found')
                main()

        elif chosen_option == 6:
            pass
        else:
            print(f'\nOption selected does not exists\nPlease try an option from the numbered options below.')
            main()
    except:
        print(f'\nOption selected does not exists\nPlease try an option from the numbered options below.')
        main()




##################### Option 1 #################################

def option1():
    '''This function is used to read the csv file inputed by the user'''
    try:
        file_name = input('Please enter CSV file name (with the .csv): ')
        data = []
        with open(f'{file_name}','r') as dta:
            dta.readline()
            for line in dta:
                data.append(line.strip().split(','))

            print(f'\n{file_name} successfully read!\n')

        return data, file_name
    except FileNotFoundError:
        print('\nSorry, file not found :(\n')
    except TypeError:
        print('\nSorry, file not found :(\n')


##################### Option 2 #################################

def option2(dta):
    '''This function generates a report for a student in a text file by entering the student's UIN'''

    # function asks for the student's UIN, if valid function proceeds. If not valid, program will ask again.
    test = True
    while test == True:
        UIN = input(f'Enter student\'s UIN: ')

        for students in dta:
            if students[0] == UIN:
                selected_student = students
                test = False
        if test == True:
            print('\nSorry but the UIN you inputted was not valid, please try again\n')

    ss = [float(selected_student[i]) for i in range(len(selected_student)) ] # Turns selected student's information into integer elements
    with open(f'{UIN}.txt','w') as student:
        exams_mean = (ss[19] + ss[20] + ss[21])/3
        labs_mean = (ss[1]+ss[2]+ss[3]+ss[4]+ss[5]+ss[6])/6
        quizzes_mean = (ss[7]+ss[8]+ss[9]+ss[10]+ss[11]+ss[12])/6
        reading_mean = (ss[13]+ss[14]+ss[15]+ss[16]+ss[17]+ss[18])/6
        score = ((labs_mean*.25) + (quizzes_mean*.10) + (reading_mean*.10) + (ss[19]*.15) + (ss[20]*.15) + (ss[21]*.15) + (ss[22]*.10))
        letter = ''
        if score < 60:
            letter = 'F'
        elif 60 <= score < 70:
            letter = 'D'
        elif 70 <= score < 80:
            letter = 'C'
        elif 80 <= score < 90:
            letter = 'B'
        elif 90 <= score <= 100:
            letter = 'A'

        student.write(f'Exams mean: {round(exams_mean,1)}\n')
        student.write(f'Labs mean: {round(labs_mean,1)}\n')
        student.write(f'Quizzes mean: {round(quizzes_mean,1)}\n')
        student.write(f'Reading activities mean: {round(reading_mean,1)}\n')
        student.write(f'Score: {round(score,1)}%\n')
        student.write(f'Letter grade: {letter}\n')

    print(f'\nFile {UIN}.txt was written...\n')
    main()

##################### Option 3 #################################

def option3(dta):
    '''This function generates a report for a student in a text file by entering the student's UIN'''

    # function asks for the student's UIN, if valid function proceeds. If not valid, program will ask again.
    test = True
    while test == True:
        UIN = input(f'Enter student\'s UIN: ')

        for students in dta:
            if students[0] == UIN:
                selected_student = students
                test = False
        if test == True:
            print('\nSorry but the UIN you inputted was not valid, please try again\n')

    path = f'{selected_student[0]}'
    if not os.path.isdir(path):
        print(f'\nNew directory created: {selected_student[0]}')
        os.makedirs(path)
    else:
        print(f'\nDirectory {selected_student[0]} overwritten...')

    ss = [float(selected_student[i]) for i in range(len(selected_student)) ] # Turns selected student's information into integer elements
    # Bar chart for exam scores #
    exam = ['Exam 1', 'Exam 2', 'Exam 3']
    exam_grades = [ss[19],ss[20],ss[21]]
    Xam = plt.bar(exam, exam_grades)
    plt.ylabel('Score (%)')
    plt.xlabel('Exam #')
    plt.title(f'Exam grades for {int(ss[0])}')
    plt.savefig(os.path.join(path,'Exam.png'))
    plt.close()

    # Bar chart for labs grades #
    labs = ['Lab 1','Lab 2', 'Lab 3','Lab 4','Lab 5','Lab 6']
    lab_grades = [ss[1],ss[2],ss[3],ss[4],ss[5],ss[6]]
    lab = plt.bar(labs, lab_grades)
    plt.ylabel('Score (%)')
    plt.xlabel('Lab #')
    plt.title(f'Lab grades for {int(ss[0])}')
    plt.savefig(os.path.join(path, 'Lab.png'))
    plt.close()

    # Bar chart for quiz grades #
    quiz = ['Quiz 1', 'Quiz 2','Quiz 3','Quiz 4','Quiz 5','Quiz 6',]
    quiz_grades = [ss[7], ss[8], ss[9], ss[10], ss[11], ss[12]]
    Q = plt.bar(quiz, quiz_grades)
    plt.ylabel('Score (%)')
    plt.xlabel('Quiz #')
    plt.title(f'Quiz grades for {int(ss[0])}')
    plt.savefig(os.path.join(path, 'Quiz.png'))
    plt.close()

    # Bar chart of reading activities #
    reading = ['R.A. 1', 'R.A. 2', 'R.A. 3','R.A. 4','R.A. 5', 'R.A. 6']
    reading_grades = [ss[13], ss[14], ss[15], ss[16], ss[17], ss[18]]
    Q = plt.bar(reading, reading_grades)
    plt.ylabel('Score (%)')
    plt.xlabel('Reading Activity #')
    plt.title(f'Reading Activity grades for {int(ss[0])}')
    plt.savefig(os.path.join(path, 'ReadingAct.png'))
    plt.close()

    print(f'Exam.png saved...')
    print(f'Lab.png saved...')
    print(f'Quiz.png saved...')
    print(f'ReadingAct.png saved...\n')
    main()

######################### Option 4 #######################################

def option4(dta):

    report = open('report.txt', 'w+')
    scores = dta
    final_grades = []
    for index, student in enumerate(scores):
        final_grades.append((float(student[1]) * (.25 / 6)) + (float(student[2]) * (.25 / 6)) +
                            (float(student[3]) * (.25 / 6)) + (float(student[4]) * (.25 / 6)) +
                            (float(student[5]) * (.25 / 6)) +
                            (float(student[6]) * (.25 / 6)) +
                            (float(student[7]) * (.10 / 6)) + (float(student[8]) * (.10 / 6)) +
                            (float(student[9]) * (.10 / 6)) + (float(student[10]) * (.10 / 6)) +
                            (float(student[11]) * (.10 / 6)) + (float(student[12]) * (.10 / 6)) +
                            (float(student[13]) * (.10 / 6) + (float(student[14]) * (.10 / 6)) +
                             (float(student[15]) * (.10 / 6)) + (float(student[16]) * (.10 / 6)) +
                             (float(student[17]) * (.10 / 6)) + (float(student[18]) * (.10 / 6)) +
                             (float(student[19]) * .15) + (float(student[20]) * .15)) +
                            (float(student[21]) * .15) + (float(student[22]) * .10))
        # This prints all 0 indexed element in each list
        # print(student[0])
    # print(scores)
    # print(len(scores))
    sorted_grades = sorted(final_grades)
    median_score = (sorted_grades[int((len(scores)) / 2)] + sorted_grades[int(((len(scores)) / 2) + 1)]) / 2
    # print(round(median_score,1))
    mean_score = sum(final_grades) / len(scores)
    # print(round(mean_score, 1))
    # print(round(min(final_grades), 1))
    # print(round(max(final_grades), 1))
    standard_dev = []
    for grade in final_grades:
        x = (grade - mean_score) ** 2
        standard_dev.append(x)
    standard_deviation = (sum(standard_dev) / (len(scores) - 1)) ** (1 / 2)
    # print(round(standard_deviation, 1))

    # Remember to write this to report.txt
    report.write(f"Total number of students: {len(scores)}\n")
    report.write(f"Minimum score: {round(min(final_grades), 1)}\n")
    report.write(f"Maximum score: {round(max(final_grades), 1)}\n")
    report.write(f"Median score: {round(median_score, 1)}\n")
    report.write(f"Mean score: {round(mean_score, 1)}\n")
    report.write(f"Standard deviation: {round(standard_deviation, 1)}\n")
    report.close()
    print(f'\nReport writen!\n')

    main()

######################### Option 5 #######################################

def option5(dta):
    scores = dta
    final_grades = []
    for index, student in enumerate(scores):
        final_grades.append((float(student[1]) * (.25 / 6)) + (float(student[2]) * (.25 / 6)) +
                            (float(student[3]) * (.25 / 6)) + (float(student[4]) * (.25 / 6)) +
                            (float(student[5]) * (.25 / 6)) +
                            (float(student[6]) * (.25 / 6)) +
                            (float(student[7]) * (.10 / 6)) + (float(student[8]) * (.10 / 6)) +
                            (float(student[9]) * (.10 / 6)) + (float(student[10]) * (.10 / 6)) +
                            (float(student[11]) * (.10 / 6)) + (float(student[12]) * (.10 / 6)) +
                            (float(student[13]) * (.10 / 6) + (float(student[14]) * (.10 / 6)) +
                             (float(student[15]) * (.10 / 6)) + (float(student[16]) * (.10 / 6)) +
                             (float(student[17]) * (.10 / 6)) + (float(student[18]) * (.10 / 6)) +
                             (float(student[19]) * .15) + (float(student[20]) * .15)) +
                            (float(student[21]) * .15) + (float(student[22]) * .10))

    rounded_grade = []
    letter_grade = []
    A = []
    B = []
    C = []
    D = []
    F = []
    for index, grade in enumerate(final_grades):
        # print(index, grade)
        rounded_grade.append(round(grade, 1))
    for index, grade in enumerate(rounded_grade):
        # print(index, grade)
        if grade >= 90:
            letter_grade.append('A')
        elif 80 <= grade < 90:
            letter_grade.append('B')
        elif 70 <= grade < 80:
            letter_grade.append('C')
        elif 60 <= grade < 70:
            letter_grade.append('D')
        elif grade < 60:
            letter_grade.append('F')
    for letter in letter_grade:
        if letter == 'A':
            A.append(letter)
        elif letter == 'B':
            B.append(letter)
        elif letter == 'C':
            C.append(letter)
        elif letter == 'D':
            D.append(letter)
        elif letter == 'F':
            F.append(letter)
    grade_count = [len(A), len(B), len(C), len(D), len(F)]

    grades = ['A', 'B', 'C', 'D', 'F']

    # To save into new directory
    path = f'class_charts'
    if not os.path.isdir(path):
        print(f'\nNew directory created: class_charts')
        os.makedirs(path)
    else:
        print(f'\nDirectory class_charts overwritten...\n')

    # Pie Graph
    pie_chart = plt.pie(grade_count, labels=grades, autopct=None,
                        colors=['#6eda00', '#afd275', '#fdda75', '#feb700', '#c71b00'])
    plt.title('Class Letter Grades')
    plt.savefig(os.path.join(path, "Letter_Grades_Distributed_Pie_Graph.png"))
    plt.close()

    # Bar Graph
    bar_chart = plt.bar(grades, grade_count, align='center',
                        color=['#6eda00', '#afd275', '#fdda75', '#feb700', '#c71b00'])
    plt.yticks(range(0, 65, 10))
    plt.xlabel('Grade')
    plt.ylabel('Count')
    plt.title('Class Letter Grades')
    plt.savefig(os.path.join(path, "Letter_Grades_Distributed_Bar_Graph.png"))
    plt.close()

    main()

main()