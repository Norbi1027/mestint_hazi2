class Kiralyno:
    def __init__(self,ke,c):
        self.kezdő = ke
        self.cél = c
        self.N = len(ke)-1

    def célteszt(self,a): #a=(a1,a2,a3....,an,s)
        return a[self.N] == self.cél #s==N+1(cél)

    def rákövetkező(self,a): #a=(a1,a2,a3....,an,s)
        gyerekek = []
        s = a[self.N] #következő sor indexe
        for i in range(1,self.N+1):
            előfeltétel = True #lerak (s,i) ???
            for m in range(1,s): #minden m<s:
                if a[m-1] != i and abs(s-m) != abs(i-a[m-1]):
                    pass
                else:
                    előfeltétel = False
                    break
        if előfeltétel:
            uj_allapot = list(a)
            uj_allapot[s-1] = i
            uj_allapot[self.N] = s+1 #s = s+1
            gyerekek.append(tuple(uj_allapot))

        return gyerekek




if __name__ == '__main__':
    feladat1 = Kiralyno((0,0,0,1),5)
    feladat2 = Kiralyno((0,0,0,0,0,0,0,0,1),9)

