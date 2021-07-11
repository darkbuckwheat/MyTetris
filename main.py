import random                                  # let`s make a "true" random
from pieces import *                           # importing classes for creation pieces


def piece_stop():                              # function for turn piece into static block
    global a, piece, f, game_field
    try:
        x, y, sp = a.inf()[0], a.inf()[1], a.inf()[3]
        for i in range(len(sp[0])):
            for j in range(len(sp[0])):
                game_field[y + j][x + i] += sp[j][i]
    except Exception:
        pass
    a = 0
    piece = False
    f = False


def new_piece():
    p = random.choice(variants)
    if p == 'o':
        a = O(random.choice([2, 3, 4, 5, 6]), 21, 0)
    elif p == 'i':
        a = I(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    elif p == 't':
        a = T(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    elif p == 's':
        a = S(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    elif p == 'z':
        a = Z(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    elif p == 'l':
        a = L(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    elif p == 'j':
        a = J(random.choice([2, 3, 4, 5, 6]), 21, random.choice([0, 1, 2, 3]))
    return a


pygame.init()                                   # pygame things
screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

game_field = [[1] * 14]                         # game field creation
for i in range(25):
    game_field.append([0] * 10 + [1, 1, 1, 1])

variants = ['i', 'o', 't', 's', 'z', 'l', 'j']  # declaring variables
run = True
n = 1
mo = 0
f = False
t = False
score = 0
font = pygame.font.Font(None, 25)
flag = True
color = (0, 0, 255)

a = new_piece()                                 # creation start piece
piece = True

c = new_piece()                                 # creation future piece

while run:
    if 1 in game_field[20][:-4] and flag:       # game over check
        flag = False
        color = (255, 0, 0)

    u = 0                                       # full lines check and scoring
    while [1] * 14 in game_field[1:]:
        game_field.pop(game_field.index([1] * 14))
        game_field.append([0] * 10 + [1, 1, 1, 1])
        u += 1
    if u != 0:
        score += 100 * (u ** u)

    for event in pygame.event.get():            # event take
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                flag = True
                game_field = [[1] * 14]
                for i in range(25):
                    game_field.append([0] * 10 + [1, 1, 1, 1])
                n = 1
                mo = 0
                a = 0
                f = False
                t = False
                score = 0
                color = (0, 0, 255)

                a = new_piece()
                piece = True

                c = new_piece()
            elif event.key == pygame.K_d and piece:
                mo = 1
            elif event.key == pygame.K_a and piece:
                mo = -1
            elif event.key == pygame.K_w and piece:
                t = True
            elif event.key == pygame.K_s and piece:
                f = True
        elif event.type == pygame.KEYUP and piece:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                mo = 0
            elif event.key == pygame.K_s:
                f = False

    screen.fill((0, 0, 0))                      # screen update

    if piece and n % 5 == 0:                    # working wise current piece and creation new, if necessary
        n = 1
        b = a.fall(game_field)
        if b == 1:
            piece_stop()
        else:
            a.draw(screen)
    elif piece and f:
        b = a.fall(game_field)
        if b == 1:
            piece_stop()
        else:
            a.draw(screen)
    elif piece and t:
        a.turn(game_field)
        t = False
        a.draw(screen)
    elif piece:
        n += 1
        a.move(mo, game_field)
        a.draw(screen)
    elif flag:
        p = random.choice(variants)
        a = c
        piece = True
        c = new_piece()

    for i in range(19):                         # drawing the game field
        pygame.draw.line(screen, (255, 255, 255), [13, 12 + (i + 1) * 31], [323, 12 + (i + 1) * 31], 1)
    for i in range(9):
        pygame.draw.line(screen, (255, 255, 255), [12 + (i + 1) * 31, 13], [12 + (i + 1) * 31, 632], 1)
    for i in range(1, len(game_field)):
        for j in range(len(game_field[i]) - 4):
            if game_field[i][j] == 1:
                pygame.draw.rect(screen, color, [13 + j * 31, 633 - i * 31, 30, 30], 0)

    pygame.draw.rect(screen, (255, 255, 255), [10, 10, 315, 625], 3, 1)     # some workarounds here
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, 330, 10], 0, 0)

    text = font.render('NEXT PIECE', True, (255, 255, 255))                 # visualising next piece
    screen.blit(text, [380, 280])
    pygame.draw.rect(screen, (255, 255, 255), [350, 325, 169, 169], 3, 1)
    for i in range(3):
        pygame.draw.line(screen, (255, 255, 255), [353, 327 + (i + 1) * 41], [516, 327 + (i + 1) * 41], 1)
    for i in range(3):
        pygame.draw.line(screen, (255, 255, 255), [352 + (i + 1) * 41, 328], [352 + (i + 1) * 41, 491], 1)
    mat = c.inf()[-1]
    if mat == 'o':
        mat = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    elif mat == 'i':
        mat = imat[0]
    elif mat == 't':
        mat = tmat[0]
    elif mat == 's':
        mat = smat[0]
    elif mat == 'z':
        mat = zmat[0]
    elif mat == 'l':
        mat = lmat[0]
    elif mat == 'j':
        mat = jmat[0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                pygame.draw.rect(screen, (255, 0, 255), [353 + j * 41, 328 + (len(mat) - i - 1) * 41, 40, 40], 0)

    text = font.render(f"SCORE: {score}", True, (255, 255, 255))            # printing information for player
    screen.blit(text, [340, 20])
    text = font.render('CONTROLS:', True, (255, 255, 255))
    screen.blit(text, [380, 60])
    text = font.render('W - turn piece clockwise', True, (255, 255, 255))
    screen.blit(text, [340, 90])
    text = font.render('A - move piece left', True, (255, 255, 255))
    screen.blit(text, [340, 120])
    text = font.render('S - forced drop', True, (255, 255, 255))
    screen.blit(text, [340, 150])
    text = font.render('D - move piece right', True, (255, 255, 255))
    screen.blit(text, [340, 180])
    text = font.render('R - restart the game', True, (255, 255, 255))
    screen.blit(text, [340, 210])

    if not flag:                  # GAME OVER lettering
        fo = pygame.font.Font(None, 75)
        text = fo.render('GAME OVER', True, pygame.color.Color('yellow'))
        screen.blit(text, [115, 275])

    clock.tick(20)                # FPS control
    pygame.display.flip()         # updating display
pygame.quit()
