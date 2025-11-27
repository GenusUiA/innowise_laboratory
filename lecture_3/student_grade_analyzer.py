students = []

def Avg(grades) -> int:
    """For counting the average meaning"""
    sum = 0
    count = 0
    for grade in grades:
        sum += grade
        count += 1
    return sum / count

if __name__ == "__main__":
    while(True):
        """loop for checking the choise"""
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        
        try:  # checking for options
            option = int(input("Enter your choise: "))
        except Exception as e:
            print("Enter a number")
            continue
            
        if option == 1:
            try: 
                name = str(input("Enter student name: ")).capitalize()
            except Exception as e:
                print("Enter your real name")
            student = {"name": name, "grades": []}
            if student in students:
                print("User already exists")
            else:
                students.append(student)
        elif option == 2:
            flag = False
            try: 
                name = str(input("Enter student name: ")).capitalize()
                for student in students:
                    if name in student["name"]:
                        flag = True
                        while True:
                            grade = input("Enter a grade (or 'done' to finish): ")
                            if grade == 'done':
                                break
                            try:
                                int_grade = int(grade)
                                if int_grade > 100 or int_grade < 0:
                                    print("Enter the grade from 0 to 100")
                                else:
                                    student["grades"].append(grade)
                            except:
                                print("Enter the grade from 0 to 100")
                if flag == False:
                    print("Student not in the list") 
            except Exception as e:
                print("Enter your real name")
            
        elif option == 3:
            sum_avg = 0
            count = 0
            averages = []
            for student in students:
                if student["grades"]:
                    for grade in student["grades"]:
                        sum_avg += int(grade)
                        count += 1
                    if count == 0:
                        average = 'N/A'
                    else: 
                        average = round(sum_avg / count, 1)
                        averages.append(average)
                    count = 0
                    print(f"{name}'s average grade is {average}")
            if averages:
                print("--------------------------")
                print(f"Max Average: {max(averages)}")
                print(f"Min Average: {min(averages)}")
                print(f"Overall Average: {sum(averages) / len(averages)}")
            else: 
                print("There is no students with the grades")
        elif option == 4:
            if not students:
                print("No students in list")
                continue
            
            avg = lambda students: Avg([int(grade) for grade in students["grades"]]) if students["grades"] else 0 
            top_student = max(students, key = avg)
            print(f"The student with the highest average is {top_student["name"]} with a grade of {round(avg(top_student),1)}")
                
        elif option == 5:
            break
        else: 
            print("Enter number from the range (1-5)")
        print()
            

