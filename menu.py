import pygame, sys
from button import Button

pygame.init()
WIDTH,HEIGHT = 500,400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Face Recognition Attendance System (18CS35, 18CS15, 18CS101)")

BG = pygame.image.load("assets/Background2.jpg")
BG = pygame.transform.scale(BG,(WIDTH,HEIGHT))

Muet = pygame.image.load("assets/Muet.png")
# Muet_logo = pygame.image.load("assets/muet logo.jpg")
pygame.display.set_icon(Muet)
Muet = pygame.transform.scale(Muet,(130,130))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    import main
    


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(65).render("MAIN MENU", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 300), 
                            text_input="START", font=get_font(35), base_color="#d7fcd4", hovering_color="green")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
        #                     text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(460, 500), 
                            text_input="REGISTER FACE", font=get_font(35), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
              
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    import Cam

        SCREEN.blit(Muet,(10,30))
        pygame.display.update()

main_menu()
