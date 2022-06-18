class WordFilter:
    def __init__(self, words: List[str]):
        self.keep = {}
        for i in range(len(words)):
            le = len(words[i])
            for j in range(1,min(11,le+1)):
                pre = words[i][:j]
                if pre not in self.keep:
                    self.keep[pre] = {}
                for k in range(1,min(11,le+1)):
                    suf = words[i][le-k:]
                    self.keep[pre][suf] = i

    def f(self, prefix: str, suffix: str) -> int:
        if prefix not in self.keep or suffix not in self.keep[prefix]:return -1
        return self.keep[prefix][suffix]