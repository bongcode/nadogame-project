import pygame
import os
################################################################################

# 기본 초기화(반드시 해야하는 부분) 
pygame.init()  # 반드시 필요한 작업!
 
# 화면크기 설정
screen_width = 640 # 스크린 가로크기
screen_height = 480 # 스크린 세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기설정

# 화면 타이틀 설정 
pygame.display.set_caption("BONG PANG") # 게임 제목

# FPS
clock = pygame.time.Clock()

################################################################################

# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 설정 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 위치시키기 위해 사용

#캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_height = character_size[1]
character_width = character_size[0]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수

   # print("fps : "+ str(clock.get_fps()) ) # 초당 현재 fps 값

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(pygame에서는 반드시 작성해야하는 문구)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님     

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
  
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
 
    pygame.display.update() # 게임화면 다시그리기

# pygame 종료
pygame.quit()
