class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return [0]
        temp_stack = []
        res = [0] * len(temperatures)
        for idx,val in enumerate(temperatures):
            if len(temp_stack) == 0 or val <= temp_stack[-1][0]:
                temp_stack.append([val, idx])
            while val > temp_stack[-1][0]:
                res[temp_stack[-1][1]] = idx - temp_stack[-1][1]
                temp_stack.pop()
                if len(temp_stack) == 0 or val <= temp_stack[-1][0]:
                    temp_stack.append([val, idx])
        return res
            
        # temp_stack = [[30, 0], [29,1]]
        # {29, 1}
        # temp_stack = [{38, 1}, {30,2}]
        # {36, 3}
        # temp_stack = [{38, 1}, {36,3}, {35,4}]
        # {40,5}
        # temp_stack = [{40,5}, {28,6}]
        # [1,4,1,2,1, , , ]