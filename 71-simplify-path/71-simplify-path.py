class Solution:
    def simplifyPath(self, path: str) -> str:
        dirList = []
        
        for directory in path.split('/') :
            if not directory or directory == ".":
                continue
            if directory == "..":
                if dirList:
                    dirList.pop()
            else:
                dirList.append(directory)
                
        res = "/"
        for directory in dirList:
            res += directory
            res += "/"
        return res[:-1] if res != "/" else "/"