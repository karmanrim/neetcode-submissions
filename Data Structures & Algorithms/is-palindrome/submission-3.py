class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(e for e in s if e.isalnum())
        st = st.lower()
        start_iter = 0
        end_iter = -1
        while True:
            if len(st) == 0:
                return True
            if st[start_iter] == st[end_iter]:
                start_iter += 1
                end_iter -= 1
                if len(st) + end_iter - start_iter <= 0:
                    break
            else:
                return False

        return True