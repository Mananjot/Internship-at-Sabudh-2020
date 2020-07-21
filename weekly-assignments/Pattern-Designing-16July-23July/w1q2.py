"""

Question: Number Pattern

Print the following pattern Pattern for N = 4 1 23 345 4567 

Input Format:
N (Total no. of rows)

Output Format:
Pattern in N lines

Sample Input 1
4

Sample Output 2
   1
  23
 345
4567

"""

n = int(input())

# Using loops

k = n - 1
for i in range(n):
  for j in range(k):
    print(end = " ")
  k -= 1			# Adding Spaces
  for j in range(i+1):
    print(i + j + 1,end="") 	# Printing numbers after Spaces
  print()

"""
# Using Control Statements

for i in range(0, n):
    k = 1
    for j in range(0,n):
      if i + j >= n - 1:
        print(i + k, end = "")
        k += 1
      else:
        print(" ", end = "")
    print()
"""

