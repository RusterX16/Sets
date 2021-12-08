class Natural:
    def __init__(self, li):
        for i in range(len(li)):
            if i < 0:
                raise AttributeError("Natural integer cannot be negative")
        self.li = li

    def __contains__(self, item):
        for i in range(len(self.li)):
            if i == item:
                return True
        return False

    def union(self, li):
        res = []

        for i in range(len(li if li > self.li else self.li)):
            print(li.__gt__(i))
