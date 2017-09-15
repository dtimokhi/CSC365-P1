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