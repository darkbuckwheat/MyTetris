import pygame       # the most important import in these project

                    # There are some matrices for pieces
imat = ([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
        [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
        [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]])

tmat = ([[0, 0, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0]])

smat = ([[0, 0, 0], [1, 1, 0], [0, 1, 1]],
        [[0, 0, 1], [0, 1, 1], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [1, 1, 0], [1, 0, 0]])

zmat = ([[0, 0, 0], [0, 1, 1], [1, 1, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
        [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]])

lmat = ([[1, 0, 0], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
        [[0, 1, 1], [0, 1, 0], [0, 1, 0]])

jmat = ([[0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1]])


                    # parent class and unice classes for every kind of piece
class Piece:
    def __init__(self, x, y, grad):
        self.x = x
        self.y = y
        self.grad = grad
        self.space = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.name = 'none'

    def turn(self, field):
        if self.check_turn(0, field):
            self.space = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def move(self, m, field):
        if self.check_move(m, field):
            self.x += m

    def fall(self, field):
        if self.check_fall(field):
            self.y -= 1
            return 0
        else:
            return 1

    def draw(self, screen):
        for i in range(len(self.space[0])):
            for j in range(len(self.space[0])):
                if self.space[j][i] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), [13 + (self.x + i) * 31, 633 - (self.y + j) * 31, 30, 30], 0)

    def check_move(self, m, field):
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(self.space[i][j] + field[self.y + i][self.x + j + m])
            if 2 in a:
                return False
        return True

    def check_fall(self, field):
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(self.space[i][j] + field[self.y - 1 + i][self.x + j])
            if 2 in a:
                return False
        return True

    def check_turn(self, n, field):
        return False

    def inf(self):
        return (self.x, self.y, self.grad, self.space, self.name)


class O(Piece):
    def __init__(self, x, y, grad):
        super().__init__(x, y, grad)
        self.space = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.name = 'o'


class I(Piece):
    def __init__(self, x, y, grad):
        global imat
        super().__init__(x, y, grad)
        self.space = imat[self.grad]
        self.name = 'i'

    def turn(self, field):
        global imat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = imat[n]
            self.grad = n

    def check_turn(self, n, field):
        global imat
        sp = imat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True


class T(Piece):
    def __init__(self, x, y, grad):
        global tmat
        super().__init__(x, y, grad)
        self.space = tmat[self.grad]
        self.name = 't'

    def turn(self, field):
        global tmat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = tmat[n]
            self.grad = n

    def check_turn(self, n, field):
        global tmat
        sp = tmat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True


class S(Piece):
    def __init__(self, x, y, grad):
        global smat
        super().__init__(x, y, grad)
        self.space = smat[self.grad]
        self.name = 's'

    def turn(self, field):
        global smat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = smat[n]
            self.grad = n

    def check_turn(self, n, field):
        global smat
        sp = smat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True


class Z(Piece):
    def __init__(self, x, y, grad):
        global zmat
        super().__init__(x, y, grad)
        self.space = zmat[self.grad]
        self.name = 'z'

    def turn(self, field):
        global zmat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = zmat[n]
            self.grad = n

    def check_turn(self, n, field):
        global zmat
        sp = zmat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True


class L(Piece):
    def __init__(self, x, y, grad):
        global lmat
        super().__init__(x, y, grad)
        self.space = lmat[self.grad]
        self.name = 'l'

    def turn(self, field):
        global lmat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = lmat[n]
            self.grad = n

    def check_turn(self, n, field):
        global lmat
        sp = lmat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True


class J(Piece):
    def __init__(self, x, y, grad):
        global jmat
        super().__init__(x, y, grad)
        self.space = jmat[self.grad]
        self.name = 'j'

    def turn(self, field):
        global jmat
        n = self.grad + 1
        if n == 4:
            n = 0
        if self.check_turn(n, field):
            self.space = jmat[n]
            self.grad = n

    def check_turn(self, n, field):
        global jmat
        sp = jmat[n]
        for i in range(len(self.space[0])):
            a = []
            for j in range(len(self.space[0])):
                a.append(sp[i][j] + field[self.y + i][self.x + j])
            if 2 in a:
                return False
        return True