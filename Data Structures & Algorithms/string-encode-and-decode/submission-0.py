class Solution:

    # ["Hello","World"]
    # --> "5#Hello5#World" --> 12
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # We use the length + a delimiter to handle multi-digit lengths
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter starting from current pointer i
            # This allows us to capture the full length regardless of digit count
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract the length (everything between i and j)
            length = int(s[i:j])
            
            # 3. Slice the actual string content
            # The content starts at j+1 and ends at j + 1 + length
            start_of_content = j + 1
            end_of_content = start_of_content + length
            res.append(s[start_of_content : end_of_content])
            
            # 4. Move the pointer i to the start of the next length-prefix
            i = end_of_content
            
        return res
        
