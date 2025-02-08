# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def solve(root):
            if root:
                return f"{root.val}({solve(root.left)})({solve(root.right)})"
            return ""

        return solve(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = list(data)
        data.reverse()
        i = 0
        while i < len(data):
            if data[i] == '(':
                data[i] = ')'
            elif data[i] == ')':
                data[i] = '('
            i += 1
        # print(data)

        def solve(data: list[str]):
            if data:
                number = 0
                sign = 1
                if data[-1] == '-':
                    sign = -1
                    data.pop()
                while data[-1] != ")":
                    number = number * 10 + int(data.pop())
                number *= sign
                node = TreeNode(number)
                count = 0
                i = 0
                while i < len(data):
                    if data[i] == "(":
                        count += 1
                    elif data[i] == ")":
                        count -= 1
                    if count == 0:
                        break
                    i += 1
                node.left = solve(data[i + 2 : -1])
                node.right = solve(data[1:i])
                return node
            return None

        return solve(data)


# Your Codec object will be instantiated and called as such:
ser = Codec()
ser.deserialize('1(2()())(3(4()())(5()()))')
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
