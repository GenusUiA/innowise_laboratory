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
        
        try:
            option = int(input("Enter your choise: "))
        except Exception as e:
            print(f"{e}, enter a number")
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
            try: 
                name = str(input("Enter student name: ")).capitalize()
                for student in students:
                    if name in student["name"]:
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
            except Exception as e:
                print("Enter your real name")
            
        elif option == 3:
            sum_avg = 0
            count = 0
            averages = []
            for student in students:
                for grades in student["grades"]:
                    for grade in grades:
                        sum_avg += int(grade)
                        count += 1
                if count == 0:
                    average = 'N/A'
                else: 
                    average = sum_avg / count
                    averages.append(average)
                count = 0
                print(f"{name}'s average grade is {average}")
            print("--------------------------")
            print(f"Max Average: {max(averages)}")
            print(f"Min Average: {min(averages)}")
            print(f"Overall Average: {sum(averages) / len(averages)}")
        # elif option == 4:
        #     avg = lambda students["grades"]: sum(grades)/len(grades)
        #     top_student = max(students, key = lambda s: avg(s["grades"]))
        #     print(f"The student with the highest average is {top_student["name"]} with a grade of {avg(top_student["grades"])}")
                
        elif option == 5:
            break
        else: 
            print("Enter number from the range (1-5)")
        print()
            

