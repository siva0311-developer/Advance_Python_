class Patient:
    def __init__(self, patient_id, name, age, gender, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info


class Staff:
    def __init__(self, staff_id, name, role, contact_info):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact_info = contact_info


class Appointment:
    def __init__(self, appointment_id, patient_id, staff_id, appointment_date):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.staff_id = staff_id
        self.appointment_date = appointment_date


class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.staff = {}
        self.appointments = {}
        self.patient_counter = 1
        self.staff_counter = 1
        self.appointment_counter = 1

    def add_patient(self, name, age, gender, contact_info):
        patient = Patient(self.patient_counter, name, age, gender, contact_info)
        self.patients[self.patient_counter] = patient
        self.patient_counter += 1
        print(f"Added Patient: {patient.name}")

    def update_patient(self, patient_id, name, age, gender, contact_info):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            patient.name = name
            patient.age = age
            patient.gender = gender
            patient.contact_info = contact_info
            print(f"Updated Patient: {patient.name}")

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            patient_name = self.patients[patient_id].name
            del self.patients[patient_id]
            print(f"Deleted Patient: {patient_name}")

    def view_patients(self):
        print("Patients:")
        for p in self.patients.values():
            print(f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Contact: {p.contact_info}")

    def add_staff(self, name, role, contact_info):
        staff = Staff(self.staff_counter, name, role, contact_info)
        self.staff[self.staff_counter] = staff
        self.staff_counter += 1
        print(f"Added Staff: {staff.name}")

    def view_staff(self):
        print("Staff:")
        for s in self.staff.values():
            print(f"ID: {s.staff_id}, Name: {s.name}, Role: {s.role}, Contact: {s.contact_info}")

    def schedule_appointment(self, patient_id, staff_id, appointment_date):
        if patient_id in self.patients and staff_id in self.staff:
            appointment = Appointment(self.appointment_counter, patient_id, staff_id, appointment_date)
            self.appointments[self.appointment_counter] = appointment
            self.appointment_counter += 1
            print(f"Scheduled Appointment for Patient ID: {patient_id} with Staff ID: {staff_id} on {appointment_date}")

    def view_appointments(self):
        print("Appointments:")
        for a in self.appointments.values():
            print(f"Appointment ID: {a.appointment_id}, Patient ID: {a.patient_id}, Staff ID: {a.staff_id}, Date: {a.appointment_date}")




hms = HospitalManagementSystem()


hms.add_patient


hms.add_staff('Dr. Alice', 'Doctor', '111-222-3333')
hms.add_staff('Nurse Bob', 'Nurse', '444-555-6666')


hms.schedule_appointment(1, 1, '2024-10-20')


hms.view_patients()
hms.view_staff()
hms.view_appointments()


hms.update_patient

hms.delete_patient()


hms.view_patients()
