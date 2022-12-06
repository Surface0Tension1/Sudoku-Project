import pygame
from board import Board
from board import Cell
from sudoku_generator import *

pygame.init()

# constants for color and pixel height/width
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

# pygame specific constants
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Sudoku')
font = pygame.font.Font('freesansbold.ttf', 32)

# variables that hold the current state of the game which allows different inputs at different points
running = True
main_menu = True
game_phase = False
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # terminates the loop and subsequently ends the program when the game window is closed
            running = False
        
        # performs specified actions (creating board object) if main menu is true and mouse clicks specificed area (button)
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
                
        # stores mouse position for user inputs/ changing button colors if hovered over
        mouse = pygame.mouse.get_pos()
        
        # creates simple white background
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
            '''
            Title: Python | Display text to PyGame window
            Author: Geeksforgeeks
            Date: Apr. 9, 2022
            Code Version: Python
            Availability: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
            '''
        elif main_menu:
            # the change in text color lets you know when you're hovering over the button
            textE = font.render('Easy', True, blue, grey)
            textRectE = textE.get_rect()
            textRectE.center = (width // 4, IncrementH)
            screen.blit(textE, textRectE)
            
        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and IncrementH - 25 <= mouse[1] <= IncrementH + 25\
                and main_menu:
            textM = font.render('Medium', True, light_blue, grey)
            textRectM = textM.get_rect()
            textRectM.center = (width // 2, IncrementH)
            screen.blit(textM, textRectM)
            
        elif main_menu:
            textM = font.render('Medium', True, blue, grey)
            textRectM = textM.get_rect()
            textRectM.center = (width // 2, IncrementH)
            screen.blit(textM, textRectM)
            
        if width / 4 * 3 - 70 <= mouse[0] <= width / 4*3 + 70 and IncrementH - 25 <= mouse[1] <= IncrementH + 25\
                and main_menu:
            textH = font.render('Hard', True, light_blue, grey)
            textRectH = textH.get_rect()
            textRectH.center = (width // 4 * 3, IncrementH)
            screen.blit(textH, textRectH)
            
        elif main_menu:
            textH = font.render('Hard', True, blue, grey)
            textRectH = textH.get_rect()
            textRectH.center = (width // 4 * 3, IncrementH)
            screen.blit(textH, textRectH)
            
        if game_phase:
            # draws the screen (includes the borders and every cell)
            board.draw(screen)

            if width / 4 - 70 <= mouse[0] <= width / 4 + 70 and GameButtonHeight - 25 <= mouse[1] <= GameButtonHeight + 25:
                # adds the reset button on the game screen
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
                # adds the restart button on the game screen
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
                # adds the quit button to the game screen
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
                    # this conditional is set so that the select method only functions
                    # if you click within the bounds of the playable area
                    board.select(x, y)
                if IncrementW - 70 <= mouse[0] <= IncrementW + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    # this location pertains to the reset button
                    # when the mouse in the area of the reset button and is clicked,
                    # the board resets to its original state
                    board.reset_to_original()
                if IncrementW * 2 - 70 <= mouse[0] <= IncrementW * 2 + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    # this location pertains to the restart button
                    # when the mouse in the area of the restart button and is clicked,
                    # the program turns off the game_phase and turns on main menu
                    # when the program loops because it's still running,
                    # the program displays the main menu instead of the game board
                    game_phase = False
                    main_menu = True
                if IncrementW * 3 - 70 <= mouse[0] <= IncrementW * 3 + 70 and GameButtonHeight - 25 <= mouse[1]\
                        <= GameButtonHeight + 25:
                    # this location pertains to the quit button
                    # when the mouse in the area of the quit button and is clicked,
                    # the program terminates and the game window is closed
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                # these events cover every keypress that the user should be making
                if pygame.key.get_pressed()[pygame.K_1]:
                    # for all number key presses, the program sketches that key's number value into the cell
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
                    # when backspace is pressed, the program sets the cell value and sketch value of the cell to 0
                    # unless that cell was provided by the sudoku generator
                    board.clear()
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    # when the enter key is pressed, the program set the cell value equal to the sketched value of the
                    # currently selected cell
                    x, y = board.selected
                    board.place_number(board.cells[x][y].sketch_value)
                    # the program checks if the board is full after every enter key press
                    # if the board is full, the game_phase is turned off and the program advances to the game_over phase
                    if board.is_full():
                        game_phase = False
                        game_over = True
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    # these arrow key presses allow the user to select an adjacent cell to the currently selected cell
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
            # check_board() returns True or False depending on if the correct solution is evaluted 
            # this is then stored in win
            win = board.check_board()
            if win:
                # displays 'win' text if there is the win condition
                # also displays a single 'Exit' button in order to stop the program using same method as prior
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
                # this occurs when 'win' returns false and will start the lose condition
                # will display 'Lose' text object followed by a 'restart' button with the same functionality as before 
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
                        # when main_menu is set to true, the user will be brought to the main_menu state based on the main_menu conditionals
                        # fundtions the same as prior restart button
                        game_over = False
                        main_menu = True

        pygame.display.flip()
        # updates the display every loop
pygame.quit()
