from sFunctions import *

# Run function

def runSearch():
   # Get double array
   try:
      studentList = openFile()
   except:
      return
   # Set running value
   # q = 0 = running
   # q = 1 = stopped
   q=0
   # Start running
   while(q==0):
      # Read User Input
      choice = input("Instruction:> ")
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
         s = ","
         #try:
         if(third == ""):
            for name in getStudent(studentList, second):
               print(s.join(name))
         else:
            for name in getStudent(studentList, second, third):
               print(s.join(name))
         #except:
            #continue;

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
         #try:
         if(third == ""):
            for name in getGradeSearch(studentList, int(second)):
               print(s.join(name))
         else:
            print(s.join(getGradeSearch(studentList, int(second), third)))
         #except:
            #continue
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



