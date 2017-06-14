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
class room:
    
    def __init__(self):
        self.roomid=""
        self.roomLocation=""
        self.roomStudentLimit=""
    def _str_(self):
        print [self.roomid,self.roomLocation,self.roomStudentLimit]    
        
    def getRoomInformation(self,content=[]):
        for i in content:
            if i.startswith("roomid:"):
                self.roomid=str(i)[7:]
            elif i.startswith("roomLocation:"):
                self.roomLocation=str(i)[13:]
            elif i.startswith("roomStudentLimit:"):
                self.roomStudentLimit=str(i)[17:]       
                            
def contains(num1,num2):
    if num1<num2:
        return False
    else:
        return True     
def readRoomFile():
    roomList=[]
    with open('model/room.txt') as f:
        lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        if not line.startswith("#") and not line=='':
            content=line.split(",")
            #print content
            rooms=room()
            rooms.getRoomInformation(content)
            rooms._str_()
            roomList.append(rooms)
            
            

                   
    return roomList;

if __name__ == "__main__":
    readRoomFile()
    print contains(1000, 50)
                    
