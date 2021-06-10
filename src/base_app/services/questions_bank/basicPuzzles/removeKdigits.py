class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in num:
            while stack and k and stack[-1] > x:
                print("stack[-1]", stack[-1], "stack: ", stack)
                stack.pop()
                k -= 1
            stack.append(x)
            print("stack: ", stack)
            
        print("******stack[:len(stack)-k]", stack[:len(stack)-k])
        return "".join(stack[:len(stack)-k]).lstrip("0") or "0"


if __name__ == "__main__":
    s1 = Solution()
    # num = "1432219", k = 3
    # Output: "1219"
    k = 3
    ip_list = ["1432219", "14322191"]
    op_list = ["1219", "12191"]
    assert s1.removeKdigits(ip_list[0], k) == op_list[0]
    print(s1.removeKdigits(ip_list[0], k))
    for ip, op in zip(ip_list, op_list):
        assert s1.removeKdigits(ip, k) == op
        # break
