class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(lst):
            for i in lst:
                if i.isInteger() == False:
                    for j in flatten(i.getList()):
                        yield j
                else:
                    yield i.getInteger()
        
        self.lst = (list(flatten(nestedList)))
        self.len_lst = len(self.lst)
        self.idx = 0
    
    def next(self) -> int:
        self.idx += 1
        return self.lst[self.idx-1]

    
    def hasNext(self) -> bool:
        if self.idx < self.len_lst:
            return True
        return False