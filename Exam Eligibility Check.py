m=input("did you have a medical cause Y or N: ")
a= int(input("enter the attendance of the student: "))

if m == 'Y': 
  print ("You are allowed")
else:
  if a>=75:  
    print ("Allowed")
  else:
    print ("Not allowed")
