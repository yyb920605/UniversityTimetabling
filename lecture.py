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
class lecture:
    
    def __init__(self):
        self.courseid=""
        self.lectureslotid=""
        self.lectureHour=""
        self.teacher=""
        self.studentNum=""
        self.major=""
        self.room=""
        self.time=""
        self.avaliableRooms=[]
        
    def outputresult(self):
        print self.courseid+self.lectureslotid+" at "+self.room.roomid+" time is "+self.time.returnResult()+" teacher is "+self.teacher
    def _str_(self):
        print [self.courseid,self.lectureslotid,self.lectureHour,self.teacher,self.studentNum,self.major,self.time,self.room]    
    def getLectureInformation(self,content=[]):
        for i in content:
            if i.startswith("courseid:"):
                self.courseid=str(i)[9:]
            elif i.startswith("lecture:"):
                self.lectureslotid=str(i)[8:]
            elif i.startswith("lectureHour:"):
                self.lectureHour=str(i)[12:]
            elif i.startswith("teacher:"):
                self.teacher=str(i)[8:]    
            elif i.startswith("studentNum:"):
                self.studentNum=str(i)[11:]     
            elif i.startswith("major:"):
                self.major=str(i)[6:]                            
#     def getTeacherTimeSlot(self):
    

def readLectureFile():
    lectureSlotList=[]
    with open('model/lecture.txt') as f:
        lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        if not line.startswith("#") and not line=='':
            content=line.split(",")
            #print content
            lectureslot=lecture();
            lectureslot.getLectureInformation(content)
            lectureslot._str_()
            lectureSlotList.append(lectureslot)

                   
    return lectureSlotList;

if __name__ == "__main__":
    readLectureFile()
                    
