# Open File
def openFile():
   # Open .txt file
   studentsDat = open('list.txt', 'r')
   teacherDat = open('teachers.txt', 'r')
   # Make array list
   fullDatList = []
   i = 0
   # enumerate give index as num and value as line
   for num, line in enumerate(studentsDat):
     # Strip a current line
     fields = line.strip().split(",")
     newFields = getTeacherVals(fields)
     # Append to a double array
     fullDatList.append(newFields)
   # Return double array
   return(fullDatList)
def openClassroomsNum():
   teacherDat = open('teachers.txt', 'r')
   indexList = []
   for index, val in enumerate(teacherDat):
      fields = val.strip().split(",")
      indexList.append(int(fields[2]))
   return indexList
def getTeacherVals(studentList):
   myList = studentList
   teacherDat = open('teachers.txt', 'r')

   classNum = int(studentList[3])
   for teacher in teacherDat:
      teacher = teacher.strip().split(",")
      if(classNum == int(teacher[2])):
         tmpList = [teacher[0].strip(), teacher[1].strip()]
         break
   myList.extend(tmpList)
   return myList
# Get grade command
# Takes: studentList(2DArr)
# gradeNumber(int)
# typeGpa(String)
def getGradeSearch(studentList, gradeNumber, typeGpa = "none"):
   if(typeGpa != "none"):
      # Find the highest/lowest gpa
      gradeStudents = getGradeValues(studentList, gradeNumber)
      # Return row of high/low gpa
      gpaStudent = getTypeGpa(gradeStudents, typeGpa)
   else:
      # Find all students with that gradeNumber
      gradeStudents = getGradeValues(studentList, gradeNumber)
      # Return rows of all
      gpaStudent = getFirstLast(gradeStudents)
   return(gpaStudent)

# Returns a 2DArr with students in that gradeNumber
# Takes: studentList(2DArr)[row][col]
# gradeNumber(int)
def getGradeValues(studentList, gradeNumber):
   tmpList = list(studentList)
   indexList = []
   for num, student in enumerate(studentList):
      if int(student[2]) != gradeNumber: 
         indexList.append(num)
   for index in sorted(indexList, reverse=True):
      del tmpList[index]
   return(tmpList)

# Return row of highest/lowest gpa
# Takes: studentList(2DArr)
# typeGpa(String)
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

# Returns 2DArr[Row][0=last,1=first]
# Takes studentList(2DArr[Row][Factor])
def getFirstLast(studentList):
   outList = list(studentList)
   for num, student in enumerate(studentList):
      outList[num] = [student[0], student[1]]
   return(outList)

# Returns 2DArr[grade][grade=0,n=1]
# Takes: studentList(2DArr)
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

# Returns Arr[0=gradeNumber,1=avgGpa]
# Takes studentList(2DArr)
# gradeNumber(int)
def getAverage(studentList, gradeNumber):
   gradeList = getGradeValues(studentList, gradeNumber)
   # Make deep copy
   outList = list(gradeList)
   for num, student in enumerate(gradeList):
      outList[num] = student[5]
   outList = list(map(float, outList))
   avgGpa = sum(outList)/float(len(outList))
   return([gradeNumber, avgGpa])

# Return 2DArr[row][0=last,1=first]
# Take: studentList(2DArr)
# busNum(int)
def getBus(studentList, busNum):
   indexList = []
   for num, student in enumerate(studentList):
      if int(student[4]) == busNum: 
         indexList.append(student)
   tmpList = getFirstLast(indexList)
   return(tmpList)

# Return 2DArr[row][0=last,1=first]
# Takes: studentList(2DArr)
# teachName(String)
def getTeacher(studentList, teachName):
   indexList = []
   for num, student in enumerate(studentList):
      if student[6] == teachName.upper(): 
         indexList.append(student)
   tmpList = getFirstLast(indexList)
   return(tmpList)

# Returns a 2DArr[row][factors depends on bus]
# Takes: studentList(2DArr)
# studentName(String)
# bus(String) - Optional B/b or BUS/bus
def getStudent(studentList, studentName, bus = "none"):
   if(bus == "none"):
      # Find the highest/lowest gpa
      gradeStudents = getNameValues(studentList, studentName)
      # Return row of high/low gpa
      gpaStudent = getS(gradeStudents)
   else:
      if(bus=="b")|(bus=="bus"):
         # Find all students with that gradeNumber
         gradeStudents = getNameValues(studentList, studentName)
         # Return rows of all
         gpaStudent = getSb(gradeStudents)
   return(gpaStudent)

