class KancsoFeladat:
    def __init__(self,ke,c,max):
        self.kezdő = ke
        self.cél = c
        self.MAX = max

    def célteszt(self,a): #a = (a1,a2,a3) állapot
        return a[0] == self.cél or a[1] == self.cél or a[2] == self.cél

    def rákövetkező(self,a): #a = (a1,a2,a3) állapot

        gyerekek = []
        a1,a2,a3 = a
        max1,max2,max3 = self.MAX

        #tölt 1,2 alkalmazási előfeltétel:
        if a1 != 0 and a2 != max2:
            T = min(a1,max(max2-a2))
        gyerekek.append(("tölt 1->2",(a1-T,a2+T,a3)))

        # tölt 1,3 alkalmazási előfeltétel:
        if a1 != 0 and a3 != max3:
             T = min(a1, max(max3 - a3))
        gyerekek.append(("tölt 1->3", (a1 - T, a2, a3 + T)))

        # tölt 2,1 alkalmazási előfeltétel:
        if a2 != 0 and a1 != max1:
            T = min(a2, max(max1 - a1))
        gyerekek.append(("tölt 2->1", (a1 + T, a2 - T, a3)))

        # tölt 2,3 alkalmazási előfeltétel:
        if a2 != 0 and a3 != max3:
            T = min(a2, max(max3 - a3))
        gyerekek.append(("tölt 2->3", (a1, a2 - T, a3 + T)))

        # tölt 3,1 alkalmazási előfeltétel:
        if a3 != 0 and a1 != max1:
            T = min(a3, max(max1 - a1))
        gyerekek.append(("tölt 3->1", (a1 + T, a2, a3 - T)))

        # tölt 3,2 alkalmazási előfeltétel:
        if a3 != 0 and a2 != max2:
            T = min(a3, max(max2 - a2))
        gyerekek.append(("tölt 3->2", (a1, a2 + T, a3 - T)))

        return gyerekek

if __name__ == '__main__':
    feladat = KancsoFeladat((0,0,8),4,(3,5,8))
