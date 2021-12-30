import pygame

pygame.init()  # 반드시 필요한 작업!

# 화면크기 설정
screen_width = 480 # 스크린 가로크기
screen_height = 640 # 스크린 세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기설정

# 화면 타이틀 설정 
pygame.display.set_caption("Nado Game") # 게임 제목

# 배경 이미지 불러오기
background = pygame.image.load("/Users/songbong-geun/Desktop/pythonworkspace/pygame_basic/background2.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/songbong-geun/Desktop/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
charcter_y_pos = screen_height - character_height # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(pygame에서는 반드시 작성해야하는 문구)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님             

    screen.blit(background, (0, 0)) # 배경 이미지를 불러와서 그리기

    screen.blit(character, (character_x_pos, charcter_y_pos))

    pygame.display.update() # 게임화면 다시그리기
    


# pygame 종료
pygame.quit()
