
age = int (input(" Enter your age "))
def classify_person (age):
  if age>= 0 and age <=12:
      print ( "Child")
  elif age <= 17:
       print ("Teenager")
  elif age <= 64:
      print ("Adult")
  else:
     print ("Senior")
classify_person(age)
