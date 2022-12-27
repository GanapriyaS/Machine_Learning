male(ram).
male(shayam).
female(sita).
female(gita).
parent(gita,ram,shyam).
parent(gita,ram,sita).
sister(X,Y):- female(X),parent(A,B,X),parent(A,B,Y),write(X),write(' is sister of '),write(Y);write(X),write(' is not a sister of '),write(Y).
rollno(1917114).
student(A):- rollno(A),write(A),write(' is a student');write(A),write(' is not a student').