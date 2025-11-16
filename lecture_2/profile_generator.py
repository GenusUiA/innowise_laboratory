#user data
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []

#life stage function
def generate_profile(age:int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

#loop for input hobbies
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == 'stop':
        break
    hobbies.append(hobby)
    
life_stage = generate_profile(current_age) #get life stage 
user_profile = {"Name": user_name, "Age": current_age, "Life Stage": life_stage, f"Favorite Hobbies ({len(hobbies)})": hobbies} #create user profile in dict

#correct output for user profile 
print()
print("---")
print("Profile Summary:")
print(f"Name: {user_name}")
print(f"Age: {current_age}")
print(f"Life Stage: {life_stage}")
if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else: 
    print(f"Favorite Hobbies ({len(hobbies)})")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")


