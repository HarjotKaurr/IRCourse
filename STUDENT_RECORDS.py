# print("*                                                                  *")
# print("*                           RIVERDALE HIGH                         *")
# print("*                                                                  *")
# print("*                     WELCOME TO STUDENT RECORD                    *")
# print("*                                                                  *")
# print("********************************************************************")

# import mysql.connector
# import datetime 
# import random
# mycon=mysql.connector.connect(host="localhost",user="root",passwd="JOjo@154",database="Student_Record")
# if mycon.is_connected()==True:
#         print("SUCCESSFULLY CONNECTED")

# c=mycon.cursor()
# count=3
# while count > 0:
#     count = count-1
#     password=input("\nENTER THE PASSWORD FOR PRIVACY CONCERNS: ")
#     if password=="!@#123":
#             print("ACCESS GRANTED")
           
#             def add():
#                 while True:
#                             print("\n*ADD Record for new admission*")
#                             print("\nCHOOSE WHAT TO ADD FROM BELOW: ")
#                             print(" 1. ADD STUDENT RECORD")
#                             print(" 2. ADD PARENT RECORD")
#                             print(" 3. ADD FEE RECORD")
#                             print(" 4. ADD MARKS RECORD")  
#                             print(" 5. QUIT ")
#                             f=int(input("\nTYPE THE NO.: "))
#                             global c
#                             if f==1:
#                                     n=int(input("\nEnter Admn number: "))
#                                     m=input("Enter Student Name: ")
#                                     r=(input("Enter Class: "))
#                                     p=input("Enter Sec: ")
#                                     q=int(input("Enter Percentage in last class: "))
#                                     s=input("Enter Date Of Birth: ")
#                                     t=input("Enter Blood Group: ")
#                                     u=int(input("Enter Phone number: "))
#                                     data=(n,m,r,p,q,s,t,u)
#                                     l=tuple(data)
#                                     sql='insert into Student_Details values(%s,%s,%s,%s,%s,%s,%s,%s)'
#                                     c.execute(sql,data)
#                                     mycon.commit()
#                                     print("\n*DATA ENTERED SUCCESSFULLY *")
                                    
#                             elif f==2:
#                                     a=int(input("\nEnter admn number: "))
#                                     k=input("Enter Parent ID: ")
#                                     b=input("Enter Parent Name: ")
#                                     d=int(input("Parent contact: "))
#                                     v=input("Address: ")
#                                     data=(a,k,b,d,v)
#                                     l=tuple(data)
#                                     print(l)
#                                     sql='insert into Parent_Details values(%s,%s,%s,%s,%s)'
#                                     c.execute("sql,data")
#                                     mycon.commit()
#                                     print("*DATA ENTERED SUCCESSFULLY *")

#                             elif f==3:
#                                     a=int(input("\nEnter admn number: "))
#                                     k=input("Enter Fee Type(Quarterly,Monthly,Annually): ")
#                                     b=input("Fee Paid(Y,N): ")
#                                     data=(a,k,b)
#                                     l=tuple(data)
#                                     print(l)
#                                     sql='insert into Fee_Details values(%s,%s,%s)'
#                                     c.execute(sql,data)
#                                     mycon.commit()
#                                     print("*DATA ENTERED SUCCESSFULLY *")
                                    
#                             elif f==4:
#                                     a=int(input("\nEnter admn number: "))
#                                     k=input("Marks in subject 1: ")
#                                     b=input("Marks in subject 2: ")
#                                     d=input("Marks in subject 3: ")
#                                     data=(a,k,b,d)
#                                     l=tuple(data)
#                                     print(l)
#                                     sql='insert Marks values(%s,%s,%s,%s)'
#                                     c.execute(sql,data)
#                                     mycon.commit()
#                                     print("*DATA ENTERED SUCCESSFULLY *")
                                    
#                             elif f==5:
#                                     print("ByeBye!DATA HAS BEEN STORED")
#                                     break
#                             else :
#                                     print("ERROR:INVALID CHOICE")
            
