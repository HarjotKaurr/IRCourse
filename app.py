# import mysql.connector
# import streamlit as st
# import random


# from datetime import datetime

# # Database Handler Class
# class DatabaseHandler:
#     def __init__(self, host, user, passwd, database):
#         self.connection = mysql.connector.connect(
#             host="localhost",user="root",passwd="JOjo@154",database="Student_Record"
#         )
#         self.cursor = self.connection.cursor()

#     def execute_query(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         self.connection.commit()

#     def fetch_data(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         return self.cursor.fetchall()

#     def close(self):
#         self.cursor.close()
#         self.connection.close()
# class DBHandler:
#     def __init__(self):
#         # Initialize database connection
#         pass

#     def execute_query(self, query, params=None):
#         print(f"Executing query: {query} with params: {params}")
#         # Actual query execution logic


# # Student Class
# class Student:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_student(self, admn_no, name, class_, sec, per, dob, blood_group, phone_no):
#         # Query to insert data
#         query = """
#         INSERT INTO Student_Details (Admn_No, S_name, Class, Sec, Per, DOB, Bloodgp, Phone_no)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         data = (admn_no, name, class_, sec, per, dob, blood_group, phone_no)
        
#         try:
#             # Check for duplicate admission number
#             check_query = "SELECT COUNT(*) FROM Student_Details WHERE Admn_No = %s"
#             self.db_handler.cursor.execute(check_query, (admn_no,))
#             exists = self.db_handler.cursor.fetchone()[0]
            
#             if exists:
#                 st.warning("Student with this admission number already exists.")
#                 return

#             # Execute the insertion
#             self.db_handler.execute_query(query, data)
#             st.success("Student added successfully!")
#         except Exception as e:
#             st.error(f"Failed to add student. Error: {e}")

#     def search_student(self, admn_no):
#         query = """
#         SELECT * FROM Student_Details WHERE Admn_No = %s
#         """
#         return self.db_handler.fetch_data(query, (admn_no,))

#     def delete_student(self, admn_no):
#         query = "DELETE FROM Student_Details WHERE Admn_No = %s"
#         self.db_handler.execute_query(query, (admn_no,))
#         st.success("Student deleted successfully!")

# # Parent Class
# class Parent:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_parent(self, admn_no, parent_id, parent_name, contact, address):
#         query = """
#         INSERT INTO Parent_Details (Admn_No, P_ID, P_name, Contact_No, Address)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         data = (admn_no, parent_id, parent_name, contact, address)
#         self.db_handler.execute_query(query, data)
#         st.success("Parent details added successfully!")

# # Fee Class
# class Fee:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_fee(self, admn_no, fee_type, fee_paid):
#         query = """
#         INSERT INTO Fee_Details (Admn_No, Fee_Type, FeePaid)
#         VALUES (%s, %s, %s)
#         """
#         data = (admn_no, fee_type, fee_paid)
#         self.db_handler.execute_query(query, data)
#         st.success("Fee details added successfully!")

# # Marks Class
# class Marks:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_marks(self, admn_no, subject1, subject2, subject3):
#         query = """
#         INSERT INTO Marks (Admn_No, Subject1, Subject2, Subject3)
#         VALUES (%s, %s, %s, %s)
#         """
#         data = (admn_no, subject1, subject2, subject3)
#         self.db_handler.execute_query(query, data)
#         st.success("Marks added successfully!")

# # Streamlit UI
# # def main():
# #     st.title("RIVERDALE HIGH SCHOOL STUDENT RECORD SYSTEM")
# #     st.sidebar.title("Navigation")
# #     choice = st.sidebar.radio("Choose an action", ["Add Student", "Search Student", "Delete Student", "Add Parent", "Add Fee", "Add Marks"])

# #     # Initialize Database Handler
# #     db_handler = DatabaseHandler("localhost", "root", "JOjo@154", "Student_Record")
# #     student = Student(db_handler)
# #     parent = Parent(db_handler)
# #     fee = Fee(db_handler)
# #     marks = Marks(db_handler)

