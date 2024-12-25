from typing import List

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), key=lambda c: c[0])

        if len(cars) < 2:
            return len(cars)

        formsFleet = lambda a, b: (target - a[0])/a[1] <= (target - b[0])/b[1]
        stack = []

        for i in range(len(cars)):
            while stack and formsFleet(stack[-1], cars[i]):
                stack.pop()
            stack.append(cars[i])
            
        return len(stack)