#             def sr():
#                     print("\n*SEARCH student record*")
#                     a=int(input("\nEnter Admn No. of the student : "))
#                     c=mycon.cursor()
#                     c.execute("select * from Student_Details S,Parent_Details P where S.Admn_No=P.Admn_No and P.Admn_no=%s"%(a,))
#                     data=c.fetchall()
#                     if c.rowcount==0:
#                             print("\nADMN NO. NOT FOUND.")
#                     else:
#                             print('\n',data)
                    
#             def dela():
#                 print("\n*DELETE all records of a particular student*")
#                 a=int(input("\nAdmn no of student whose record you want to delete: "))
#                 c.execute("delete from Marks where Admn_no=%s"%(a,))
#                 c.execute("delete from fee_Details where Admn_No=%s"%(a,))
#                 c.execute("delete from parent_details where Admn_no=%s"%(a,))
#                 c.execute("delete from Student_details where Admn_no=%s"%(a,))
#                 z=c.fetchone ()
#                 if c.rowcount==0:
#                         print("\nADMN NO. NOT FOUND.")
#                 else:
#                         print("\nDELETED SUCCESSFULLY")
#                 mycon.commit()

#             def update():
#                      print("\n*UPDATE the details of the student*")
#                      while True:
#                              print("\nCHOOSE THE TABLE YOU WANT TO UPDATE: ")
#                              print(" 1. UPDATE STUDENT_DETAILS")
#                              print(" 2. UPDATE PARENT_DETAILS")
#                              print(" 3. UPDATE FEE_DETAILS")
#                              print(" 4. UPDATE MARKS RECORD")
#                              print(" 5. QUIT")
#                              s=int(input('\n'))
#                              if s==1:
#                                     a=input ("ENTER THE ADMN_NO OF THE STUDENT WHOSE REC WE HAVE TO UPDATE: ")
#                                     print ("CHOOSE FROM BELOW: ")
#                                     print (" 1. UPDATE Name")
#                                     print (" 2. UPDATE Per")
#                                     print (" 3. UPDATE Sec")
#                                     print (" 4. UPDATE class")
#                                     print (" 5. UPDATE DOB")
#                                     print (" 6. UPDATE PHONE NUMBER")
#                                     print (" 7. UPDATE BLOODGRP")
#                                     ch=int(input ("WHAT TO UPDATE: "))
#                                     if ch==1:
#                                             n=str(input("Enter the updated S_name: "))
#                                             c.execute("update Student_Details set S_name='%s' where Admn_No=%s"%(n,a))
#                                             c.execute("select* from Student_Details where Admn_No=%s"% (a,))
#                                             x=c.fetchone()
#                                             if x is None:
#                                                     print("No Record")
#                                             else:
#                                                     print("DONE")
#                                                     print(x)
#                                                     mycon.commit()
#                                     elif ch==2:
#                                             per=int(input("enter the updated Per: "))
#                                             c.execute("update Student_Details set Per=%s where Admn_No=%s"% (per,a))
#                                             c.execute("select*from Student_Details where Admn_No=%s"% (a,))
#                                             y=c.fetchone()
#                                             if y is None:
#                                                     print("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(y)
#                                                     mycon.commit()
#                                     elif ch==3:
#                                             Sec=input("enter the updated Sec: ")
#                                             c.execute("update student_Details set Sec='%s' where Admn_No=%s"%(Sec,a))
#                                             c.execute("select* from student_Details where Admn_No=%s"% (a, ))
#                                             z=c.fetchone()
#                                             if z is None:
#                                                     print("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(z)
#                                                     mycon.commit()
#                                     elif ch==4:
#                                             classs=input("enter the updated Class: ")
#                                             c.execute("update student_Details set Class=%s where Admn_No=%s"%(classs,a))
#                                             c.execute("select*from student_Details where Admn_No=%s"% (a, ))#enter class in strings
#                                             q=c.fetchone()
#                                             if q is None:
#                                                     print("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(q)
#                                                     mycon.commit()
#                                     elif ch==5:
#                                             DOB=input("enter the updated DOB: ")
#                                             c.execute("update student_Details set DOB=%s where Admn_No=%s"%(DOB,a))
#                                             c.execute("select* from student_Details where Admn_No=%s"% (a, ))#enter DOB in strings
#                                             p=c.fetchone()
#                                             if p is None:
#                                                     print("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(p)
#                                                     mycon.commit()
#                                     elif ch==6:
#                                             Phone_no=input("enter the updated Phone_no: ")
#                                             c.execute("update Student_Details set Phone_no=%s where Admn_No=%s"%(Phone_no ,a))
#                                             c.execute("select* from student_Details where Admn_No=%s"% (a, ))
#                                             r=c.fetchone()
#                                             if r is None:
#                                                     print ("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(r)
#                                                     mycon.commit()
#                                     elif ch==7:
#                                             Bloodgp=input("enter the updated Bloodgp: ")
#                                             c.execute("update student_Details set Bloodgp='%s' where Admn_No=%s"%(Bloodgp,a))
#                                             c.execute("select* from student_Details where Admn_No=%s"%(a, ))
#                                             o=c.fetchone()
#                                             if o is None:
#                                                     print("no record")
#                                             else:
#                                                     print("DONE")
#                                                     print(o)
#                                                     mycon.commit()
#                              elif s==2:
#                                      a=input ("ENTER THE P_ID OF THE STUDENT WHOSE REC WE HAVE TO UPDATE: ")
#                                      print ("CHOOSE FROM BELOW: ")
#                                      print (" 1. UPDATE P_name")
#                                      print (" 2. UPDATE Contact_No")
#                                      print (" 3. UPDATE Address")
#                                      ch=int(input ("WHAT TO UPDATE: "))
#                                      if ch==1:
#                                              n=str(input("Enter the updated P_name: "))
#                                              c.execute("update Parent_Details set P_name='%s' where P_ID='%s'"%(n,a))
#                                              c.execute("select* from Parent_Details where P_ID='%s'"% (a,))
#                                              x=c.fetchone()
#                                              if x is None:
#                                                      print("No Record")
#                                              else:
#                                                      print("DONE")
#                                                      print(x)
#                                                      mycon.commit()
#                                      elif ch==2:
#                                              con=int(input("enter the updated Contact_No: "))
#                                              c.execute("update Parent_Details set Contact_No=%s where P_ID='%s'"% (con,a))
#                                              c.execute("select*from Parent_Details where P_ID='%s'"% (a,))
#                                              y=c.fetchone()
#                                              if y is None:
#                                                      print("no record")
#                                              else:
#                                                      print("DONE")
#                                                      print(y)
#                                                      mycon.commit()
#                                      elif ch==3:
#                                              aas=str(input("Enter the updated Address: "))
#                                              c.execute("update Parent_Details set Address='%s' where P_ID='%s'"%(aas,a))
#                                              c.execute("select* from Parent_Details where P_ID='%s'"% (a,))
#                                              x=c.fetchone()
#                                              if x is None:
#                                                      print("No Record")
#                                              else:
#                                                      print("DONE")
#                                                      print(x)
#                                                      mycon.commit()
#                              elif s==3:
#                                 a=input ("ENTER THE admn no OF THE STUDENT WHOSE REC WE HAVE TO UPDATE: ")
#                                 print ("CHOOSE FROM BELOW: ")
#                                 print ("1. UPDATE Fee_Type")
#                                 print ("2. UPDATE FeePaid")
#                                 ch=int(input("WHAT TO UPDATE: "))
#                                 if ch==1:
#                                         n=str(input("Enter the updated Fee_Type: "))
#                                         c.execute("update Fee_Details set Fee_Type='%s' where Admn_no=%s"%(n,a))
#                                         c.execute("select* from Fee_Details where Fee_Type='%s'"% (a,))
#                                         x=len(c.fetchall())
#                                         i=c.fetchall()
#                                         if i is None:
#                                                 print("No Record")
#                                         else:
#                                                 print("DONE")
#                                                 for j in range(0,x):
#                                                         print(i[j])
#                                                 mycon.commit()
#                                 elif ch==2:
#                                         con=input("enter the Fee paid(Y/N): ")
#                                         c.execute("update Fee_Details set FeePaid='%s' where Admn_no=%s"% (con,a))
#                                         c.execute("select*from Fee_Details where FeePaid='%s'"% (con,))
#                                         y=c.fetchall()
#                                         if y is None:
#                                                 print("No Record")
#                                         else:
#                                                 print("DONE")
#                                                 c.execute("select* from fee_details where Admn_no=%s"%(a,))
#                                                 m=c.fetchone()
#                                                 print(m)
#                                                 mycon.commit() 
#                              elif s==4:
#                                      a=input ("ENTER THE Admn_no OF THE STUDENT WHOSE MARKS WE HAVE TO UPDATE: ")
#                                      print ("CHOOSE FROM BELOW: ")
#                                      print (" 1. UPDATE Marks in subject1")
#                                      print (" 2. UPDATE Marks in subject2")
#                                      print (" 3. UPDATE Marks in subject3")
#                                      ch=int(input ("WHAT TO UPDATE: "))
#                                      if ch==1:
#                                              n=int(input("Enter the updated Marks of subject 1: "))
#                                              c.execute("update Marks set Subject1='%s' where Admn_no=%s"%(n,a))
#                                              c.execute("select* from MARKS where Admn_no=%s"% (a,))
#                                              x=c.fetchone()
#                                              if x is None:
#                                                      print("No Record")
#                                              else:
#                                                      print("DONE")
#                                                      print(x)
#                                                      mycon.commit()
#                                      elif ch==2:
#                                              n=int(input("Enter the updated Marks of subject 2: "))
#                                              c.execute("update Marks set Subject2='%s' where Admn_no=%s"%(n,a))
#                                              c.execute("select* from MARKS where Admn_no=%s"% (a,))
#                                              x=c.fetchone()
#                                              if x is None:
#                                                      print("No Record")
#                                              else:
#                                                      print("DONE")
#                                                      print(x)
#                                                      mycon.commit()
#                                      elif ch==3:
#                                              n=int(input("Enter the updated Marks of subject 3: "))
#                                              c.execute("update Marks set Subject3='%s' where Admn_no=%s"%(n,a))
#                                              c.execute("select* from MARKS where Admn_no=%s"% (a,))
#                                              x=c.fetchone()
#                                              if x is None:
#                                                      print("No Record")
#                                              else:
#                                                      print("DONE")
#                                                      print(x)
#                                                      mycon.commit() 
                                    