# #     if choice == "Add Student":
# #         st.header("Add New Student")
# #         admn_no = st.number_input("Admission Number", min_value=1)
# #         name = st.text_input("Student Name")
# #         class_ = st.text_input("Class")
# #         sec = st.text_input("Section")
# #         per = st.number_input("Percentage in Last Class", min_value=0, max_value=100)
# #         dob = st.date_input("Date of Birth")
# #         blood_group = st.text_input("Blood Group")
# #         phone_no = st.text_input("Phone Number")
# #         if st.button("Add Student"):
# #             student.add_student(admn_no, name, class_, sec, per, dob, blood_group, phone_no)

# #     elif choice == "Search Student":
# #         st.header("Search Student")
# #         admn_no = st.number_input("Enter Admission Number", min_value=1)
# #         if st.button("Search"):
# #             result = student.search_student(admn_no)
# #             if result:
# #                 st.write(result)
# #             else:
# #                 st.error("Student not found!")

# #     elif choice == "Delete Student":
# #         st.header("Delete Student")
# #         admn_no = st.number_input("Enter Admission Number to Delete", min_value=1)
# #         if st.button("Delete"):
# #             student.delete_student(admn_no)

# #     elif choice == "Add Parent":
# #         st.header("Add Parent Details")
# #         admn_no = st.number_input("Admission Number", min_value=1)
# #         parent_id = st.text_input("Parent ID")
# #         parent_name = st.text_input("Parent Name")
# #         contact = st.text_input("Contact Number")
# #         address = st.text_input("Address")
# #         if st.button("Add Parent"):
# #             parent.add_parent(admn_no, parent_id, parent_name, contact, address)

# #     elif choice == "Add Fee":
# #         st.header("Add Fee Details")
# #         admn_no = st.number_input("Admission Number", min_value=1)
# #         fee_type = st.selectbox("Fee Type", ["Quarterly", "Monthly", "Annually"])
# #         fee_paid = st.selectbox("Fee Paid", ["Y", "N"])
# #         if st.button("Add Fee"):
# #             fee.add_fee(admn_no, fee_type, fee_paid)

# #     elif choice == "Add Marks":
# #         st.header("Add Marks")
# #         admn_no = st.number_input("Admission Number", min_value=1)
# #         subject1 = st.number_input("Marks in Subject 1", min_value=0, max_value=100)
# #         subject2 = st.number_input("Marks in Subject 2", min_value=0, max_value=100)
# #         subject3 = st.number_input("Marks in Subject 3", min_value=0, max_value=100)
# #         if st.button("Add Marks"):
# #             marks.add_marks(admn_no, subject1, subject2, subject3)

# #     # Close the database connection
# #     db_handler.close()

# # if __name__ == "__main__":
# #     main()



# import mysql.connector
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set Streamlit page config
# st.set_page_config(page_title="Student Record System", page_icon="🏫", layout="wide")

# # Database Handler Class
# class DatabaseHandler:
#     def __init__(self, host, user, passwd, database):
#         self.connection = mysql.connector.connect(
#             host=host, user=user, passwd=passwd, database=database
#         )
#         self.cursor = self.connection.cursor()

#     def execute_query(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         self.connection.commit()

#     def fetch_data(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         return self.cursor.fetchall()

#     def close(self):
#         self.cursor.close()
#         self.connection.close()

# # Student Class
# class Student:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_student(self, admn_no, name, class_, sec, per, dob, blood_group, phone_no):
#         query = """
#         INSERT INTO Student_Details (Admn_No, S_name, Class, Sec, Per, DOB, Bloodgp, Phone_no)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         data = (admn_no, name, class_, sec, per, dob, blood_group, phone_no)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Student added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add student. Error: {e}")

#     def delete_student(self, admn_no):
#         try:
#             # First, delete dependent records from all related tables
#             self.db_handler.execute_query("DELETE FROM Fee_Details WHERE Admn_No = %s", (admn_no,))
#             self.db_handler.execute_query("DELETE FROM Parent_Details WHERE Admn_No = %s", (admn_no,))
#             self.db_handler.execute_query("DELETE FROM Marks WHERE Admn_No = %s", (admn_no,))

#             # Now, delete the student record
#             self.db_handler.execute_query("DELETE FROM Student_Details WHERE Admn_No = %s", (admn_no,))

#             st.success("✅ Student deleted successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to delete student. Error: {e}")


#     def search_student(self, admn_no):
#         query = "SELECT * FROM Student_Details WHERE Admn_No = %s"
#         result = self.db_handler.fetch_data(query, (admn_no,))
#         return result

