#!/usr/bin/python
#
# Copyright (c) 2014-2017 - Yinbo Yang <hityangyinbo@163.com>
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from constraint import *
from lecture import *
from timeSlot import *
from teacher import *
from room import *
import time
from pyasn1.compat.octets import null

def main():
    problem = Problem(RecursiveBacktrackingSolver())


    print"read timeslot:"
    timeSlotList=readTimeFile()
    print"read lecturelist:"
    lectureList=readLectureFile()
    print"read teacherlist:"
    teacherList=readTeacherFile(timeSlotList)
    print"read roomlist:"
    roomList=readRoomFile()
    
    print "endcoding lecture time and room:"
#lectureTime,lectureRoom and lecture is encoding relatedly,for example TL1,RL1 and L1 represent the same lecture, but TL1 will be assigned time slot in CSP for lecture L1, the same as RL1(room)
    dicOflectureTime=encodingLectureTime(lectureList)
    dicOflectureRoom=encodingLectureRoom(lectureList)
    dicOflecture=encodingLecture(lectureList)
    dicOfLectureByCourseId=encodingLectureByCourseId(lectureList)
    dicOfTime=encodingTime(timeSlotList)
#Two variables Ti and Ri representing lecture i is assigned to time slot and class room
    print "add variables:"
    problem.addVariables(dicOflectureTime.keys(), timeSlotList)
    problem.addVariables(dicOflectureRoom.keys(), roomList)
#Constraint one:the lectures in the same major should be assigned in different time slot.
#I also create dicOfLectureRoomByMajor={} for constrain four, this is an encoding dictionary of lectureRoom dividied by majors
    print "begin to add constraints:"
    start_time=time.time()
    print "add constraint one"
    dicOfLectureRoomByMajor={}
    dicOfMajor= divideMajor(dicOflecture)
    for i in dicOfMajor.keys():
        temList=[]
        temList2=[]
        if i not in dicOfLectureRoomByMajor.keys():
            dicOfLectureRoomByMajor[i]=[]
        for j in dicOfMajor[i]:
            temList.append("T"+j)
            temList2.append("R"+j)
        dicOfLectureRoomByMajor[i]=temList2
        problem.addConstraint(AllDifferentConstraint(), temList)
#Constraint Two: one teacher can only teacher one lecture in a time slot.
    print "add constraint two"
    dicOfDtea=divideTeacher(teacherList, dicOfLectureByCourseId)
    for i in dicOfDtea.keys():
        temList=[]
        for j in dicOfDtea[i]:
            temList.append("T"+j)
        problem.addConstraint(AllDifferentConstraint(), temList)
#Constraint Three: the lecture can only be assigned to room if the students number is less than the room's limit   
    print "add constraint three"
    dicOflectureRoom=availableRoom(roomList, dicOflectureRoom)
    for i in dicOflectureRoom.keys():
        lect=dicOflectureRoom[i]
        temList=[]
        temList.append(i)

        problem.addConstraint(InSetConstraint(lect.avaliableRooms),temList)

#Constraint Four: the room can only be assigned to one lecture at the same time 
#Based on the first three constraints, we only concern about lectures from different majors
    print "add constraint four"
    def func(T1,R1,T2,R2):
        if T1==T2:
            return R1!=R2
        else:
            return R1==R2 or R1!=R2
    print dicOfLectureRoomByMajor
    listOfMajorKeys=dicOfLectureRoomByMajor.keys()
    lenOfMajorKeys=len(listOfMajorKeys)
    for i in range(0,lenOfMajorKeys-1):
        temList3=dicOfLectureRoomByMajor[listOfMajorKeys[i]]
        for j in range(i+1,lenOfMajorKeys):
            temList4=dicOfLectureRoomByMajor[listOfMajorKeys[j]]
            for roomlect in temList3:
                for roomlect1 in temList4:
                    timeLect="T"+roomlect[1:]
                    timeLect1="T"+roomlect1[1:]
                    problem.addConstraint(func, [timeLect,roomlect,timeLect1,roomlect1])
#     print listOfMajorKeys
        
#     problem.addConstraint(func, (T1,R1,T2,R2))   

#Soft constraint
#Soft constraint one: the lecture should be assigned in lecturer preferred time slots
#we can use dictionary of constraint 2
    print "add soft constraint one"
    for i in range(0,len(teacherList)):
        tea=teacherList[i]
        #temList5 is a list of keys of teacher's available time slots
        temList5=tea.avaliableTimeSlot
        temList=[]
        for z in temList5:
            temList.append(dicOfTime[z])
        #temList6 is a list of lectures that this teacher teaches
        temList6=[]
        for j in dicOfDtea[tea.name]:
            temList6.append("T"+j)
#         print tea.name
#         print temList
#         print temList5
#         print temList6
        problem.addConstraint(InSetConstraint(temList),temList6)
