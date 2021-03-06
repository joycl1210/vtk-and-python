class Solution:
    def numSquares(self, n: int) -> int:
        # 双端队列
        from collections import deque
        deq = deque()
        visited = set()
        
        deq.append((n,0))
        while deq:
            number,step = deq.popleft()
            targets=[number-i*i for i in range(1,int(number**0.5)+1)]
            for target in targets:
                if target == 0:
                    return step+1
                if target not in visited:
                    deq.append((target,step+1))
                    visited.add(target)
        return 0
