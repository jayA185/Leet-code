from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        answer = 1

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Keep sign consistent
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            answer = max(answer, max(slopes.values(), default=0) + 1)

        return answer