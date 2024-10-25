'''
class patient:
    people={}
    field=['Patient Name','Age','Condition']
    medics={}
    
    def ram(self):
        while True:
            print("1.Add Patient Details\n2.Add Appointment Details\n3.View Patient Details")
            option=int(input())
            if(option==1):
                self.patientAdd()
            elif(option==2):
                x=schedule_appointment()
                x.appointment()
            
            elif(option==3):
                print("1.View Patient List\n2.View Appointment List")
                y=int(input())
                if(y==1):
                   self.get_patients()
                elif(y==2):
                    a=schedule_appointment()
                    a.get_appointment()
            else:
                print("INVALID")   
    def patientAdd(self):
        for i in self.field:
            x=input('Enter {} :'.format(i))
            if i=='Age':
                x=int(x)
                Age=x
            self.medics[i]=x
        self.people[Age]=self.medics
        print("Patient Details Add Successfully ")


    def get_patients(self):
        if not self.people:
            print("No patients found.")
        else:
            print("Patient List:")
            for name, details in self.people.items():
                print(f"Name: {details['Patient Name']}, Age: {details['Age']}, Condition: {details['Condition']}")

                                                    
     
      
                


loki=patient()
loki.ram()
'''

print("HOSPITAL MANAGEMENT:-")
class Patient:
    people = {}
    fields = ['Patient Name', 'Age', 'Condition']
    
    def ram(self):
        while True:
            print("\n1. Add Patient Details\n2. Add Appointment Details\n3. View Patient Details\n4. Exit")
            option = int(input())
            if option == 1:
                self.patientAdd()
            elif option == 2:
                x = ScheduleAppointment()
                x.appointment()
            elif option == 3:
                print("1. View Patient List\n2. View Appointment List\n3. View Patient Condition")
                y = int(input())
                if y == 1:
                    self.get_patients()
                elif y == 2:
                    a = ScheduleAppointment()
                    a.get_appointment()
                elif y==3:
                   
                   self.get_condition()
            elif option ==4:
              print("Thanks For Yours Details")
              break
                 
            else:
                print("INVALID")

    def patientAdd(self):
        patient_data = {}
        for i in self.fields:
            a = input(f'Enter {i}: ')
            if i == 'Age':
                a = int(a)
            patient_data[i] =a
        self.people[patient_data['Patient Name']] = patient_data
        print("Patient Details Added Successfully")

    def get_patients(self):
        if not self.people:
            print("No patients found.")
        else:
            print("Patient List:")
            for name, details in self.people.items():
                print(f"Name: {details['Patient Name']}, Age: {details['Age']}, Condition: {details['Condition']}")
                
    def get_condition(self):
        if not self.people:
            print("Patient Condition Not Found")
        else:
            print("Patient Condition List")
            conditions = map(lambda details: f"Condition: {details['Condition']}, Name: {details['Patient Name']}, Age: {details['Age']}", self.people.values())
            for i in conditions:
                print(i)
                
class ScheduleAppointment:
    appointments = {}
    fields = ['Patient Name', 'DutyDoctor', 'Date']

    def appointment(self):
        appointment_data = {}
        for i in self.fields:
            b = input(f'Enter {i}: ')
            appointment_data[i] = b
        self.appointments[appointment_data['Date']] = appointment_data
        print("Appointment Added Successfully")

    def get_appointment(self):
        if not self.appointments:
            print("No appointments found.")
        else:
            print("Appointment List:")
            for date, details in self.appointments.items():
                print(f"Date: {date}, Patient Name: {details['Patient Name']}, Duty Doctor: {details['DutyDoctor']}")


      
task= Patient()
task.ram()





  
    





