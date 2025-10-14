import os
import csv

# Class Patient 
class Patient:
    def __init__(self, patient_id, name, age, weight, height, bp):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bp = bp  # (systolic, diastolic)

    def is_high_bp(self):
        systolic, diastolic = self.bp
        return systolic > 140 or diastolic > 90

    def calculate_bmi(self):
        if self.height <= 0:
            return None
        return self.weight / (self.height ** 2)

    def __str__(self):
        bmi = self.calculate_bmi()
        bmi_str = f"{bmi:.2f}" if bmi is not None else "N/A"
        return (f"Patient ID: {self.patient_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Weight: {self.weight} kg\n"
                f"Height: {self.height} m\n"
                f"Blood Pressure: {self.bp[0]}/{self.bp[1]} mmHg\n"
                f"BMI: {bmi_str}\n"
                f"High BP: {'Yes' if self.is_high_bp() else 'No'}")

# Class Clinic
class Clinic():
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def find_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None
    
    def find_patients_by_name(self, keyword):
        found_patients = []
        # Chuyển keyword về chữ thường để tìm kiếm không phân biệt hoa/thường
        search_term = keyword.lower()
        for patient in self.patients:
            if search_term in patient.name.lower():
                found_patients.append(patient)
        return found_patients
    
    def show_all_patients(self):
        if not self.patients:
            print("No patients in the clinic.")
        for patient in self.patients:
            print(patient)
            print("-" * 20)

    def show_high_bp_patients(self):
        high_bp_found = False
        print("High Blood Pressure Patients:")
        for patient in self.patients:
            if patient.is_high_bp():
                print(patient.bp[0], "/", patient.bp[1], " - ", patient.name)
                print("-" * 20)
                high_bp_found = True
        if not high_bp_found:
            print("No patients with high blood pressure.")

    def remove_patient(self, patient_id):
        patient = self.find_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False

    def save_to_file(self):
        try:
            with open("patients.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Patient ID", "Name", "Age", "Weight", "Height"
                                 , "Systolic BP", "Diastolic BP"])
                for patient in self.patients:
                    writer.writerow([patient.patient_id, patient.name, patient.age,
                                     patient.weight, patient.height,patient.bp[0], patient.bp[1]])
            print(f"Data saved to patients.csv")
        except IOError as e:
            print(f"Error saving file: {e}")

    def load_from_file(self ):       
        self.patients.clear()
        try:
            with open("patients.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    patient_id, name, age, weight, height, systolic, diastolic = row
                    patient = Patient(patient_id, name, int(age), float(weight), 
                                      float(height), (int(systolic), int(diastolic)))
                    self.add_patient(patient)
            print(f"Data loaded from patients.csv")
        except FileNotFoundError:
            print(f"No such file: patients.csv")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
            
    def sort_patients(self, key):
        if key == 'age':
            self.patients.sort(key=lambda patient: patient.age)
            print("Patients sorted by age.")
        elif key == 'bmi':
            self.patients.sort(key=lambda patient: patient.calculate_bmi() or 0)
            print("Patients sorted by BMI.")
        else:
            print("Invalid sort key.")

# Input validation functions
def intValidate(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

def floatValidate(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def StringValidate(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please enter a valid string.")
            continue
# 7. Create a new class Visit to manage Visit History concerning the data of visitors who visited patient.
class Visit:
    def __init__(self):
        self.visit_history = {}  
    # def add_visit(self, patient_id, visit_date, reason):
        
# 8. Create a new class to manage Clinic Staff and Role Management,
# regarding role based access (username, password) for Doctor, Receptionist, Admin
class Staff:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role # Doctor, Receptionist, Admin
    
class StaffManagement:
    def __init__(self):
        self.staff_list = []
    def add_staff(self, username, password, role):
        self.staff_list.append(Staff(username, password, role))
    def authenticate(self, username, password):
        for staff in self.staff_list:
            if staff.username == username and staff.password == password:
                return staff.role
        return None

# Main program
def main():
    clinic = Clinic()
    staff_management = StaffManagement()
    # hardcode nhân viên cho demo
    staff_management.add_staff("doctor1", "123456", "Doctor")
    staff_management.add_staff("receptionist1", "123456", "Receptionist")
    staff_management.add_staff("admin1", "123456", "Admin")
    staff_management.add_staff("huy", "huy", "Nurse")
    
    print("Welcome to the Clinic Management System")
    username = StringValidate("Enter your username: ")
    password = intValidate("Enter your password: ")
    role = staff_management.authenticate(username, password)
    # Kiểm tra quyền truy cập
    if role == "Doctor" or role == "Receptionist" or role == "Admin":
        print(f"Login successful! Welcome {role}.")
    elif role == "Nurse":
        print(f"You don't have permission to access the system.")
        return
    else:
        print("Login failed. Invalid username or password.")
        return
    
    while True:
        print("\n===== Clinic Management System =====")
        print("1. Add new patient")
        print("2. View all patients")
        print("3. Search patient")
        print("4. View patients with high blood pressure")
        print("5. Remove patient by ID")
        print("6. Save patients to file")
        print("7. Load patients from file")
        # print("8. Add Visit Record (Bonus)")
        # print("9. Visit History (Bonus)")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")


        if choice == "1":
            patient_id = StringValidate("Enter patient ID: ")
            name = StringValidate("Enter patient name: ")
            age = intValidate("Enter patient age: ")
            weight = floatValidate("Enter patient weight (kg): ")
            height = floatValidate("Enter patient height (m): ")
            systolic = intValidate("Enter systolic BP( normal < 120): ") # huyết áp tâm thu
            diastolic = intValidate("Enter diastolic BP( normal < 80): ") # huyết áp tâm trương
            bp = (systolic, diastolic)
            new_patient = Patient(patient_id, name, age, weight, height, bp)
            clinic.add_patient(new_patient)
            print("Patient added successfully.")
            
        elif choice == "2":
            clinic.show_all_patients()
            user_choice = StringValidate("Do you want to sort patients? (yes/no)")
            if user_choice.lower() == 'yes':
                sort_key = StringValidate("Enter sort key (age/bmi): ").lower()
                clinic.sort_patients(sort_key)
                clinic.show_all_patients()
        
        elif choice == "3":
            print("Search by:")
            print("1. Patient ID")
            print("2. Name keyword")
            search_option = StringValidate("Choose an option (1-2): ")
            if search_option == "1":
                search_id = StringValidate("Enter patient ID to search: ")
                patient = clinic.find_patient_by_id(search_id)
                if patient:
                    print(patient)
                else:
                    print("Patient not found.")
            elif search_option == "2":
                search_name = StringValidate("Enter name keyword to search: ")
                patients = clinic.find_patients_by_name(search_name)
                if patients:
                    for p in patients:
                        print(p)
                else:
                    print("No patients found.")
                    
        elif choice == "4":
            clinic.show_high_bp_patients()
            
        elif choice == "5":
            remove_id = StringValidate("Enter patient ID to remove: ")
            if clinic.remove_patient(remove_id):
                print("Patient removed successfully.")
            else:
                print("Patient not found.")
                
        elif choice == "6":
            clinic.save_to_file()
            print("Patients saved to file successfully.")
        elif choice == "7":
            clinic.load_from_file()
            print("Patients loaded from file successfully.")
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()