#                              elif s==5:
#                                      break
            
#             #students ranging between (menu driven) 1. dob's 2.percentage 3.class
#             def rang():
#                 print("\n*Students RANGING between 2 limits*")
#                 while True:                
#                     print("\n1. FIND STUDENTS RANGING BETWEEN TWO DOB's ")
#                     print("2. FIND STUDENTS RANGING BETWEEN TWO percentages ")
#                     print("3. FIND STUDENTS RANGING BETWEEN TWO CLASSES ")
#                     print("4. Quit ")
#                     x=int(input('\n'))
#                     global c
#                     if x==1:
#                         s=int(input("\nENTER THE UPPER LIMIT OF YEAR: "))
#                         p=int(input("ENTER THE UPPER LIMIT OF MONTH: "))
#                         q=int(input("ENTER THE UPPER LIMIT OF DATE: "))
#                         T=datetime.date(s,p,q)
#                         e=int(input("\nENTER THE LOWER LIMIT OF YEAR: "))
#                         f=int(input("ENTER THE LOWER LIMIT OF MONTH: "))
#                         t=int(input("ENTER THE LOWER LIMIT OF DATE: "))
#                         K=datetime.date(e,f,t)
#                         c.execute("select Admn_No, S_name,Class,Sec from student_details where DOB>='{}' and DOB<='{}'".format(K,T))
#                         d=c.fetchall()
#                         print("\n")
#                         for i in d:
#                             print(i)
#                     elif x==2:
#                         e=int(input("\nENTER THE UPPER LIMIT OF PERCENTAGE: "))
#                         f=int(input("ENTER THE LOWER LIMIT OF PERCENTAGE: "))
#                         c.execute("select Admn_No, S_name,Class,Sec from student_details where Per>={} and Per<={}".format(f,e))
#                         l=len(c.fetchall())
#                         c.execute("select Admn_No, S_name,Class,Sec from student_details where Per>={} and Per<={}".format(f,e))
#                         print("TOTAL RECORD FETCHED ARE: ",l)
#                         d=c.fetchall()
#                         print("\n")
#                         for i in d:
#                             print(i)
#                     elif x==3:
#                         e=input("\nENTER THE UPPER LIMIT OF CLASS: ")
#                         f=input("ENTER THE LOWER LIMIT OF CLASS: ")
#                         c.execute("select Admn_No, S_name,Class,Sec from student_details where Class>='{}' and Class<='{}'".format(f,e))
#                         l=len(c.fetchall())
#                         c.execute("select Admn_No, S_name,Class,Sec from student_details where Class>='{}' and Class<='{}'".format(f,e))
#                         print("\nTOTAL RECORD FETCHED ARE: ",l)
#                         d=c.fetchall()
#                         print("\n")
#                         for i in d:
#                             print(i)
#                     elif x==4:
#                         print("Bye Bye! Have A Good Day")
#                         break
#             #ELIGIBLE FOR SCHOLARSHIP (GREATER THAN 95%)
#             def scholarship():
#                     print("\n*Students Eligible for SCHOLORSHIP*")
#                     c.execute("select Admn_No, S_name,Sec,Per from student_details where Per>95 and Class='XII'")
#                     l=len(c.fetchall())
#                     c.execute("select Admn_No, S_name,Sec,Per from student_details where Per>95 and class='XII'")
#                     print("\nStudents Eligible For 1st level Scholarship are :",l)
#                     d=c.fetchall()
#                     for i in d:
#                             print(i)
#                     c.execute("select Admn_No, S_name,Sec,Per from student_details where class='XI' and Per between '95' and '99' ")
#                     G=len(c.fetchall())
#                     c.execute("select Admn_No, S_name,Sec,Per from student_details where class='XI' and Per between '95' and '99' ")
#                     print("\nStudents Eligible For 2nd level Scholarship are :",G)
#                     d=c.fetchall()
#                     for i in d:
#                             print(i)
#             def check():
#                     print("\n*CHECK whether the student is from the school or not.*")
#                     flag = True
#                     while flag == True:
#                             k=input("\nName of the student to be checked: ")
#                             c.execute("select S_name,Class,Sec from student_details where S_name='%s'"% (k, ))
#                             mydata=c.fetchone()
#                             if mydata is None:
#                                      print("\nNO,",(k),"is not from this school.")
#                                      flag = False
#                             elif mydata!=k:
#                                     print("\nYES",mydata[0],"is from this school, his details are",mydata)      
#                                     flag = False 
#                             else:
#                                     break       