# # Parent Class
# class Parent:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_parent(self, admn_no, parent_id, parent_name, contact, address):
#         query = """
#         INSERT INTO Parent_Details (Admn_No, P_ID, P_Name, contact_no, Address)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         data = (admn_no, parent_id, parent_name, contact, address)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Parent details added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add parent. Error: {e}")

# # Fee Class
# class Fee:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_fee(self, admn_no, fee_type, fee_paid):
#         query = """
#         INSERT INTO Fee_Details (Admn_No, Fee_Type, FeePaid)
#         VALUES (%s, %s, %s)
#         """
#         data = (admn_no, fee_type, fee_paid)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Fee details added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add fee. Error: {e}")

# # Marks Class
# class Marks:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_marks(self, admn_no, subject1, subject2, subject3):
#         query = """
#         INSERT INTO Marks (Admn_No, Subject1, Subject2, Subject3)
#         VALUES (%s, %s, %s, %s)
#         """
#         data = (admn_no, subject1, subject2, subject3)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Marks added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add marks. Error: {e}")

# # Sidebar Menu
# with st.sidebar:
#     selected = option_menu(
#         "Student Management",
#         ["🏠 Home", "📚 Add Student", "🔍 Search Student", "❌ Delete Student", "👨‍👩‍👦 Add Parent", "💰 Add Fee", "📊 Add Marks"],
#         icons=["house", "plus", "search", "trash", "users", "dollar-sign", "bar-chart"],
#         menu_icon="cast",
#         default_index=0
#     )

# # Initialize Database Handler
# db_handler = DatabaseHandler("localhost", "root", "JOjo@154", "Student_Record")
# student = Student(db_handler)
# parent = Parent(db_handler)
# fee = Fee(db_handler)
# marks = Marks(db_handler)

# # Home
# if selected == "🏠 Home":
#     st.title("🎓 Welcome to Riverdale High Student Records")
#     st.write("Use the sidebar to navigate through options.")

# # Add Student
# elif selected == "📚 Add Student":
#     st.title("📌 Add New Student")
#     with st.form("add_student_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             admn_no = st.number_input("📌 Admission Number", min_value=1)
#             name = st.text_input("📌 Student Name")
#             class_ = st.text_input("📌 Class")
#             sec = st.text_input("📌 Section")
#         with col2:
#             per = st.number_input("📌 Percentage in Last Class", min_value=0, max_value=100)
#             dob = st.date_input("📌 Date of Birth")
#             blood_group = st.text_input("📌 Blood Group")
#             phone_no = st.text_input("📌 Phone Number")
#         submit = st.form_submit_button("✅ Add Student")
#         if submit:
#             student.add_student(admn_no, name, class_, sec, per, dob, blood_group, phone_no)

# # Search Student
# elif selected == "🔍 Search Student":
#     st.title("🔍 Search Student Record")
#     admn_no = st.number_input("📌 Enter Admission Number", min_value=1)
#     search = st.button("🔍 Search")
#     if search:
#         result = student.search_student(admn_no)
#         if result:
#             st.success("🎉 Student Found!")
#             st.write(result)
#         else:
#             st.warning("❌ No record found!")

# # Delete Student
# elif selected == "❌ Delete Student":
#     st.title("🗑️ Delete Student Record")
#     admn_no = st.number_input("📌 Enter Admission Number", min_value=1)
#     delete = st.button("🗑️ Delete Student")
#     if delete:
#         student.delete_student(admn_no)

# # Add Parent
# elif selected == "👨‍👩‍👦 Add Parent":
#     st.title("👨‍👩‍👦 Add Parent Details")
#     with st.form("add_parent_form"):
#         admn_no = st.number_input("📌 Admission Number", min_value=1)
#         parent_id = st.text_input("📌 Parent ID")
#         parent_name = st.text_input("📌 Parent Name")
#         contact = st.text_input("📌 Contact Number")
#         address = st.text_input("📌 Address")
#         submit = st.form_submit_button("✅ Add Parent")
#         if submit:
#             parent.add_parent(admn_no, parent_id, parent_name, contact, address)

