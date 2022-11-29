class RandomizedSet:

    def __init__(self):
        self.r_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.r_set:
            self.r_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.r_set:
            self.r_set.remove(val)
            return True
        return False
            
    def getRandom(self) -> int:
        return random.choice(list(self.r_set))
