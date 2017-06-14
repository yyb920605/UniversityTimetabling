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
from timeSlot import timeSlot

class teacher:
    def __init__(self):
        self.name=""
        self.courseList=[]
        self.timeList={}
        self.avaliableTimeSlot=[]
    def getTeacherInformation(self,content=[]):
        for i in content:
            if i.startswith("name:"):
                self.name=str(i)[5:]
            elif i.startswith("course:"):
                self.courseList.append(str(i)[7:])
            elif i.startswith("time:"):
                timeString=i[5:]
                s=timeString.split(" ")
                if s[0] not in self.timeList.keys():
                    self.timeList[s[0]]=[];
                    tl=self.timeList[s[0]]
                    if len(s)!=1:
                        tl.append(s[1])
                else:
                    if len(s)!=1:
                        tl=self.timeList[s[0]]
                        tl.append(s[1])                                       
    def getTeacherTimeSlot(self,timeSlotList=[]):
        for i in self.timeList.keys():
            timelist=self.timeList[i]
            if timelist==[]:
                for j in timeSlotList:
                    if j.weekday==i:
                        self.avaliableTimeSlot.append(j.timeid)
            else:
                for z in timelist:
                    s=z.split('-')
                    start=s[0]
                    end=s[1]
                    for j in timeSlotList:            
                        if j.avaibleTime(start,end,i):
                            self.avaliableTimeSlot.append(j.timeid)

                
                 
    def _str_(self):
        print [self.name,self.courseList,self.timeList,self.avaliableTimeSlot]

def readTeacherFile(timeList):
    teacherList=[];
    with open('model/teacher.txt') as f:
        lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        if not line.startswith("#") and not line=='':
            content=line.split(",")
            #print content
            tea=teacher()
            tea.getTeacherInformation(content)
            tea.getTeacherTimeSlot(timeList)
            tea._str_()
            teacherList.append(tea)
                   
    return teacherList;

if __name__ == "__main__":
    a=[]
    readTeacherFile(a)
                    
