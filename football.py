#N - Number of passes
#T - Test Cases
T = int(input()) #Testcases
MyArray = []
for i in range(T):
	N = list(input().upper().split())
	ball_possesed = N[1]
	MyArray.append(ball_possesed)
	
	for j in range(int(N[0])):
		process = list(input().upper().split())
		if process[0] == "P":
			ball_possesed = process[1]
			MyArray.append(ball_possesed)
			
		elif process[0] == "B":
			MyArray.pop()
			

	print("Player {}".format(ball_possesed))
