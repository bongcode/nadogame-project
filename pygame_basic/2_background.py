import pygame

pygame.init()  # 반드시 필요한 작업!

# 화면크기 설정
screen_width = 480 # 스크린 가로크기
screen_height = 640 # 스크린 세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기설정

# 화면 타이틀 설정 
pygame.display.set_caption("Nado Game") # 게임 제목

# 배경 이미지 불러오기
#background = pygame.image.load()

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(pygame에서는 반드시 작성해야하는 문구)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님             

    #screen.blit(background, (0, 0)) # 배경 이미지를 불러와서 그리기
    screen.fill((0, 255, 255)) # 배경에 색을 기입, (R,G,B)순
    
    pygame.display.update() # 게임화면 다시그리기
    


# pygame 종료
pygame.quit()
