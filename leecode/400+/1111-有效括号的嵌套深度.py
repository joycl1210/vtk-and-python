def maxDepthAfterSplit(self, seq):
    ans = []
    d = 0
    for c in seq:
        if c == '(':
            d += 1
            ans.append(d % 2)
        if c == ')':
            ans.append(d % 2)
            d -= 1
    return ans
