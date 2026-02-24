class Hanoi:
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c
        self.N = len(ke)

    def célteszt(self,a): #a= (a1,a2,.....,an)
        return a == self.cél

    def rákövetkező(self,a):
        gyerekek = []
        for melyiket in range(0,self.N):
            for hova in ['P','Q','R']:
                tmp = True #feltételezem hogy az opreátor alkalmazható
                if a[melyiket] != hova:
                    for i in range(0,melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            pass
                        else:
                            tmp = False
                            break
                else:
                    tmp = False

                if tmp:
                    uj_allapot = list(a)
                    uj_allapot[melyiket] = hova
                    gyerekek.append(tuple(uj_allapot))
                    
        return gyerekek



if __name__ == '__main__':
    feladat = Hanoi(('P','P','P','P','P'),('R','R','R','R','R'))