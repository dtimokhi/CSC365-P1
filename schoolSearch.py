from statistics import mean
from sFunctions import *

# Open file

def openFile():
   # Open .txt file
   studentsDat = open('students.txt', 'r')
   # Make array list
   fullDatList = []
   i = 0
   # enumerate give index as num and value as line
   for num, line in enumerate(studentsDat):
     # Strip a current line
     fields = line.strip().split(",")
     # Append to a double array
     fullDatList.append(fields)
   # Return double array
   return(fullDatList)

# Start running

def runSearch():
   # Get double array
   studentList = openFile()
   # Set running value
   # q = 0 = running
   # q = 1 = stopped
   q=0
   # Start running
   while(q==0):
      choice = input("")
      choice = choice.lower()
      first = ""
      second = ""
      third = ""
      thirdLet = ""
      if(len(choice)>0):
         first=choice.split()[0]
         firstLet = first[0]
         if(len(choice.split()) > 1):
            second=choice.split()[1]
            secondLet = second[0]
            if(len(choice.split()) > 2):
               third=choice.split()[2]
               thirdLet =third[0]  
      if(first == "s:" or first == "student:"):
         print("Student")
      if(first == "teacher:" or first == "t:"):
         print("Teacher")
      if(first == "bus:" or first == "b:"):
         print("Bus")
      if(first == "grade:" or first == "g:"):
      s = ","
      try:
         if(thirdLet == ""):
         for name in getGradeSearch(studentList, int(second)):
            print(s.join(name))
         else:
            print(s.join(getGradeSearch(studentList, int(second), third)))
      except:
         continue
      if((first == "average:" or first == "a:")):
         try:
            print(getAverage(studentList, int(second)))
         except:
            continue
      if(first == "i" or first == "info"):
         try:
            for grade in getInfo(studentList):
               print(str(grade[0]) + ": " + str(grade[1]))
          except:
             continue
      if(first == "q" or first== "quit"):
         q=1
      else:
         q=0

runSearch()



