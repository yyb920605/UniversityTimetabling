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
from datetime import *
class timeSlot:
    
    def __init__(self):
        self.timeid=""
        self.startTime=""
        self.endTime=""
        self.weekday=""
    def _str_(self):
        print [self.timeid,self.startTime,self.endTime,self.weekday]
    def returnResult(self):
        return self.timeid+" "+self.weekday+" "+self.startTime+"-"+self.endTime    
    def getTimeInformation(self,content=[]):
        for i in content:
            if i.startswith("tid:"):
                self.timeid=str(i)[4:]
            elif i.startswith("weekday:"):
                self.weekday=str(i)[8:]
            elif i.startswith("startime:"):
                self.startTime=str(i)[9:]
            elif i.startswith("endtime:"):
                self.endTime=str(i)[8:]            
    def avaibleTime(self,startorigin,endorigin,day):
        startor=datetime.strptime(startorigin,'%H:%M')
        endor=datetime.strptime(endorigin,'%H:%M')
        startth=datetime.strptime(self.startTime,'%H:%M')
        endtth=datetime.strptime(self.endTime,'%H:%M')
        if startor<=startth and endor>=endtth and day==self.weekday:
            return True
        else:
            return False
        
# class timeSlotList:
#     
#     def __init__(self):
#         self.timeSlotList={};
#     def addTimeSlot(self,tid,timeSlot):
#         self.timeSlotList[tid]=timeSlot;
#     def _str_(self):
#         for t in self.timeSlotList:
#             print self.timeSlotList[t]._str_();
#     def getAviliableTimeSlot(self,startTime,endTime,weekday):
#         weekday.list(); 


def readTimeFile():
    timeSlotList=[]
    with open('model/time.txt') as f:
        lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        if not line.startswith("#") and not line=='':
            content=line.split(",")
            #print content
            times=timeSlot()
            times.getTimeInformation(content)
            times._str_()
            timeSlotList.append(times)

                   
    return timeSlotList;

if __name__ == "__main__":
    readTimeFile()
#     startor=datetime.strptime("00:00",'%H:%M')
#     endor=datetime.strptime("14:00",'%H:%M')
#     print startor<endor

                    
