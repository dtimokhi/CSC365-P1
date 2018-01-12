from sFunctions import *

t = openFile()
#for i in t:
	#print(i)
#WOOLERY,NOLAN,2,104,51,2.92,STEIB,GALE
tmp = getTeachersInGrade(t, "3")
#print(tmp[1] == tmp[2])
#print(tmp)

#print(getEnrollment(t))

tmp = getMeanGpaTeacher(t)
tmp = getUniqueBusRoute(t)
tmp = getMeanBus(t)
print(tmp)