#Soft constraint two: the same course's lecture should not be the same day
    print "add soft constraint two"
    def func2(a,b):
        return a.weekday!=b.weekday
    def func3(a,b,c):
        return a.weekday!=b.weekday!=c.weekday
    def func4(a,b,c,d):
        return a.weekday!=b.weekday!=c.weekday!=d.weekday
    def func5(a,b,c,d,e):
        return a.weekday!=b.weekday!=c.weekday!=d.weekday!=e.weekday
    for i in dicOfLectureByCourseId.keys():
        lect=dicOfLectureByCourseId[i]
        temList=[]
        if len(lect)==2:
            for j in lect:
                tlec="T"+j
                temList.append(tlec)
                problem.addConstraint(func2, temList)
        elif len(lect)==3:
            for j in lect:
                tlec="T"+j
                temList.append(tlec)
                problem.addConstraint(func3, temList)
        elif len(lect)==4:
            for j in lect:
                tlec="T"+j
                temList.append(tlec)
                problem.addConstraint(func4, temList)
        elif len(lect)==5:
            for j in lect:
                tlec="T"+j
                temList.append(tlec)
                problem.addConstraint(func5, temList)
#     problem.addConstraint(func2, ["TL0","TL1"])
    print ("encoding constraints phase costs %s seconds"%(time.time()-start_time))

    print "begin to get solution:"
    start_time=time.time()
#     solutions=problem.getSolutions()
#     if solutions != None:
#         for solution in solutions:
#             displaySolution(solution, dicOflectureTime, dicOflectureRoom, dicOflecture)
    solution=problem.getSolution()
    displaySolution(solution, dicOflectureTime, dicOflectureRoom, dicOflecture)
    print ("getting solutions phase costs %s seconds"%(time.time()-start_time))
   
#     solutions=problem.getSolutionIter()
#     for i in range(0,10)   

def displaySolution(solution=[],dicOflectureTime={},dicOflectureRoom={},dicOflecture={}):
    for i in dicOflectureTime.keys():
        j='R'+i[1:]
        t=solution[i]
        s=solution[j]
        lect=dicOflectureTime[i]
        room=dicOflectureRoom[j]
        lect.time=t
        room.room=s
    for i in dicOflecture.keys():
        lect=dicOflecture[i]
        lect.outputresult()  
#This funciton is used to divide lectures' majors into dictionary
#input:dictionary of lectures after encoding
#output:major dictionary
def divideMajor(lectureDic={}):
    majorDic={}
    for k in lectureDic.keys():
        lect=lectureDic[k]
        major=lect.major
        if major not in majorDic.keys():
            majorDic[major]=[]
        l=majorDic[major]
        l.append(k)
    return majorDic

#This funciton is used to divide courses by teachers into dictionary
#input:list of teacher
#output:teacher dictionary with list of lectures
def divideTeacher(teacherlist=[],dicOfLectureByCourseId={}):
    teacherDic={}
    for i in range(0,len(teacherlist)):
        tea=teacherlist[i]
        if tea.name not in teacherDic.keys():
            teacherDic[tea.name]=[]
        listOfcourse=tea.courseList
        l=teacherDic[tea.name]
        for j in range(0,len(listOfcourse)):
            course=listOfcourse[j]
            if course in dicOfLectureByCourseId.keys():
                l2=dicOfLectureByCourseId[course]
                l+=l2
    return teacherDic
#This funciton is used to calculate the list of available rooms for lectures
#input:list of room and dictionary of lecture after encoding
#output:teacher dictionary with list of lectures
def availableRoom(listOfRoom=[],dicOfLectureRoom={}):
    for i in dicOfLectureRoom.keys():
        lect=dicOfLectureRoom[i]
        for j in range(0,len(listOfRoom)):
            room=listOfRoom[j]
            if contains(float(room.roomStudentLimit), float(lect.studentNum)):
                lect.avaliableRooms.append(room)
#     for i in range(0,len(listOfRoom)):
#         print i
#         room=listOfRoom[i]
#         if room.roomid not in roomDic.keys():
#             roomDic[room.roomid]=[]
#         l=roomDic[room.roomid]
#         print room.roomid
#         for j in dicOfLectureRoom.keys():
#             lect=dicOfLectureRoom[j]
#             if contains(float(room.roomStudentLimit), float(lect.studentNum)):
#                 l.append(j)
    return dicOfLectureRoom   

def contains(num1,num2):
    if num1<num2:
        return False
    else:
        return True  
        
        
def encodingLectureByCourseId(lecturelist=[]):
    listOfCourse={}
    for i in range(0,len(lecturelist)):
        lec=lecturelist[i]
       
        if lec.courseid not in listOfCourse.keys():
            listOfCourse[lec.courseid]=[]
        l=listOfCourse[lec.courseid]
        l.append("L%d"%i)

    return listOfCourse  


def encodingLectureTime(lecturelist=[]):
    listOfLect={};
    for i in range(0,len(lecturelist)):
        if "TL%d"%i not in listOfLect.keys():
            listOfLect["TL%d"%i]=lecturelist[i]
    return listOfLect      
def encodingLecture(lecturelist=[]):
    listOfLect={};
    for i in range(0,len(lecturelist)):
        if "L%d"%i not in listOfLect.keys():
            listOfLect["L%d"%i]=lecturelist[i]
    return listOfLect    
def encodingTime(timelist=[]):
    listOftime={};
    for i in range(0,len(timelist)):
        if "T%d"%(i+1) not in listOftime.keys():
            listOftime["T%d"%(i+1)]=timelist[i]
    return listOftime     
def encodingLectureRoom(lecturelist=[]):
    listOfLect={};
    for i in range(0,len(lecturelist)):
        if "RL%d"%i not in listOfLect.keys():
            listOfLect["RL%d"%i]=lecturelist[i]
    return listOfLect  
    
    

    
if __name__ == "__main__":
    main()