# # Add Fee
# elif selected == "💰 Add Fee":
#     st.title("💰 Add Fee Details")
#     admn_no = st.number_input("📌 Admission Number", min_value=1)
#     fee_type = st.selectbox("📌 Fee Type", ["Quarterly", "Monthly", "Annually"])
#     fee_paid = st.selectbox("📌 Fee Paid", ["Y", "N"])
#     submit = st.button("✅ Add Fee")
#     if submit:
#         fee.add_fee(admn_no, fee_type, fee_paid)

# # Add Marks
# elif selected == "📊 Add Marks":
#     st.title("📊 Add Marks")
#     admn_no = st.number_input("📌 Admission Number", min_value=1)
#     subject1 = st.number_input("📌 Marks in Subject 1", min_value=0, max_value=100)
#     subject2 = st.number_input("📌 Marks in Subject 2", min_value=0, max_value=100)
#     subject3 = st.number_input("📌 Marks in Subject 3", min_value=0, max_value=100)
#     submit = st.button("✅ Add Marks")
#     if submit:
#         marks.add_marks(admn_no, subject1, subject2, subject3)

# # Close the database connection
# db_handler.close()


# import mysql.connector
# import streamlit as st
# import pandas as pd
# from streamlit_option_menu import option_menu

# # Set Streamlit page config
# st.set_page_config(page_title="Student Record System", page_icon="🏫", layout="wide")

# # Database Handler Class
# class DatabaseHandler:
#     def __init__(self, host, user, passwd, database):
#         self.connection = mysql.connector.connect(
#             host=host, user=user, passwd=passwd, database=database
#         )
#         self.cursor = self.connection.cursor()

#     def execute_query(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         self.connection.commit()

#     def fetch_data(self, query, params=None):
#         self.cursor.execute(query, params or ())
#         return self.cursor.fetchall()

#     def close(self):
#         self.cursor.close()
#         self.connection.close()

# # Student Class
# class Student:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_student(self, admn_no, name, class_, sec, per, dob, blood_group, phone_no):
#         query = """
#         INSERT INTO Student_Details (Admn_No, S_name, Class, Sec, Per, DOB, Bloodgp, Phone_no)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         data = (admn_no, name, class_, sec, per, dob, blood_group, phone_no)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Student added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add student. Error: {e}")

#     def delete_student(self, admn_no):
#         try:
#             self.db_handler.execute_query("DELETE FROM Fee_Details WHERE Admn_No = %s", (admn_no,))
#             self.db_handler.execute_query("DELETE FROM Parent_Details WHERE Admn_No = %s", (admn_no,))
#             self.db_handler.execute_query("DELETE FROM Marks WHERE Admn_No = %s", (admn_no,))
#             self.db_handler.execute_query("DELETE FROM Student_Details WHERE Admn_No = %s", (admn_no,))

#             st.success("✅ Student deleted successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to delete student. Error: {e}")

#     def search_student(self, admn_no):
#         query = "SELECT * FROM Student_Details WHERE Admn_No = %s"
#         return self.db_handler.fetch_data(query, (admn_no,))

# # Parent Class
# class Parent:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_parent(self, admn_no, parent_id, parent_name, contact, address):
#         query = """
#         INSERT INTO Parent_Details (Admn_No, P_ID, P_Name, contact_no, Address)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         data = (admn_no, parent_id, parent_name, contact, address)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Parent details added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add parent. Error: {e}")

# # Fee Class
# class Fee:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_fee(self, admn_no, fee_type, fee_paid):
#         query = """
#         INSERT INTO Fee_Details (Admn_No, Fee_Type, FeePaid)
#         VALUES (%s, %s, %s)
#         """
#         data = (admn_no, fee_type, fee_paid)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Fee details added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add fee. Error: {e}")

# # Marks Class
# class Marks:
#     def __init__(self, db_handler):
#         self.db_handler = db_handler

#     def add_marks(self, admn_no, subject1, subject2, subject3):
#         query = """
#         INSERT INTO Marks (Admn_No, Subject1, Subject2, Subject3)
#         VALUES (%s, %s, %s, %s)
#         """
#         data = (admn_no, subject1, subject2, subject3)
#         try:
#             self.db_handler.execute_query(query, data)
#             st.success("✅ Marks added successfully!")
#         except Exception as e:
#             st.error(f"❌ Failed to add marks. Error: {e}")

