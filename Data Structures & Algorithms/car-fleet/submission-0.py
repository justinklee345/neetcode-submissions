class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted(zip(position, speed), key=lambda car: car[0], reverse = True)
        stack = []

        for position, speed in arr:
            time = (target - position) / speed
            if len(stack) >= 1 and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)