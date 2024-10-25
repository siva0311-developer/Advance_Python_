'''
class Patient:
    def __init__(self):
        self.people = {}
        self.field = ['Patient Name', 'Age', 'Condition']

    def patient_add(self):
        medics = {}
        for i in self.field:
            x = input('Enter {}: '.format(i))
            if i == 'Age':
                x = int(x)  # Convert age to integer
            medics[i] = x
        self.people[medics['Age']] = medics  # Store patient data by age as key
        print("Patient Details Added Successfully")

    def get_patient(self):
        return self.people  # Return all patient details


class ScheduleAppointment:
    def __init__(self):
        self.doctor = {}
        self.fields = ['Patient Name', 'DutyDoctor', 'Date']

    def appointment(self):
        counter = {}
        for i in self.fields:
            y = input('Enter {}: '.format(i))
            counter[i] = y
        self.doctor[counter['Date']] = counter  # Store appointment data by date
        print("Appointment Scheduled Successfully")


# Example usage
task = Patient()
task.patient_add()

# Get and print all patient details
patients = task.get_patient()
print("All Patients:", patients)

amaran = ScheduleAppointment()
amaran.appointment()
'''

'''

def ram():
        print("1.Add Patient Details\n2.Add Schedule_appointment")
        y=input()
        if(y==1):
            self.patientAdd()
            ram()
        elif(y==2):
            self.appointment()
        else:
            print("Invalid")
'''

def ram():
    while True:
        print("1.Add Patient Details\n2.Add Appointment Details\n3.View Patient Details")
        option=int(input())
        if(option==1):
            x=patient()
            x.patientAdd()
        elif(option==2):
            x=schedule_appointment()
            x.appointment()
            
        elif(option==3):
            print("1.View Patient List\n2.View Appointment List")
            y=int(input())
            if(y==1):
                x=patient()
                x.get_patients()
            elif(y==2):
                a=schedule_appointment()
                a.get_appointment()
        else:
            print("INVALID")
            
class patient:
    people={}
    field=['Patient Name','Age','Condition']
    medics={}

    
    
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
            for field, details in (self.people.items()):
                print(f"Details: {details}")
                                                    
     
      
                

class schedule_appointment:
    doctor={}
    fields=['Patient Name','DutyDoctor','Date']
    counter={}
    
    def appointment(self):
        for i in self.fields:
            y=input('Enter {} :'.format(i))
            if i=='Date':
                Date=y
            self.counter[i]=y
        self.doctor[Date]=self.counter
        print("schedule_appointment Add Successfully ")
        
    def get_appointment(self):
        if not self.doctor:
            print("No schedule found.")
            return
        print("Appointment List:")
        for i, details in self.doctor.items():
            print(f"Details: {details}")    
            
ram()        






  
    





