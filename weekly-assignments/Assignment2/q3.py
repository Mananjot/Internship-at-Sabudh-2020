# Time = O(n) and Space = O(n)
def solution(walls):
    # Initialize
    tankLength = len(walls)
    water = 0
    # Boundary arrays for each index in walls
    max_left = [0]*tankLength 
    max_right = [0]*tankLength 

    # Filling left Boundary for each wall
    max_left[0] = walls[0] 
    for wall in range( 1, tankLength): 
        max_left[wall] = max(max_left[wall-1], walls[wall]) 

    # Filling right Boundary for each wall
    max_right[tankLength-1] = walls[tankLength-1] 
    for wall in range(tankLength-2, -1, -1): 
        max_right[wall] = max(max_right[wall + 1], walls[wall])

    # Computing the water that can be stored
    for wall in range(0, tankLength):
        water += min(max_left[wall],max_right[wall]) - walls[wall]
    return water

walls = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution(walls))

"""
# Time = O(n2) and Space = O(1)
print(water)
tankLength = len(walls)
water = 0
for wall in range(1, tankLength - 1):
    max_left = max(walls[:wall+1])
    max_right = max(walls[wall:tankLength])
    water += min(max_left,max_right) - walls[wall]
print(water)
"""