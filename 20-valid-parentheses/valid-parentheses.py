class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # Opening brackets
            if ch in "({[":
                stack.append(ch)

            # Closing brackets
            else:
                # Stack empty or mismatch
                if not stack or stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0