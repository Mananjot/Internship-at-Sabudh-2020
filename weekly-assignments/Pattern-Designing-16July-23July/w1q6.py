"""

Question: Print the pattern
Print the following pattern for the given number of rows.

Pattern for N = 5
1 2 3 4 5
11 12 13 14 15
21 22 23 24 25
16 17 18 19 20
6 7 8 9 10

Input format:
N (Total no. of rows)

Output format:
Pattern in N lines

Sample Input 1
4

Sample Output 2
1 2 3 4
9 10 11 12
13 14 15 16
5 6 7 8

"""

n = int(input())

if n % 2 == 0:
  up_run_freq = n - 2                 # it is same like (n-1)//2 * 2 - 1
  low_run_freq = up_run_freq + 1      
  
else:
  up_run_freq = n - 1                 # it is same like n//2 * 2 - 1
  low_run_freq = up_run_freq - 1


for i in range(0, up_run_freq + 1, 2):
  pattern = []                        # List is used in order to fulfill output format --> No space after last element
  for j in range(1, n + 1):
    pattern.append(n * i + j)         # dirctly print(n * i + j, end = " ") can be used
  print(*pattern, sep = " ")
    
for i in range(low_run_freq,0, -2):
  pattern = []                        
  for j in range(1, n + 1):         
    pattern.append(n * i + j)         # print(n * i + j, end = " ")
  print(*pattern, sep = " ")          # This prints the list without brackets [] and commas , with a space
  

"""

up_run_freq divide the square into two parts 
the halfs are doubled because we have to run the loop with step size 2 and -2

j  0 1 2 3      i     k                         result 4*k + j + 1
 -------------                                        j = 0
| 1 2 3 4     | 0     0                             4*0 + 0 + 1
| 9 10 11 12  | 1     2 (up_run_freq ends)          4*2 + 0 + 1
| 13 14 15 16 | 2     3 (low_run_freq starts)       4*3 + 0 + 1
| 5 6 7 8     | 3     1                             4*1 + 0 + 1
 -------------
 
""" 
    

