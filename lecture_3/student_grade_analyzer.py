students = []

def Avg(grades: list) -> float:
    """For counting the average meaning"""
    return sum(grades) / len(grades)

def is_valid_name(name: str) -> bool:
    """For checking the name"""
    return name.isalpha()

if __name__ == "__main__":
    while True:
        """loop for checking the choice"""
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        
        try:  
            option = int(input("Enter your choice: "))
        except Exception as e:
            print("Enter a number")
            continue
        
        # Add new student    
        if option == 1:
            try: 
                name = str(input("Enter student name: ")).capitalize()
                if not is_valid_name(name):
                    print("You should use only letters")
                else:
                    student = {"name": name, "grades": []}
                    #check user name
                    if any(student["name"] == name for student in students):
                        print("User already exists")
                    else:
                        students.append(student)
            except Exception as e:
                print("Enter your correct name")
        
        # Add grades to student
        elif option == 2:
            founded = False
            try: 
                name = str(input("Enter student name: ")).capitalize()
                for student in students:
                    if name == student["name"]:
                        founded = True
                        while True:
                            grade = input("Enter a grade (or 'done' to finish): ")
                            if grade == 'done':
                                break
                            try:
                                if int(grade) > 100 or int(grade) < 0:
                                    print("Enter the grade from 0 to 100")
                                else:
                                    student["grades"].append(int(grade))
                            except:
                                print("Invalid input. Please enter a number.")
                if founded == False:
                    print("Student not in the list") 
            except Exception as e:
                print("Enter your correct name")
        
        # Generate full report
        elif option == 3:
            print("--- Student Report ---")
            averages = []
            
            for student in students:
                if student["grades"]:
                    average = round(Avg(student["grades"]), 1)
                    averages.append(average)
                    print(f"{student["name"]}'s average grade is {average}.")
                else:
                    print(f"{student["name"]}'s average grade is N/A.")   
                
            if averages:
                print("--------------------------")
                print(f"Max Average: {max(averages)}")
                print(f"Min Average: {min(averages)}")
                print(f"Overall Average: {sum(averages) / len(averages)}")
            else: 
                print("There is no students with grades")
        
        #Top student        
        elif option == 4:
            if not students:
                print("No students in list")
                continue
            students_with_grades = [student for student in students if student["grades"]]
            if not students_with_grades:
                print("No students with grades")
            else:
                avg = lambda student: Avg(student["grades"]) if student["grades"] else 0 
                top_student = max(students_with_grades, key=avg)
                print(f"The student with the highest average is {top_student["name"]} with a grade of {round(avg(top_student),1)}")
        
        #Exit from application
        elif option == 5:
            print("Exiting program.")
            break
        else: 
            print("Enter number from the range (1-5)")
        print()