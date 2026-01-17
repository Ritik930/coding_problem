class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)

        squares = []
        for i in range(N):
            square = [bottomLeft[i], topRight[i]]
            squares.append(square)
        squares.sort()
        # print(squares)

        res = 0
        for i in range(N):
            curStart, curEnd = squares[i]
            for j in range(i + 1, N):
                nxtStart, nxtEnd = squares[j]

                # confirm no intersection
                if curEnd[0] <= nxtStart[0] or curEnd[1] <= nxtStart[1]:
                    continue

                botL = [max(curStart[0], nxtStart[0]), max(curStart[1], nxtStart[1])]
                topR = [min(curEnd[0], nxtEnd[0]), min(curEnd[1], nxtEnd[1])]
                side = min(topR[0] - botL[0], topR[1] - botL[1])
                if side > 0:
                    res = max(res, side * side)
        return res