# Returns a 2DArr with factor 0 (Last name) matching to name
# Takes: studentList(2DArr)
# name(String)
def getNameValues(studentList, name):
   indexList = []
   for num, student in enumerate(studentList):
      if student[0] == name.upper(): 
         indexList.append(student)
   return(indexList)

# Returns a 2DArr with factors for student
# Takes: studentList(2DArr)
def getS(studentList):
   outList = list(studentList)
   for num, student in enumerate(studentList):
      outList[num] = [student[0], student[1],student[2],student[3], student[6],student[7]]
   return(outList)

# Returns a 2DArr with factors for student + bus
# Takes: studentList(2DArr)
def getSb(studentList):
   outList = list(studentList)
   for num, student in enumerate(studentList):
      outList[num] = [student[0], student[1],student[4]]
   return(outList)
def getAllStudentsInClass(studentList, classNum):
   indexList = []
   for num, student in enumerate(studentList):
      if (int(student[3].strip()) == int(classNum)): 
         indexList.append(student)
   return(indexList)
def getAllTeachersInClass(studentList, classNum):
   indexList = []
   for num, student in enumerate(studentList):
      if (int(student[3].strip()) == int(classNum)): 
         indexList.append([student[6].strip(), student[7].strip()])
   for index, val in enumerate(indexList):
      indexList[index] = "-".join(val)
   indexList = list(set(indexList))
   for index, val in enumerate(indexList):
      indexList[index] = val.split("-")
   return(indexList)
def getTeachersInGrade(studentList, gradeNum):
   newListTmp = getGradeValues(studentList, int(gradeNum))
   newList = []
   for index, val in enumerate(newListTmp):
      newList.append([val[6].strip(), val[7].strip()])
   for index, val in enumerate(newList):
      newList[index] = "-".join(val)
   newList = list(set(newList))
   for index, val in enumerate(newList):
      newList[index] = val.split("-")
   return(newList)
def getEnrollment(studentList):
   outList = []
   for classNum in openClassroomsNum():
      n = 0
      for student in studentList:
         if int(student[3]) == classNum:
            n = n + 1
      tmpList = [classNum, n]
      outList.append(tmpList)
   return outList
def getGpaVal(studentList, valNum):
   outList = []
   for student in studentList:
      outList.append(float(student[valNum]))
   return outList
def getMeanGpaGrade(studentList):
   meanList = []
   for grade in range(7):
      gradeList = getGradeValues(studentList, grade)
      gpaList = getGpaVal(gradeList, 5)
      if(len(gpaList) == 0):
         meanGpa = "NULL"
      else:
         meanGpa = round(sum(gpaList)/float(len(gpaList)), 3)
      meanList.append([grade, meanGpa])
   return meanList
def getUniqueTeachers(studentList):
   newList = []
   newListTmp = studentList
   for index, val in enumerate(newListTmp):
      newList.append([val[6].strip(), val[7].strip()])
   for index, val in enumerate(newList):
      newList[index] = "-".join(val)
   newList = list(set(newList))
   for index, val in enumerate(newList):
      newList[index] = val.split("-")
   return(newList)
def getTeacherStudents(studentList, lstName, fstName):
   indexList = []
   for num, student in enumerate(studentList):
      if (student[6] == lstName.upper()) & (student[7] == fstName.upper()): 
         indexList.append(student)
   return(indexList)
def getMeanGpaTeacher(studentList):
   newTeachers = getUniqueTeachers(studentList)
   meanList = []
   for teacher in newTeachers:
      lstName = teacher[0]
      fstName = teacher[1]
      studentsTeacher = getTeacherStudents(studentList, lstName, fstName)
      gpaList = getGpaVal(studentsTeacher, 5)
      meanGpa = round(sum(gpaList)/float(len(gpaList)), 3)
      myAppend = teacher
      myAppend.append(meanGpa)
      meanList.append(myAppend)
   return meanList
def getUniqueBusRoute(studentList):
   newList = []
   newListTmp = studentList
   for index, val in enumerate(newListTmp):
      newList.append(int(val[4].strip()))
   newList = sorted(list(set(newList)))
   newList = [str(x) for x in newList]
   return(sorted(newList))
def getStudentsBus(studentList, busNum):
   indexList = []
   for num, student in enumerate(studentList):
      if(student[4] == busNum): 
         indexList.append(student)
   return(indexList)
def getMeanBus(studentList):
   busList = getUniqueBusRoute(studentList)
   meanList = []
   for bus in busList:
      studentBus = getStudentsBus(studentList, bus)
      gpaList = getGpaVal(studentBus, 5)
      meanGpa = round(sum(gpaList)/float(len(gpaList)), 3)
      meanList.append([bus, meanGpa])
   return meanList



