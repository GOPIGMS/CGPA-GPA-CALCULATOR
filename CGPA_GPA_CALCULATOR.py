

print("""How to use : 
step 1:Enter what  you need cgpa or gpa.
IF GPA FOLLOW THESE STEPS:-

step 1:Enter the number subjects and press enter.
step 2:Enter the credit value of the subject.
step 3:Enter the grade obtained in exam. (For the reference mentioned the grade and their value below)
"you can verify your grade after entering it will be displayed"
step 4:Repeat step 2 and 3.
"at last you can see your credit and grade separately"
step 4 :Your GPA will be displayed.

Here is the GRADES their VALUES:

"O"   : 10,
"A+"  :9,
"A"   :8,
"B+"  :7,
"B"   :6,
"RA"  :0.
IF CGPA FOLLOW THESE STEPS:-

step 1:Enter the number of sem  you need to calculate:
step 2:Enter the gpa of sem 1.
step 3:Repeat step 2 until the total number of sem you have mentioned.
step 4 :Your CGPA will be displayed.

""" )
def quote(f):
   if f > 9.5:
      print("congrats")
      print("your are a Gold medalist ")

   elif f > 8.5 and f <=9.5:
      print("congrats")
      print("your are 1st class with distinction ")

   elif f > 7.5 and f <= 8.5:
      print("congrats")
      print("your are 1st class ")


   elif f > 6 and f <=7.5:

      print("your can get 1st class if you work hard ")
      print("all the best")

   else:

      print("Don't worry failure is a step stone to success ")
      print("all the best")







need=input("what do you need gpa or cgpa:").upper()
if need=="GPA":
   # dictonary assigned with credits and their value
   ref = {"O": 10,
          "A+": 9,
          "A": 8,
          "B+": 7,
          "B": 6,
          "RA": 0}
   n = int(input("enter the no of subject:"))
   c = []
   g = []
   for i in range(n):
      c.append(int(input(f"enter the {i + 1} subject credit  : ")))

      g.append(input(f"enter the {i + 1}  subject grade  : ").upper())

      print(f"the {i + 1} subject credit:{c[i]},grade:{g[i]} ")
   print("credits:", c)
   print("grades:", g)
   print("check you have entered all the value correct ")
   verify=input("enter y to change  if needed   else enter any value to see the result:").upper()
   if verify=='Y':
      change=input("enter c to change the credit and g change to grade  :").upper()
      if change =="C":
         change_index=int (input("enter the change index in the above list (start from 1):"))
         change_value=int(input("enter the credit value to change:"))
         c[change_index-1]=change_value
      elif change =="G":
         change_index=int (input("enter the change index in the above list (start from 1):"))
         change_value=input("enter the grade  value to change:").upper()
         g[change_index-1]=change_value
      else:
         print("invalid input")

   d = 0
   for i in range(n):
      d = d+(c[i] * (ref[g[i]]))

   e = sum(c)
   f = d / e
   print(f"Here is the grade:{f:.2f}")
   quote(f)


elif need=="CGPA":
   Total_cgpa=[]
   enter_cgpa=int(input("Enter the number of sem  you need to calculate:"))
   for i in range(enter_cgpa):
      Total_cgpa.append(float(input(f"enter the {i + 1} sem gpa : ")))
   print("Gpa you entered ",Total_cgpa)
   print("check you have entered all the value correct ")
   verify = input("enter y to change  if needed   else enter any value to see the result:").upper()
   if verify == 'Y':
      change_index = int(input("enter the change index in the above list (start from 1):"))
      change_value = float(input("enter the sem value to change:"))
      Total_cgpa[change_index - 1] = change_value
   cgpa=sum(Total_cgpa)/enter_cgpa
   print("your cgpa is:",cgpa)
   quote(cgpa)

else:
    print("Invalid Input")



