hospital_data={}

def add_patient(name, age):
    hospital_data[name] = {'age': age, 'appointments': []}
    print(f"Added patient {name} with age {age} successfully.")

def add_doctor(name, specialty):
    if 'doctors' not in hospital_data:
        hospital_data['doctors'] = {}
        hospital_data['doctors'][name] = specialty
        print(f"Added doctor {name} with specialty {specialty} successfully.")

def schedule_appointment(patient_name, doctor_name, time):
    if patient_name in hospital_data and doctor_name in hospital_data['doctors']:
        hospital_data[patient_name]['appointments'].append((doctor_name, time))
        print(f"Scheduled appointment for {patient_name} with Dr. {doctor_name} at {time}.")
    else: print(f"Error: Patient or Doctor not found.")

def show_appointments(patient_name):
    if patient_name in hospital_data: patient_info = hospital_data[patient_name]
    print(f"Appointments for {patient_name}:")
    for appointment in patient_info['appointments']:
        print(f" Doctor: Dr. {appointment[0]}, Specialty: {hospital_data['doctors'][appointment[0]]}, Time: {appointment[1]}")
    else: print(f"Error: Patient {patient_name} not found.")

def main():
    while True:
        print("1. add_patient")
        print("2. add_doctor")
        print("3. appointment_schedule")
        print("4. show_appointment")
        print("5. EXIT")

        user_choice=int(input("Enter your choice 1-5: "))

        if user_choice==1:
            name= input("Enter Patient's Name: ")
            age= input("Enter patient's age: ")
            add_patient(name,age)
        elif user_choice == 2:
            doctor_name = input("Enter Doctor's Name: ")
            specialty = input("Enter Doctor's Specialty: ")
            add_doctor(doctor_name, specialty)
        elif user_choice == 3:
            patient_name = input("Enter Patient's Name: ")
            doctor_name = input("Enter Doctor's Name: ")
            time = input("Enter Appointment Time: ")
            schedule_appointment(patient_name, doctor_name, time)
        elif user_choice == 4:
            patient_name = input("Enter Patient's Name: ")

            show_appointments(patient_name)
        elif user_choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()

