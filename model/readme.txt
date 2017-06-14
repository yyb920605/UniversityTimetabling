1.CS represents a group of courses, CS_id represents id of a course from CS, for example comp6320
2.L represents each lecture of course.
L_limit represents the number of students who enroll the lecture l.
L_major represents the major of lecture l 
L_teacher represents the teacher of lecture l.
For example, the course comp6320 has three lectures, and these lectures have their own id(i).
3.CSi represents a group of all lectures,l belongs to CSi
4.T represents a group of time slots, t represents single time slot
5.R represents a group of class rooms, r represents single room, r_limit represents the upper bound of students in this class room
6.P represents a group of teachers, p represent a teacher belongs to P
p_t represents a group of time slots that teacher p wants/prefer to take lecture

	
7.Variable: RLi represents the lecture l's class room
8.Variable: TLi represents the lecture l's time slot

Constraints:
1. the lectures in the same major should be assigned in different time slot.
Ti!=Ti' if l_major==l'_major
2. one teacher can only teacher one lecture in a time slot.
because we have constraint one, it means we will concern about teachers who teacher different majors' courses
Ti!=Ti' if l_teacher==l'_teacher and l_major!=l'_major
3. the lecture can only be assigned to room if the students number is less than the room's limit
Ri!=r if r_limit<=l_limit
4. the room can only be assigned to one lecture at the same time 
Ri!=Ri' if Ti==Ti' where i!=i'

soft constraints:
1. the lecture should be assigned in lecturer preferred time slots
Ti belongs to p_t if l_teacher==p

2. the same course's lecture should not be the same day

