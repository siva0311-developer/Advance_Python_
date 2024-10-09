x#polymorphism

'''class person1:
    def action(self):
        print("run")
        
class person2(person1):
    def action(self):
        print("walk")
        
class person3(person1):
    def action(self):
        print("swim")
obj=[person1(),person2(),person3()]

for i in obj:
    i.action()'''


'''def is_leap(year):
    if(year % 400 == 0):
        return True
    else:
         return False 

year=int(input("Enter the year: "))
if is_leap(year):
    print("year is true")
else:
    print("year is false")'''



#ramjii
'''year=int(input("Enter the year: "))
if(year % 400 == 0):
    print("return True")
else:
     print("return False")'''



'''1.Enter Student Details
2.View Details
3.Exit'''


class Student:
    students = {}

    @classmethod
    def run(cls):
        print("\n1. Enter Student Details")
        print("2. View Details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            cls.enter_details()
        elif choice == '2':
            cls.view_details()
        elif choice == '3':
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")
            cls.run()  # Re-run the method for another choice

    @classmethod
    def enter_details(cls):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        cls.students[student_id] = {'Name': name, 'Age': age}
        print(f"Details for Student ID {student_id} added successfully!")
        cls.run()  # Go back to the menu after adding

    @classmethod
    def view_details(cls):
        if not cls.students:
            print("No student details available.")
        else:
            for student_id, details in cls.students.items():
                print(f"Student ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}")
        cls.run()  # Go back to the menu after viewing

# Start the program
Student.run()

        
       































            
         
