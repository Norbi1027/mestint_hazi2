class Kiralyno:
    def __init__(self, ke, c):
        self.kezdő = ke      # mátrix
        self.cél = c         # N+1
        self.N = len(ke)

    def célteszt(self, a):  # a = (matrix, s)
        matrix, s = a
        return s == self.cél

    def rákövetkező(self, a):  # a = (matrix, s)
        gyerekek = []
        matrix, s = a

        for i in range(self.N):  # oszlop
            előfeltétel = True

            # oszlop ellenőrzés
            for r in range(s-1):
                if matrix[r][i] == 1:
                    előfeltétel = False
                    break

            # bal felső átló
            r, c = s-2, i-1
            while r >= 0 and c >= 0 and előfeltétel:
                if matrix[r][c] == 1:
                    előfeltétel = False
                r -= 1
                c -= 1

            # jobb felső átló
            r, c = s-2, i+1
            while r >= 0 and c < self.N and előfeltétel:
                if matrix[r][c] == 1:
                    előfeltétel = False
                r -= 1
                c += 1

            if előfeltétel:
                uj_matrix = [row[:] for row in matrix]
                uj_matrix[s-1][i] = 1

                gyerekek.append((uj_matrix, s+1))

        return gyerekek


if __name__ == '__main__':

    kezdo4 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    feladat1 = Kiralyno(kezdo4, 5)