class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        print(paths)
        st = []
        for path in paths:
            if not st and path == '..':
                continue
            if not st:
                st.append(path)
            elif path:
                if path == '..':
                    st.pop()
                elif path == '.':
                    continue
                else:
                    st.append(path)
        result = "/".join(st)
        result.startswith
        return "/".join(st)