#             def report():
#                     print("\n*Distribution of REMARKS and CLUB names*")
#                     while True:
#                             print("\nChoose what to randomize:-")
#                             print("1. Report Card Remarks ")
#                             print("2. Club Name")
#                             print("3. Quit ")
#                             g=int(input("\n"))
#                             global c
#                             if g==1:
#                                     a=int(input("\nEnter admn number of student whose report card remarks you want to see: "))
#                                     b=c.execute("select S_name from student_details where Admn_No=%s"% a)
#                                     mydata=c.fetchone()
#                                     Quotes=["is a conscientious and hard working student.","Has continued to make steady progress.",
#                                             "cooperates consistently with the teachers and other students.",
#                                             "is kind and helpful to everyone in the classroom.",
#                                             "is honest and trustworthy in dealings with others.",
#                                             "is concerned about the feelings of peers.",
#                                             "takes an active role in discussions.",
#                                             "tackles new challenges with a positive attitude.",
#                                             "is learning to be cooperative when working in groups."]
#                                     value=random.choice(Quotes)
#                                     for i in mydata:
#                                             print('\n',mydata[0], value)
#                             elif g==2:
#                                     a=int(input("\nEnter admn number of student whom you want to assign a club: "))
#                                     b=c.execute("select S_name from student_details where Admn_No=%s"% a)
#                                     mydata=c.fetchone()
#                                     Names=["Clever Clowns-They are Smart,but likes to clown around.",
#                                            "Perfect Pirates-Arrrr, They're a perfect bunch!",
#                                            "The Immortals-They're a group worthy of a superhero slogan.",
#                                            "The Incredibles-They've each got their own special skills.",
#                                            "Industrious Irises-They works hard!",
#                                            "Talented Turtles,Dude!-they are talented but also a chill bunch of dudes",
#                                            "Tenacious Tigers-They're fierce and unyielding",
#                                            "The Loyal Leopards-It's a group who will stick together to the end"]
#                                     value=random.choice(Names)
#                                     for i in mydata:
#                                             print('\n',mydata[0]," has been allotted to", value)
#                             else:
#                                     print("Bye Bye! Have A Good Day")
#                                     break
#             def order():
#                     print("\n*See the details by ASEC and DESC order*")
#                     while True:
#                             print("\nCHOOSE")
#                             print("1. SHOW NAMES IN ASCENDING ORDER ")
#                             print("2. SHOW CLASSES IN ASCENDING ORDER ")
#                             print("3. SHOW PERCENTAGE IN ASCENDING ORDER ")
#                             print("4. SHOW CLASSES IN DESCENDING ORDER ")
#                             print("5. QUIT")
#                             ch=int(input ("\nWHAT TO UPDATE: "))
#                             if ch==1:
#                                     query="select S_name from student_details order by S_name"
#                                     c.execute(query)
#                                     d=c.fetchall()
#                                     for i in d:
#                                             print(i)
#                             elif ch==2:
#                                     query="select S_name,Class from student_details order by Class"
#                                     c.execute(query)
#                                     d=c.fetchall()
#                                     for i in d:
#                                             print(i)
#                             elif ch==3:
#                                     query="select S_name,Class,Per from student_details order by Per"
#                                     c.execute(query)
#                                     d=c.fetchall()
#                                     for i in d:
#                                             print(i)
#                             elif ch==4:
#                                     query="select S_name,Class from student_details order by Class desc"
#                                     c.execute(query)
#                                     d=c.fetchall()
#                                     for i in d:
#                                             print(i)
#                             elif ch==5:
#                                     print("\nBye Bye! Have A Good Day")
#                                     break
#                             else:
#                                     print("\nINVALID CHOICE")

