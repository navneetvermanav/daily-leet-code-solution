class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        def build():
            curr = 1
            for num in target:
                yield 'Push'
                while curr < num:
                    yield from ('Pop', 'Push')
                    curr += 1
                curr += 1
        return list(build())