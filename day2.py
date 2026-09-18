class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)

        frt, lst = [float('inf')] * 26, [-1] * 26

        for i in range(n):

            c = ord(s[i]) - ord('a')

            frt[c] = min(frt[c], i)
            lst[c] = i

        inter = []

        for c in range(26):

            if lst[c] == -1:
                continue

            l, r = frt[c], lst[c]
            val, i = True, l

            while i <= r:

                x = ord(s[i]) - ord('a')

                if frt[x] < l:
                    val = False
                    break

                r = max(r, lst[x])
                i += 1

            if val:
                inter.append((l, r))

        inter.sort(key=lambda x: x[1])

        ans, lst_end = [], -1

        for l, r in inter:

            if l > lst_end:

                ans.append(s[l:r + 1])
                lst_end = r

        return ans