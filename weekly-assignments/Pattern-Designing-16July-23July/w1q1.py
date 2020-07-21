"""
Question: Pattern --> Triangle of numbers
Print the following pattern for the given number of rows. 
Pattern for N = 4 The dots represent spaces.
      1
    232
  34543
4567654

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Constraints:
0 <= N <= 50

Sample Input 1:
5

Sample Output 1:
        1
      232
    34543
  4567654
567898765

Sample Input 2:
4

Sample Output 2:
      1
    232
  34543
4567654

"""

n = int(input())
k = n*2 - 2			#No. of Columns
for i in range(0, n):
  for j in range(0,k):		#Creating Spaces in each row
    print(end = " ")
  k -= 2 			
  for j in range(0,i+1):	#incrementing no.'s in each row    
    print(i+j+1, end ="")	
  for j in range(i, 0,-1):	#decrementing no.'s in each row     #range(i+1, 1,-1)
    print(i+j, end="")		#print(i+j-1)
  print()
  
 
