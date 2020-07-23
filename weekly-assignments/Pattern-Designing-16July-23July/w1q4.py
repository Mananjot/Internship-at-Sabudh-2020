
"""

Question: Arrow pattern

Print the following pattern for the given number of rows. Assume N is "always odd".
Note : There is space after every star. 

Pattern for N = 7

*
 * *
   * * *
     * * * *
   * * *
 * *
*

Input format:
Integer N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input 1
11

Sample Output 1

*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
"""

n = int(input())

# Method 1 --> Using For loop and List
# This method is used to get the required format of output i.e no space after last asterick (*)
# Valid if N is odd
k = -1                 # required indents
print("*")
for i in range(1, n):
  result = []
  if i <= n // 2:
    k += 2
    l = i + 1         # l sets the range for the loop and helps to write one loop for both if and else 
  else:               # Refer method 2 below which do not have the l
    k -= 2
    l = n % i
  m = k
  for j in range(l):
    result.append(" "*m + "*")
    m = 0
  print(*result, sep = " ")

"""

# Method 2 --> Using For Loop 
# Both loops separetly provide indentation as well as to print asterick
# But gives space character at last and does not pass test cases
# Valid if N is odd
k = -1
print("*")
for i in range(1, n):
  if i <= n // 2:
    k += 2
    for j in range(k):
      print(end =" ")
    for j in range(i+1):
      print("*", end=" ") 
    print()
  else:
    k -= 2
    for j in range(k):
      print(end =" ")
    for j in range(n%i):
      print("*", end=" ") 
    print()
    
"""
"""

# Method 2 --> Using 1 For Loop and join Method
# But gives space character at last and does not pass test cases
# Valid if N is odd
k = -1                    #required indents
print("*")
result = []
for i in range(1, n):
  if i <= n // 2:
    k += 2
    l = i + 1 
  else:
    k -= 2
    l = n % i
  m = k
  result.append(" "*m + "* "*l)
print("\n".join(result))

"""
    

