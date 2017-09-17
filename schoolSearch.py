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
      # Read User Input
      choice = input("")
      # Cast input to lower case
      choice = choice.lower()
      # Set storage variables
      first = ""
      second = ""
      third = ""
      # Check if anything was entered
      if(len(choice)>0):
         # Split the line
         split=choice.split()
         # Find length
         lSplit = len(split)
         # Get first value
         first = split[0]
         # Check length to continue
         if(lSplit > 1):
            # Read in second value
            second = split[1]
            # Check length to continue
            if(lSplit > 2):
               # Read in third value
               third=split[2]

      ### If statements to check command input ###
      
      # Student command
      if(first == "s:" or first == "student:"):
         print("Student")
      # Teacher command
      if(first == "teacher:" or first == "t:"):
         # Separator for .join()
         s = ","
         try:
            for name in getTeacher(studentList, second):
               print(s.join(name))
         except:
            continue
      # Bus command
      if(first == "bus:" or first == "b:"):
         # Separator for .join()
         s = ","
         try:
            for name in getBus(studentList, int(second)):
               print(s.join(name))
         except:
            continue
      # Grade command
      if(first == "grade:" or first == "g:"):
         # Separator for .join()
         s = ","
         try:
            if(third == ""):
               for name in getGradeSearch(studentList, int(second)):
                  print(s.join(name))
               else:
                  print(s.join(getGradeSearch(studentList, int(second), third)))
         except:
            continue
      # Average command
      if((first == "average:" or first == "a:")):
         try:
            tmpList = getAverage(studentList, int(second))
            print(str(tmpList[0]) + "," + str(tmpList[1]))
         except:
            continue
      # Info command
      if(first == "i" or first == "info"):
         try:
            for grade in getInfo(studentList):
               print(str(grade[0]) + ": " + str(grade[1]))
         except:
            continue
      # Quit command
      if(first == "q" or first== "quit"):
         # Set q to stop value
         q=1
      else:
         # Keep q at running value
         q=0

      ### End of command statements ###

# Issue run command
runSearch()



