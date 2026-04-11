class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We get time to destination of each position
        # if the one behind has time to destination lower than the one ahead
        # it joins the one ahead and form a fleet
        sorted_position = sorted(zip(position, speed))
        position, speed = zip(*sorted_position)

        n = len(position)
        time_to_destination = [0] * n
        for i in range(n):
            time_to_destination[i] = (target - position[i]) / speed[i]
        fleets = []
        
        for i in reversed(time_to_destination):
        # append to fleets, only if the one behind have larger tdd than the one in front of it
            if len(fleets) == 0 or i > fleets[-1]:
                fleets.append(i)
        return len(fleets)
            




