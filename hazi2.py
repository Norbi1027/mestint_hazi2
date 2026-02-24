class KancsoFeladat:
    def __init__(self, ke, c, max):
        self.kezdo = ke
        self.cel = c
        self.MAX = max

    def celteszt(self, a):  # a = (a1,a2,a3) állapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a):  # a = (a1,a2,a3) állapot
        gyerekek = []
        maxok = self.MAX

        for forras in range(3):
            for cel in range(3):
                if forras != cel and a[forras] != 0 and a[cel] != maxok[cel]:

                    T = min(a[forras], maxok[cel] - a[cel])

                    uj_allapot = list(a)
                    uj_allapot[forras] -= T
                    uj_allapot[cel] += T

                    gyerekek.append(
                        (f"tölt {forras+1}->{cel+1}", tuple(uj_allapot))
                    )

        return gyerekek


if __name__ == '__main__':
    feladat = KancsoFeladat((0, 0, 8), 4, (3, 5, 8))