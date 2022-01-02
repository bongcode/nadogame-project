# quiz) 하늘에서 떨어지는 똥 피하는 게임을 만드시오

#게임조건
#1. 캐릭터는 가장 아래에 위치, 좌우로만 이동가능
#2. 똥은 화면 가장위에서 떨어짐. x좌표는 매번 랜덤으로 설정
#3. 캐릭터가 똥을 피하면 다음 똥이 다시떨어짐
#4. 캐릭터가 똥과 충돌하면 "게임종료"
#5. FPS는 30으로 고정

#게임 이미지
#1. 배경: 640 * 480 - background.png
#2. 캐릭터: 70 * 70 - character.png
#3. 똥: 70 * 70 - enemy.png


import random
import pygame
#from pygame import key
#from pygame.constants import K_RIGHT

pygame.init()  # 반드시 필요한 작업!

# 화면크기 설정
screen_width = 480 # 스크린 가로크기
screen_height = 640 # 스크린 세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 크기설정

# 화면 타이틀 설정 
pygame.display.set_caption("Nado Game") # 게임 제목

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("/Users/songbong-geun/Desktop/pythonworkspace/pygame_basic/background2.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/songbong-geun/Desktop/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
charcter_y_pos = screen_height - character_height # 화면 세로의 크기 가장 아래에 해당하는 곳에 위치


# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 똥 만들기
ddong = pygame.image.load("/Users/songbong-geun/Desktop/pythonworkspace/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size # 이미지의 크기를 구해옴
ddong_width = ddong_size[0] # 캐릭터의 가로크기
ddong_height = ddong_size[1] # 캐릭터의 세로크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)


# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수

   # print("fps : "+ str(clock.get_fps()) ) # 초당 현재 fps 값

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(pygame에서는 반드시 작성해야하는 문구)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님     

        if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동
                to_x -= character_speed  # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로 이동
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 

    character_x_pos += to_x * dt
    charcter_y_pos += to_y * dt

  # 가로 경계값 처리(캐릭터가 화면 밖으로 나가지 않게 하기)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 좌표 오른쪽 아래에 그림이 그려지므로 값에서 캐릭터 크기 뻼
        character_x_pos = screen_width - character_width


    # 세로 경계값 처리
    if charcter_y_pos < 0: 
        charcter_y_pos = 0
    elif charcter_y_pos > screen_height - character_height:
        charcter_y_pos = screen_height - character_height

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
        


    # 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = charcter_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 충돌체크
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요") 
        running = False


    screen.blit(background, (0, 0)) # 배경 이미지를 불러와서 그리기
    screen.blit(character, (character_x_pos, charcter_y_pos)) # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) # 적 그리기 


    # 타이머 집어넣기
    # 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간을 1000으로 나누어 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자색상 
    screen.blit(timer, (10, 10))


    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
 

    # 잠시 대기
    #pygame.time.delay(2000)

    pygame.display.update() # 게임화면 다시그리기
    


# pygame 종료
pygame.quit()

