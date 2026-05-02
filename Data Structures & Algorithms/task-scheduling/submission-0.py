from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # So if for each pass, we do the the one with highest frequency first:
        # Ex: [A,A,A,B,B] n = 2
        # It would look like:
        # A -> _ -> _ -> A -> _ -> _ -> A
        # We can check if other is enough to fill in the gaps
        # Denote f as the highest frequency
        # Formula is gonna: (f-1) * n + f
        # (f frequency creates f-1 gaps n) + f 
        # What if there are two having the same highest frequency
        # ["A","A","A","B","B","B"], n = 2
        # A->B->Idle->A->B->Idle->A->B = 8 instead of 7 like the formula.
        # Cause at the end, we not only fill in f, but also the others with same highest
        # --> (f-1)*n + count_of_highest_frequency
        # And there is also some cases where len(tasks) is already sufficient
        # tasks = ["A","A","A","B","B","C","D","E"], n = 2
        # A->B-C>A->B->D->A->E
        # So max(len(tasks), (f-1)*n + count_of_highest_frequency)
        
        # INTUITION for max()
        # One way to build intuition: try ["A","A","A","A"], n = 0. No cooldown at all, 
        # so answer is just 4 = len(tasks). Formula gives (4-1)*0 + 1 = 1. max(4, 1) = 4 ✓.
        # Now try ["A","A","A","A"], n = 2. Formula gives (4-1)*2 + 1 = 7. max(4, 7) = 7 ✓.
        # The max is doing the case selection for you implicitly
        count = Counter(tasks) #Return the count of each value in tasks
        f = max(count.values())
        count_max = 0
        for v in count.values():
            if v == f:
                count_max = count_max + 1
        return max(len(tasks), (f-1)*n + f + count_max-1)