#             def passorfail():
#                     print("\n*Check if the student has PASSED or FAILED*")
#                     a=int(input("\nEnter Admn No:"))
#                     c.execute("select S_name from student_details where Admn_no=%s"%(a ))
#                     l=c.fetchall()
#                     if c.rowcount==1:
#                                 c.execute("select S_name from student_details where Per<40 and Admn_no='{}%'".format(a))
#                                 if c.rowcount==1:
#                                         l=c.fetchall()
#                                         print("\nYou have FAILED this year, NEED TO WORK HARD!!!")  
#                                 else:
#                                     print('\n',l[0]," You have PASSED AND PROMOTED")
#                     else:
#                         print("\nSORRY!! WRONG ADMN NO. ")
                                
#             def board():
#                     print("\nStudent giving BOARD EXAMS this year are:-")
#                     c.execute("select S_name,class from Student_details where class='X' or class='XII'")
#                     l=c.fetchall()
#                     for i in l:
#                         print(i)
            
#             def vaccination():
#                     print("\nStudents eligible for vaccination:-")
#                     c.execute("select s_name, class, DOB, Phone_no from student_Details where DOB<'2007-01-01'")
#                     l=c.fetchall()
#                     for i in l:
#                         print(i)

#             def markfee():
#                     print("\n*Search the MARK and FEE details of the student*")
#                     flag = True
#                     while flag == True:
#                             print("\nCHOOSE")
#                             print(" 1. MARK details of the student. ")
#                             print(" 2. FEE details of the student. ")
#                             print(" 3. Quit.")
#                             ch=int(input('\nYour Choice: '))
#                             if ch==1:
#                                     a=int(input("\nEnter Admn No. of the student : "))
#                                     c=mycon.cursor()
#                                     c.execute("select * from Marks where Admn_no=%s"%(a,))
#                                     mydata=c.fetchall()
#                                     if c.rowcount==0:
#                                             print("Admn no. not found")
#                                     else:
#                                             print('\n',mydata)
#                             elif ch==2:
#                                     a=int(input("\nEnter Admn No. of the student : "))
#                                     c=mycon.cursor()
#                                     c.execute("select*from Fee_Details where Admn_no=%s"%(a,))
#                                     mydata=c.fetchall()
#                                     if c.rowcount==0:
#                                             print("Admn no. not found")
#                                     else:
#                                             print('\n',mydata)
#                                             flag = False                    
#                             elif ch==3:
#                                     break
#                             else:
#                                     print("INVALID CHOICE \n")
                                    