# # Sidebar Menu
# with st.sidebar:
#     selected = option_menu(
#         "Student Management",
#         ["🏠 Home", "📚 Add Student", "🔍 Search Student", "❌ Delete Student", "👨‍👩‍👦 Add Parent", "💰 Add Fee", "📊 Add Marks"],
#         icons=["house", "plus", "search", "trash", "users", "dollar-sign", "bar-chart"],
#         menu_icon="cast",
#         default_index=0
#     )

# # Initialize Database Handler
# db_handler = DatabaseHandler("localhost", "root", "JOjo@154", "Student_Record")
# student = Student(db_handler)
# parent = Parent(db_handler)
# fee = Fee(db_handler)
# marks = Marks(db_handler)

# # Home Page (Displays Student Records)
# if selected == "🏠 Home":
#     st.title("🎓 Welcome to Riverdale High Student Records")
#     st.write("Use the sidebar to navigate through options.")

#     # Fetch all student records
#     query = "SELECT * FROM Student_Details"
#     student_records = db_handler.fetch_data(query)

#     # Display records in a table if data exists
#     if student_records:
#         st.subheader("📋 Student Records")
#         df = pd.DataFrame(student_records, columns=["Admn_No", "Name", "Class", "Sec", "Percentage", "DOB", "Blood Group", "Phone No"])
#         st.dataframe(df, use_container_width=True)
#     else:
#         st.warning("❌ No student records found!")

# # Add Student
# elif selected == "📚 Add Student":
#     st.title("📌 Add New Student")
#     with st.form("add_student_form"):
#         admn_no = st.number_input("📌 Admission Number", min_value=1)
#         name = st.text_input("📌 Student Name")
#         class_ = st.text_input("📌 Class")
#         sec = st.text_input("📌 Section")
#         per = st.number_input("📌 Percentage", min_value=0, max_value=100)
#         dob = st.date_input("📌 Date of Birth")
#         blood_group = st.text_input("📌 Blood Group")
#         phone_no = st.text_input("📌 Phone Number")
#         submit = st.form_submit_button("✅ Add Student")
#         if submit:
#             student.add_student(admn_no, name, class_, sec, per, dob, blood_group, phone_no)

# # Search Student
# elif selected == "🔍 Search Student":
#     st.title("🔍 Search Student Record")
#     admn_no = st.number_input("📌 Enter Admission Number", min_value=1)
#     search = st.button("🔍 Search")
#     if search:
#         result = student.search_student(admn_no)
#         if result:
#             st.success("🎉 Student Found!")
#             st.write(result)
#         else:
#             st.warning("❌ No record found!")

# # Delete Student
# elif selected == "❌ Delete Student":
#     st.title("🗑️ Delete Student Record")
#     admn_no = st.number_input("📌 Enter Admission Number", min_value=1)
#     delete = st.button("🗑️ Delete Student")
#     if delete:
#         student.delete_student(admn_no)

# # Close the database connection
# db_handler.close()


import mysql.connector
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Set Streamlit page config
st.set_page_config(page_title="Student Record System", page_icon="🏫", layout="wide")

# Database Handler Class
class DatabaseHandler:
    def __init__(self, host, user, passwd, database):
        self.connection = mysql.connector.connect(
            host=host, user=user, passwd=passwd, database=database
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

# Initialize Database Handler
db_handler = DatabaseHandler("localhost", "root", "JOjo@154", "Student_Record")

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        "Student Management",
        ["🏠 Home", "📚 Add Student", "🔍 Search Student", "❌ Delete Student"],
        icons=["house", "plus", "search", "trash"],
        menu_icon="cast",
        default_index=0
    )

