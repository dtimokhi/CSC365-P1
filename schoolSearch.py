from statistics import mean
from sFunctions import *

def openFile():
   studentsDat = open('students.txt', 'r')
   fullDatList = []
   i = 0
   for num, line in enumerate(studentsDat):
     fields = line.strip().split(",")
     fullDatList.append(fields)
   return(fullDatList)

def runSearch():
   studentList = openFile()
   q=0
   while(q==0):
       choice = input("")
       choice = choice.lower()
       first = ""
       second = ""
       third = ""
       thirdLet = ""
       if(len(choice)>0):
           first=choice.split()[0]
           firstLet = first[0].lower()
           if(len(choice.split()) > 1):
               second=choice.split()[1]
               secondLet = second[0].lower()
               if(len(choice.split()) > 2):
                  third=choice.split()[2]
                  thirdLet =third[0].lower()  
       if(first.lower() == "s:" or first.lower() == "student:"):
           print("Student")
       if(first.lower() == "teacher:" or first.lower() == "t:"):
           print("Teacher")
       if(first.lower() == "bus:" or first.lower() == "b:"):
           print("Bus")
       if(first.lower() == "grade:" or first.lower() == "g:"):
        s = ","
        try:
          if(thirdLet == ""):
            for name in getGradeSearch(studentList, int(second)):
              print(s.join(name))
          else:
            print(s.join(getGradeSearch(studentList, int(second), third)))
        except:
          continue
       if((first.lower() == "average:" or first.lower() == "a:")):
          try:
             print(getAverage(studentList, int(second)))
          except:
             continue
       if(first.lower() == "i" or first.lower() == "info"):
          try:
            for grade in getInfo(studentList):
               print(str(grade[0]) + ": " + str(grade[1]))
          except:
             continue
            
       if(first.lower() == "q" or first.lower()== "quit"):
           q=1
       else:
           q=0

runSearch()

studentListTmp = openFile()
print(getFirstLast(studentListTmp))


