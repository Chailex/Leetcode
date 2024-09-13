# Solution using fast and slow pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        def square_sum(x):
            sum = 0
            while x > 0:
                y = x % 10
                sum += y**2
                x = x//10
            return sum

        while True:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))

            if slow == 1 or fast == 1:
                return True
            if fast == slow:
                return False


# Solution using set()
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def square_sum(x):
            sum = 0
            while x > 0:
                y = x % 10
                sum += y**2
                x = x//10
            return sum

        while True:
            n = square_sum(n)
            if n in visited:
                return False
            if n == 1:
                return True
            visited.add(n)
