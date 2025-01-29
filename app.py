import mysql.connector
import streamlit as st
import random


from datetime import datetime

# Database Handler Class
class DatabaseHandler:
    def __init__(self, host, user, passwd, database):
        self.connection = mysql.connector.connect(
            host="localhost",user="root",passwd="JOjo@154",database="Student_Record"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_data(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
class DBHandler:
    def __init__(self):
        # Initialize database connection
        pass

    def execute_query(self, query, params=None):
        print(f"Executing query: {query} with params: {params}")
        # Actual query execution logic


# Student Class
class Student:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_student(self, admn_no, name, class_, sec, per, dob, blood_group, phone_no):
        # Query to insert data
        query = """
        INSERT INTO Student_Details (Admn_No, S_name, Class, Sec, Per, DOB, Bloodgp, Phone_no)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (admn_no, name, class_, sec, per, dob, blood_group, phone_no)
        
        try:
            # Check for duplicate admission number
            check_query = "SELECT COUNT(*) FROM Student_Details WHERE Admn_No = %s"
            self.db_handler.cursor.execute(check_query, (admn_no,))
            exists = self.db_handler.cursor.fetchone()[0]
            
            if exists:
                st.warning("Student with this admission number already exists.")
                return

            # Execute the insertion
            self.db_handler.execute_query(query, data)
            st.success("Student added successfully!")
        except Exception as e:
            st.error(f"Failed to add student. Error: {e}")

    def search_student(self, admn_no):
        query = """
        SELECT * FROM Student_Details WHERE Admn_No = %s
        """
        return self.db_handler.fetch_data(query, (admn_no,))

    def delete_student(self, admn_no):
        query = "DELETE FROM Student_Details WHERE Admn_No = %s"
        self.db_handler.execute_query(query, (admn_no,))
        st.success("Student deleted successfully!")

# Parent Class
class Parent:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_parent(self, admn_no, parent_id, parent_name, contact, address):
        query = """
        INSERT INTO Parent_Details (Admn_No, P_ID, P_name, Contact_No, Address)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (admn_no, parent_id, parent_name, contact, address)
        self.db_handler.execute_query(query, data)
        st.success("Parent details added successfully!")

# Fee Class
class Fee:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_fee(self, admn_no, fee_type, fee_paid):
        query = """
        INSERT INTO Fee_Details (Admn_No, Fee_Type, FeePaid)
        VALUES (%s, %s, %s)
        """
        data = (admn_no, fee_type, fee_paid)
        self.db_handler.execute_query(query, data)
        st.success("Fee details added successfully!")

# Marks Class
class Marks:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def add_marks(self, admn_no, subject1, subject2, subject3):
        query = """
        INSERT INTO Marks (Admn_No, Subject1, Subject2, Subject3)
        VALUES (%s, %s, %s, %s)
        """
        data = (admn_no, subject1, subject2, subject3)
        self.db_handler.execute_query(query, data)
        st.success("Marks added successfully!")

# Streamlit UI
def main():
    st.title("RIVERDALE HIGH SCHOOL STUDENT RECORD SYSTEM")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Choose an action", ["Add Student", "Search Student", "Delete Student", "Add Parent", "Add Fee", "Add Marks"])

    # Initialize Database Handler
    db_handler = DatabaseHandler("localhost", "root", "JOjo@154", "Student_Record")
    student = Student(db_handler)
    parent = Parent(db_handler)
    fee = Fee(db_handler)
    marks = Marks(db_handler)

    if choice == "Add Student":
        st.header("Add New Student")
        admn_no = st.number_input("Admission Number", min_value=1)
        name = st.text_input("Student Name")
        class_ = st.text_input("Class")
        sec = st.text_input("Section")
        per = st.number_input("Percentage in Last Class", min_value=0, max_value=100)
        dob = st.date_input("Date of Birth")
        blood_group = st.text_input("Blood Group")
        phone_no = st.text_input("Phone Number")
        if st.button("Add Student"):
            student.add_student(admn_no, name, class_, sec, per, dob, blood_group, phone_no)

    elif choice == "Search Student":
        st.header("Search Student")
        admn_no = st.number_input("Enter Admission Number", min_value=1)
        if st.button("Search"):
            result = student.search_student(admn_no)
            if result:
                st.write(result)
            else:
                st.error("Student not found!")

    elif choice == "Delete Student":
        st.header("Delete Student")
        admn_no = st.number_input("Enter Admission Number to Delete", min_value=1)
        if st.button("Delete"):
            student.delete_student(admn_no)

    elif choice == "Add Parent":
        st.header("Add Parent Details")
        admn_no = st.number_input("Admission Number", min_value=1)
        parent_id = st.text_input("Parent ID")
        parent_name = st.text_input("Parent Name")
        contact = st.text_input("Contact Number")
        address = st.text_input("Address")
        if st.button("Add Parent"):
            parent.add_parent(admn_no, parent_id, parent_name, contact, address)

    elif choice == "Add Fee":
        st.header("Add Fee Details")
        admn_no = st.number_input("Admission Number", min_value=1)
        fee_type = st.selectbox("Fee Type", ["Quarterly", "Monthly", "Annually"])
        fee_paid = st.selectbox("Fee Paid", ["Y", "N"])
        if st.button("Add Fee"):
            fee.add_fee(admn_no, fee_type, fee_paid)

    elif choice == "Add Marks":
        st.header("Add Marks")
        admn_no = st.number_input("Admission Number", min_value=1)
        subject1 = st.number_input("Marks in Subject 1", min_value=0, max_value=100)
        subject2 = st.number_input("Marks in Subject 2", min_value=0, max_value=100)
        subject3 = st.number_input("Marks in Subject 3", min_value=0, max_value=100)
        if st.button("Add Marks"):
            marks.add_marks(admn_no, subject1, subject2, subject3)

    # Close the database connection
    db_handler.close()

if __name__ == "__main__":
    main()