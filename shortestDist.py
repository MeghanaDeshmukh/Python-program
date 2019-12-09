def checkExistence(low,high,array):
	diff = abs(high - low);
	if diff > len(array):
		for index in range (0, len(array)):
			if array[index] < high and array[index] > low:
				return False;
	else:
		for index in range(low+1, high):
			if index in array:
				return False;
	return True;

def solution():
	#A= [1,4,7,3,3,5];
	A=[-2147483648,-13,-7,-13,0,-126,-1,-8];
	minDist = -1;
	#print("len is: ", len(A));
	for i in range(0, len(A)-1):
		#print ("i is :" , i);
		for j in range (i+1, len(A)):
			#print("i, A[i]: ", i, A[i], "\n j, A[j]: ", j,A[j]);
			if A[i] == A[j]:
				#print("A[i], Aj] equals: ", A[i], A[j]);
				continue;
			elif A[i] < A[j]:
				adjacent = checkExistence(A[i],A[j],A);
			elif  A[j] < A[i]:
				adjacent = checkExistence(A[j],A[i],A);
			
			#print("Adjacent is: ", adjacent, abs(i-j));
			if adjacent: 
				#print("Adjacent is: ", adjacent, abs(i-j));
				if minDist > abs(i-j) or minDist == -1 :
					minDist = abs(i-j);
	
	#print (minDist);
	return minDist;
			

solution();