#             def totavg():
#                     flag = True
#                     while flag == True:
#                             print('\nTOTAL and AVERAGE marks of the student\n')
#                             print(" 1. Total marks of the students.")
#                             print(" 2. Average marks of the student.")
#                             print(" 3. Quit.\n")
#                             ch=int(input('Your Choice: '))
#                             if ch in [1, 2] :
#                                     a=int(input("\nEnter Admn No. of the student : "))
#                                     c=mycon.cursor()
#                                     c.execute("select subject1, subject2, subject3 from marks where Admn_no=%s"%(a,))
#                                     t = c.fetchall()
#                                     total = list(t[0])
#                                     total = sum(list(map(int, total)))     
#                             if ch  != 3:
#                                     if ch==1:
#                                             print("\nMarks:", total, "\nTotal Marks:", total, "\n")
#                                     elif ch==2:
#                                             print("\nMarks:", total, "\nAverage Marks:", total/3, "\n")
#                                     else:
#                                             print("\nINVALID CHOICE, TRY AGAIN!!!")
#                             elif ch == 3:
#                                     break
#             def alpha():
#                     flag = True
#                     while flag == True:
#                             print("\n*Check the STUDENT RECORD of the names starting with USER'S LETTER CHOICE*")
#                             print(" \n1. Student Details of the student.")
#                             print("2. Parent Details of the student.")
#                             print("3. Marks of the student.")
#                             print("4. Quit.\n")
#                             ch=int(input('Your Choice: '))
#                             if ch in [1,2,3]:
#                                     a=input("\nEnter the letter of your choice: ")   
#                             if ch ==1:
#                                     c.execute("select * from student_details where S_name like '{}%'".format(a))
#                                     t = c.fetchall()
#                                     if c.rowcount==0:
#                                             print("Sorry..there is no data found with this letter.")
#                                     else:
#                                             print('\n',t)        
#                             elif ch==2:
#                                     c.execute("select S.Admn_No,S_name,P_name from student_details S,Parent_details P where S_name like '{}%'".format(a))
#                                     t = c.fetchone()
#                                     if c.rowcount==0:
#                                         print("sorry there is no data found with this letter.")
#                                     else:
#                                         print('\n',t)        
#                             elif ch==3:
#                                     c.execute("select S.Admn_No,S_name,Subject1,Subject2,Subject3 from student_details S,Marks M where S_name like '{}%'".format(a))
#                                     t = c.fetchone()
#                                     if c.rowcount==0:
#                                         print("sorry there is no data found with this letter.")
#                                     else:
#                                         print('\n',t)
#                             elif ch==4:
#                                     print("Bye Bye! Have A Good Day")
#                                     break
#                             else:
#                                     print("INVALID CHOICE")
#                                     break
                           
