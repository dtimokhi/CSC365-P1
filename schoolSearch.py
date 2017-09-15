from statistics import mean

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
         try:
            if(third == ""):
               for name in getGradeSearch(studentList, int(second)):
                  print(name)
            else:
               print(getGradeSearch(studentList, int(second), third))
         except:
            continue
       if((first.lower() == "average:" or first.lower() == "a:")):
         try:
           print(getAverage(studentList, int(second)))
         except:
            continue
       if(first.lower() == "i" or first.lower() == "info"):
           print("Info")
       if(first.lower() == "q" or first.lower()== "quit"):
           q=1
       else:
           q=0

def getGradeValues(studentList, gradeNumber):
   tmpList = list(studentList)
   indexList = []
   for num, student in enumerate(studentList):
      if int(student[2]) != gradeNumber: 
         indexList.append(num)
   for index in sorted(indexList, reverse=True):
      del tmpList[index]
   return(tmpList)

def getFirstLast(studentList):
   outList = list(studentList)
   for num, student in enumerate(studentList):
      outList[num] = [student[0], student[1]]
   return(outList)


def getTypeGpa(studentList, typeGpa):
   outList = list(studentList)
   for num, student in enumerate(studentList):
      outList[num] = student[5]
   if typeGpa == "h":
      maxGpa = outList.index(max(outList))
      gpaStudent = studentList[maxGpa]
   elif typeGpa == "l":
      minGpa = outList.index(min(outList))
      gpaStudent = studentList[minGpa]
   return(gpaStudent)

def getGradeSearch(studentList, gradeNumber, typeGpa = "none"):
   if(typeGpa != "none"):
      gradeStudents = getGradeValues(studentList, gradeNumber)
      gpaStudent = getTypeGpa(gradeStudents, typeGpa)
   else:
      gradeStudents = getGradeValues(studentList, gradeNumber)
      gpaStudent = getFirstLast(gradeStudents)
   return(gpaStudent)

def getAverage(studentList, gradeNumber):
   gradeList = getGradeValues(studentList, gradeNumber)
   outList = list(gradeList)
   for num, student in enumerate(gradeList):
      outList[num] = student[5]
   outList = list(map(float, outList))
   avgGpa = mean(outList)
   return([gradeNumber, avgGpa])

runSearch()

studentListTmp = openFile()
print(getFirstLast(studentListTmp))


