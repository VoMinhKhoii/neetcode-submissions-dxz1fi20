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
            
        # we add in if val of next temp <= val of last item in temp_stack
        # if val of next temp > val of last item in temp_stack
        # res at position = last item in temp_stack = position of next temp - 
        # original position of item to be popped
        # WHILE LOOP: we want to constantly hold a next temp to check
        # until it meet the last value in stack which has larger value