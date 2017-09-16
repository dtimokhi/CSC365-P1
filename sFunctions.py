from statistics import mean

def openFile():
   studentsDat = open('students.txt', 'r')
   fullDatList = []
   i = 0
   for num, line in enumerate(studentsDat):
     fields = line.strip().split(",")
     fullDatList.append(fields)
   return(fullDatList)

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
   if (typeGpa == "h") | (typeGpa == "high"):
      maxGpa = outList.index(max(outList))
      gpaStudent = studentList[maxGpa]
   elif (typeGpa == "l") | (typeGpa == "low"):
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
def getInfo(studentList):
   outList = []
   for grade in range(7):
      n = 0
      for student in studentList:
         if int(student[2]) == grade:
            n = n + 1
      tmpList = [grade, n]
      outList.append(tmpList)
   return outList
def getBus(studentList, busNum):
   indexList = []
   for num, student in enumerate(studentList):
      if int(student[4]) == busNum: 
         indexList.append(student)
   tmpList = getFirstLast(indexList)
   return(tmpList)
def getTeacher(studentList, teachName):
   indexList = []
   for num, student in enumerate(studentList):
      if student[6] == teachName.upper(): 
         indexList.append(student)
   tmpList = getFirstLast(indexList)
   return(tmpList)












