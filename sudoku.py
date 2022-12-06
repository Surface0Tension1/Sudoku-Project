import pygame
from board import Board
from board import Cell
from sudoku_generator import *

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
grey = (100, 100, 100)
blue = (0, 0, 128)
light_blue = (65, 205, 255)
black = (0,0,0)
width = 500
height = 600
IncrementW = width/4
IncrementH = (height-100)/2
GameButtonHeight = IncrementH * 2.2

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Sudoku')
font = pygame.font.Font('freesansbold.ttf', 32)

running = True
main_menu = True
game_phase = False
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and main_menu:
            if IncrementW-70 <= mouse[0] <= IncrementW+70 and IncrementH-25 <= mouse[1] <= IncrementH+25:
                board = Board(9, 9, width, height-100, screen, 30)
                main_menu = False
                game_phase = True
            if IncrementW*2-70 <= mouse[0] <= IncrementW*2+70 and IncrementH-25 <= mouse[1] <= IncrementH+25:
                board = Board(9, 9, width, height-100, screen, 40)
                num_array = generate_sudoku(9, 40)
                for i in range(9):
                    for j in range(9):
                        board.cells[i][j].set_cell_value(num_array[i][j])
                main_menu = False
                game_phase = True
            if IncrementW * 3 - 70 <= mouse[0] <= IncrementW*3+70 and IncrementH-25 <= mouse[1] <= IncrementH+25:
                board = Board(9, 9, width, height-100, screen, 50)
                num_array = generate_sudoku(9, 50)
                for i in range(9):
                    for j in range(9):
                        board.cells[i][j].set_cell_value(num_array[i][j])
                main_menu = False
                game_phase = True

        mouse = pygame.mouse.get_pos()

        screen.fill(white)

        if width / 4 - 70 <= mouse[0] <= width / 4 + 70 and IncrementH - 25 <= mouse[1] <= IncrementH + 25\
                and main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textE = font.render('Easy', True, light_blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectE = textE.get_rect()
            textRectE.center = (width // 4, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textE, textRectE)
        elif main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textE = font.render('Easy', True, blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectE = textE.get_rect()
            textRectE.center = (width // 4, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textE, textRectE)
        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and IncrementH - 25 <= mouse[1] <= IncrementH + 25\
                and main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textM = font.render('Medium', True, light_blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectM = textM.get_rect()
            textRectM.center = (width // 2, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textM, textRectM)
        elif main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textM = font.render('Medium', True, blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectM = textM.get_rect()
            textRectM.center = (width // 2, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textM, textRectM)
        if width / 4 * 3 - 70 <= mouse[0] <= width / 4*3 + 70 and IncrementH - 25 <= mouse[1] <= IncrementH + 25\
                and main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textH = font.render('Hard', True, light_blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectH = textH.get_rect()
            textRectH.center = (width // 4 * 3, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textH, textRectH)
        elif main_menu:
            # create a text surface object,
            # on which text is drawn on it.
            textH = font.render('Hard', True, blue, grey)

            # create a rectangular object for the
            # text surface object
            textRectH = textH.get_rect()
            textRectH.center = (width // 4 * 3, IncrementH)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            screen.blit(textH, textRectH)
        if game_phase:
            board.draw(screen)

            if width / 4 - 70 <= mouse[0] <= width / 4 + 70 and GameButtonHeight - 25 <= mouse[1] <= GameButtonHeight + 25:

                text_reset = font.render('Reset', True, light_blue, grey)

                textRect_reset = text_reset.get_rect()
                textRect_reset.center = (width // 4, GameButtonHeight)

                screen.blit(text_reset, textRect_reset)

            else:
                text_reset = font.render('Reset', True, blue, grey)

                textRect_reset = text_reset.get_rect()
                textRect_reset.center = (width // 4, GameButtonHeight)

                screen.blit(text_reset, textRect_reset)

            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and GameButtonHeight - 25 <= mouse[1] <= GameButtonHeight + 25:

                text_restart = font.render('Restart', True, light_blue, grey)

                textRect_restart = text_restart.get_rect()
                textRect_restart.center = (width // 2, GameButtonHeight)

                screen.blit(text_restart, textRect_restart)

            else:
                text_restart = font.render('Restart', True, blue, grey)

                textRect_restart = text_restart.get_rect()
                textRect_restart.center = (width // 2, GameButtonHeight)

                screen.blit(text_restart, textRect_restart)

            if width / 4 * 3 - 70 <= mouse[0] <= width / 4 * 3 + 70 and GameButtonHeight - 25 <= mouse[1] <= GameButtonHeight + 25:

                text_quit = font.render('Quit', True, light_blue, grey)

                textRect_quit = text_quit.get_rect()
                textRect_quit.center = (width // 4 * 3, GameButtonHeight)

                screen.blit(text_quit, textRect_quit)

            else:
                text_quit = font.render('Quit', True, blue, grey)

                textRect_quit = text_quit.get_rect()
                textRect_quit.center = (width // 4 * 3, GameButtonHeight)

                screen.blit(text_quit, textRect_quit)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = board.click(mouse[0], mouse[1])
                if mouse[1] <= 500:
                    board.select(x, y)
                if IncrementW - 70 <= mouse[0] <= IncrementW + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    board.reset_to_original()
                if IncrementW * 2 - 70 <= mouse[0] <= IncrementW * 2 + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    game_phase = False
                    main_menu = True
                if IncrementW * 3 - 70 <= mouse[0] <= IncrementW * 3 + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1]:
                    board.sketch(1)
                if pygame.key.get_pressed()[pygame.K_2]:
                    board.sketch(2)
                if pygame.key.get_pressed()[pygame.K_3]:
                    board.sketch(3)
                if pygame.key.get_pressed()[pygame.K_4]:
                    board.sketch(4)
                if pygame.key.get_pressed()[pygame.K_5]:
                    board.sketch(5)
                if pygame.key.get_pressed()[pygame.K_6]:
                    board.sketch(6)
                if pygame.key.get_pressed()[pygame.K_7]:
                    board.sketch(7)
                if pygame.key.get_pressed()[pygame.K_8]:
                    board.sketch(8)
                if pygame.key.get_pressed()[pygame.K_9]:
                    board.sketch(9)
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    board.clear()
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    x, y = board.selected
                    board.place_number(board.cells[x][y].sketch_value)
                    if board.is_full():
                        game_phase = False
                        game_over = True
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    x, y = board.selected
                    if 0 < y:
                        board.select(x, y-1)
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    x, y = board.selected
                    if y < 8:
                        board.select(x, y+1)
                if pygame.key.get_pressed()[pygame.K_UP]:
                    x, y = board.selected
                    if 0 < x:
                        board.select(x - 1, y)
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    x, y = board.selected
                    if x < 8:
                        board.select(x+1, y)

        if game_over:
            win = board.check_board()
            if win:
                text_end = font.render('WIN', True, (0,0,0), grey)

                textRect_end = text_end.get_rect()
                textRect_end.center = (width // 2, IncrementH)

                screen.blit(text_end, textRect_end)

                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and GameButtonHeight - 25 <= mouse[
                    1] <= GameButtonHeight + 25 \
                        and game_phase:

                    text_exit = font.render('Exit', True, light_blue, grey)

                    textRect_exit = text_exit.get_rect()
                    textRect_exit.center = (width // 2, GameButtonHeight)

                    screen.blit(text_exit, textRect_exit)

                else:
                    text_exit = font.render('Exit', True, blue, grey)

                    textRect_exit = text_exit.get_rect()
                    textRect_exit.center = (width // 2, GameButtonHeight)

                    screen.blit(text_exit, textRect_exit)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if IncrementW * 2 - 70 <= mouse[0] <= IncrementW * 2 + 70 and GameButtonHeight - 25 <= mouse[1] \
                            <= GameButtonHeight + 25:
                        pygame.quit()
            else:
                text_end = font.render('LOSE', True, (0,0,0), grey)

                textRect_end = text_end.get_rect()
                textRect_end.center = (width // 2, IncrementH)

                screen.blit(text_end, textRect_end)
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and GameButtonHeight - 25 <= mouse[1] <= GameButtonHeight + 25:

                    text_restart = font.render('Restart', True, light_blue, grey)
                    textRect_restart = text_restart.get_rect()
                    textRect_restart.center = (width // 2, GameButtonHeight)
                    screen.blit(text_restart, textRect_restart)

                else:
                    text_restart = font.render('Restart', True, blue, grey)

                    textRect_restart = text_restart.get_rect()
                    textRect_restart.center = (width // 2, GameButtonHeight)

                    screen.blit(text_restart, textRect_restart)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if IncrementW * 2 - 70 <= mouse[0] <= IncrementW * 2 + 70 and GameButtonHeight - 25 <= mouse[1] \
                            <= GameButtonHeight + 25:
                        game_over = False
                        main_menu = True

        pygame.display.flip()
pygame.quit()

