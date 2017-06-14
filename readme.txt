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
"""
 
1.L represents a group of courses, l represents id of a course from L, for example comp6320
2.i represents each lecture of course.
i_limit represents the number of students who enroll the lecture i.
i_major represents the major of lecture i 
i_teacher represents the teacher of lecture i.
For example, the course comp6320 has three lectures, and these lectures have their own id(i).
3.CSi represents a group of all lectures,i belongs to CSi
4.T represents a group of time slots, t represents single time slot
5.R represents a group of class rooms, r represents single room, r_limit represents the upper bound of students in this class room
6.P represents a group of teachers, p represent a teacher belongs to P
p_t represents a group of time slots that teacher p wants/prefer to take lecture

	
7.Variable: Ri represents the lecture i's class room
8.Variable: Ti represents the lecture t's time slot

Constraints:
1. the lectures in the same major should be assigned in different time slot.
Ti!=Ti' if i_major==i'_major
2. one teacher can only teacher one lecture in a time slot.
because we have constraint one, it means we will concern about teachers who teacher different majors' courses
Ti!=Ti' if i_teacher==i'_teacher and i_major!=i'_major
3. the lecture can only be assigned to room if the students number is less than the room's limit
Ri!=r if r_limit<=i_limit
4. the room can only be assigned to one lecture at the same time 
Ri!=Ri' if Ti==Ti' where i!=i'

soft constraints:
1. the lecture should be assigned in lecturer preferred time slots
Ti belongs to p_t if i_teacher==p

2. the same course's lecture should not be the same day