#             def feepaid():
#                     flag = True
#                     while flag == True:
#                             print("\n*Display student name and parent contact of students whose FEE IS NOT PAID*")
#                             a=int(input("\nEnter the Admn_no of the student: "))
#                             c=mycon.cursor()
#                             c.execute("select S_name, class, Fee_type, Feepaid from Student_Details S, Fee_details F where S.Admn_no=F.Admn_no and S.Admn_no=%s"%(a,))
#                             t=c.fetchall()
#                             print(t)
#                             b=input("\nWant to check the student's Parent details (Y or N): ")
#                             if b=="Y":
#                                     c.execute("select*from parent_details where Admn_no=%s"%(a,))
#                                     t=c.fetchall()
#                                     print(t)
#                                     flag = False
                                    
#                             elif b=="N":
#                                     print("\nOkay!!")
#                                     flag = False
#                             else:
#                                     print("\nINVALID CHOICE, TRY AGAIN!!!")
#                                     break
                            
#             while True:
#                     print("\nCHOOSE : ")
#                     print(" 1. ADD Record for new admission.")
#                     print(" 2. SEARCH student record.")
#                     print(" 3. DELETE all records of a particular student.")
#                     print(" 4. UPDATE the details of the student.")
#                     print(" 5. Students RANGING between 2 limits.")
#                     print(" 6. Students Eligible for SCHOLORSHIP. ")
#                     print(" 7. CHECK whether the student is from the school or not. ")
#                     print(" 8. Distribution of REMARKS and CLUB names.")
#                     print(" 9. See the details by ASEC and DESC order.")
#                     print(" 10. Check if the student has PASSED or FAILED.")
#                     print(" 11. Students giving BOARD EXAMS this year.")
#                     print(" 12. Students eligible for VACCINATION.")
#                     print(" 13. Search the MARK and FEE details of the student.")
#                     print(" 14. TOTAL and AVERAGE marks of the student.")
#                     print(" 15. Check the STUDENT RECORD of the names starting with USER'S LETTER CHOICE.")
#                     print(" 16. Display student names and parent contact of students whose FEE IS NOT PAID")
#                     print(' 17. Exit ')
#                     ch=int(input('\nEnter Task number: '))
#                     if ch == 17:
#                             print('\n\t\t\t!!!!Exiting Now, Meet you soon!!!! ')
#                             for i in range(1):
#                                     print('\n\t\t\t***Logging off***')
#                             exit()
#                     if ch==1:
#                             add()
#                     elif ch==2:
#                             sr()
#                     elif ch==3:
#                             dela()               
#                     elif ch==4:
#                             update()
#                     elif ch==5:
#                             rang()
#                     elif ch==6:
#                             scholarship()
#                     elif ch==7:
#                             check()
#                     elif ch==8:
#                             report()
#                     elif ch==9:
#                             order()
#                     elif ch==10:
#                             passorfail()
#                     elif ch==11: 
#                             board()
#                     elif ch==12:
#                             vaccination()
#                     elif ch==13:
#                             markfee()
#                     elif ch==14:
#                             totavg()
#                     elif ch==15:
#                             alpha()
#                     elif ch==16:
#                             feepaid()
#                     else :
#                             print("\nINVALID CHOICE ")
#     else:
#             print("\nWRONG PASSWORD: ACCESS DENIED")
#             print("You have %d valid attempts left now"%(count))



                                                         