# **🏠 Home Page: Display All Student Data**
if selected == "🏠 Home":
    st.title("🎓 Welcome to Riverdale High Student Records")

    # Fetch all student records
    query = "SELECT * FROM Student_Details"
    student_records = db_handler.fetch_data(query)

    # Display records in a table if data exists
    if student_records:
        st.subheader("📋 Student Details")
        df_students = pd.DataFrame(
            student_records, 
            columns=["Admn_No", "Name", "Class", "Sec", "Percentage", "DOB", "Blood Group", "Phone No"]
        )
        df_students["Admn_No"] = df_students["Admn_No"].astype(str)  # Remove commas
        df_students["Phone No"] = df_students["Phone No"].astype(str)  # Remove commas
        st.dataframe(df_students, use_container_width=True)

        # Fetch Parent Details
        st.subheader("👨‍👩‍👦 Parent Details")
        parent_records = db_handler.fetch_data("SELECT * FROM Parent_Details")
        if parent_records:
            df_parents = pd.DataFrame(
                parent_records, 
                columns=["Admn_No", "P_ID", "Parent Name", "Contact No", "Address"]
            )
            df_parents["Admn_No"] = df_parents["Admn_No"].astype(str)  # Remove commas
            df_parents["Contact No"] = df_parents["Contact No"].astype(str)  # Remove commas
            st.dataframe(df_parents, use_container_width=True)
        else:
            st.warning("❌ No parent records found!")

        # Fetch Fee Details
        st.subheader("💰 Fee Details")
        fee_records = db_handler.fetch_data("SELECT * FROM Fee_Details")
        if fee_records:
            df_fees = pd.DataFrame(
                fee_records, 
                columns=["Admn_No", "Fee Type", "Fee Paid"]
            )
            df_fees["Admn_No"] = df_fees["Admn_No"].astype(str)  # Remove commas
            st.dataframe(df_fees, use_container_width=True)
        else:
            st.warning("❌ No fee records found!")

        # Fetch Marks Details
        st.subheader("📊 Marks Details")
        marks_records = db_handler.fetch_data("SELECT * FROM Marks")
        if marks_records:
            df_marks = pd.DataFrame(
                marks_records, 
                columns=["Admn_No", "Subject1", "Subject2", "Subject3"]
            )
            df_marks["Admn_No"] = df_marks["Admn_No"].astype(str)  # Remove commas
            st.dataframe(df_marks, use_container_width=True)
        else:
            st.warning("❌ No marks records found!")
    else:
        st.warning("❌ No student records found!")

# **📚 Add Student**
elif selected == "📚 Add Student":
    st.title("📌 Add New Student")
    with st.form("add_student_form"):
        admn_no = st.text_input("📌 Admission Number")  # Text to avoid commas
        name = st.text_input("📌 Student Name")
        class_ = st.text_input("📌 Class")
        sec = st.text_input("📌 Section")
        per = st.number_input("📌 Percentage", min_value=0, max_value=100)
        dob = st.date_input("📌 Date of Birth")
        blood_group = st.text_input("📌 Blood Group")
        phone_no = st.text_input("📌 Phone Number")  # Text to avoid commas
        submit = st.form_submit_button("✅ Add Student")

        if submit:
            query = """
            INSERT INTO Student_Details (Admn_No, S_name, Class, Sec, Per, DOB, Bloodgp, Phone_no)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (admn_no, name, class_, sec, per, dob, blood_group, phone_no)
            try:
                db_handler.execute_query(query, data)
                st.success("✅ Student added successfully!")
            except Exception as e:
                st.error(f"❌ Failed to add student. Error: {e}")

# **🔍 Search Student**
elif selected == "🔍 Search Student":
    st.title("🔍 Search Student Record")
    admn_no = st.text_input("📌 Enter Admission Number")  # Text to avoid commas
    search = st.button("🔍 Search")

    if search:
        query = "SELECT * FROM Student_Details WHERE Admn_No = %s"
        result = db_handler.fetch_data(query, (admn_no,))
        
        if result:
            st.success("🎉 Student Found!")
            df = pd.DataFrame(
                result, 
                columns=["Admn_No", "Name", "Class", "Sec", "Percentage", "DOB", "Blood Group", "Phone No"]
            )
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("❌ No record found!")

# **❌ Delete Student**
elif selected == "❌ Delete Student":
    st.title("🗑️ Delete Student Record")
    admn_no = st.text_input("📌 Enter Admission Number")  # Text to avoid commas
    delete = st.button("🗑️ Delete Student")

    if delete:
        try:
            db_handler.execute_query("DELETE FROM Fee_Details WHERE Admn_No = %s", (admn_no,))
            db_handler.execute_query("DELETE FROM Parent_Details WHERE Admn_No = %s", (admn_no,))
            db_handler.execute_query("DELETE FROM Marks WHERE Admn_No = %s", (admn_no,))
            db_handler.execute_query("DELETE FROM Student_Details WHERE Admn_No = %s", (admn_no,))
            st.success("✅ Student deleted successfully!")
        except Exception as e:
            st.error(f"❌ Failed to delete student. Error: {e}")

# Close the database connection
db_handler.close()
