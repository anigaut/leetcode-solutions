# The stack contains one car from each unique fleet
# When one car is bound to reach the target before a car that started ahead of it, they both form a fleet
# Sort the position array

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        speed_map = {}

        for i in range(len(position)):
            speed_map[position[i]] = speed[i]
        position.sort(reverse=True)
        
        for i in range(len(position)):
            time_reached = (target - position[i])/speed_map[position[i]]
            if not stack or time_reached > stack[-1]:
                stack.append(time_reached)
        
        return len(stack) 
