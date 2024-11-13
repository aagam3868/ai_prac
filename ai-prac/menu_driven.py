# def display_menu():
#     print("\n--- Question Menu ---")
#     print("1. What is Python?")
#     print("2. What are lists in Python?")
#     print("3. What is a function?")
#     print("4. What is a loop?")
#     print("5. Exit")

# def answer_question(choice):
#     if choice == 1:
#         return "Python is a high-level, interpreted programming language known for its simplicity and versatility."
#     elif choice == 2:
#         return "Lists in Python are ordered collections of items, which can be of any data type, and are mutable."
#     elif choice == 3:
#         return "A function is a block of reusable code that performs a specific task when called."
#     elif choice == 4:
#         return "A loop in programming allows repetitive execution of a block of code as long as a condition is met."
#     elif choice == 5:
#         return "Exiting the program."
#     else:
#         return "Invalid choice! Please choose a valid question number."

# # Main Program
# def menu_driven_program():
#     while True:
#         display_menu()
#         choice = int(input("\nEnter the number of the question you want an answer to (or press 5 to exit): "))
        
#         answer = answer_question(choice)
#         print(f"\nAnswer: {answer}")
        
#         if choice == 5:
#             break

# # Run the menu-driven program
# menu_driven_program()




people = { 
    "Alice": {"hobbies": ["apple"], "instruments": []}, 
    "Bob": {"hobbies": ["cricket"], "instruments": ["piano"]}, 
    "Charlie": {"hobbies": ["chess"], "instruments": ["flute"]}, 
    "David": {"hobbies": ["buttermilk"], "instruments": []}, 
} 
 
def has_hobby(person, hobby): 
    return hobby in people[person]["hobbies"] 
 
def plays_instrument(person, instrument): 
    return instrument in people[person]["instruments"] 
 
def main(): 
    # Define the menu 
    menu = """ 
        Menu: 
        1. Who likes apple? 
        2. Does anybody like apple? 
        3. Is it true that nobody likes apple? 
        4. Who likes apple as well as enjoys playing cricket and piano? 
        5. Does anybody play at least one instrument? 
        6. Who likes to play chess, drink buttermilk but does not play any instrument? 
        7. Who share at least one hobby and at least one instrument? 
        8. Who are the persons sharing common instruments but no hobbies in common? 
        
        Enter question number (or 0 to exit):  
    """ 
 
    while True: 
        print(menu) 
        choice = int(input().strip())
 
        if choice == 0: 
            break 
 
        # Answer based on user selection 
        if choice == 1: 
            answer = [person for person in people if has_hobby(person, "apple")] 
            print(", ".join(answer) + " like apple." if answer else "Nobody likes apple.") 
 
        elif choice == 2: 
            answer = any(has_hobby(person, "apple") for person in people)
            print("Yes" if answer else "No")
 
        elif choice == 3: 
            answer = not any(has_hobby(person, "apple") for person in people)
            print("Yes" if answer else "No") 
 
        elif choice == 4: 
            answer = [person for person in people if has_hobby(person, "apple") and has_hobby(person, "cricket") and plays_instrument(person, "piano")] 
            print(", ".join(answer) + " like apple, cricket, and piano." if answer else "Nobody likes all three.") 
 
        elif choice == 5: 
            answer = any(people[person]["instruments"] for person in people) 
            print("Yes" if answer else "No") 
 
        elif choice == 6: 
            answer = [person for person in people if has_hobby(person, "chess") and has_hobby(person, "buttermilk") and not people[person]["instruments"]]
            print(", ".join(answer) + " fulfill the criteria." if answer else "Nobody matches the criteria.") 
 
        elif choice == 7: 
            answer = [
                person 
                for person in people 
                if set(people[person]["hobbies"]) & set(people[other]["hobbies"]) and set(people[person]["instruments"]) & set(people[other]["instruments"])
                for other in people if person != other
            ]
            print(", ".join(set(answer)) + " share at least one hobby and instrument." if answer else "Nobody shares both.") 
 
        elif choice == 8: 
            answer = [
                person 
                for person in people 
                if set(people[person]["instruments"]) & set(people[other]["instruments"]) and not (set(people[person]["hobbies"]) & set(people[other]["hobbies"]))
                for other in people if person != other
            ]
            print(", ".join(set(answer)) + " share common instruments but no hobbies in common." if answer else "Nobody matches the criteria.") 
 
        else: 
            print("Invalid choice. Please try again.")

# Run the program
main()
