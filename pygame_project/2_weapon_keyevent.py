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

# 캐릭터 이동방향
character_to_x = 0

# 캐릭터 이동속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러개 발사 가능조건
weapons = []

# 무기 이동속도
weapon_speed = 10



# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수

   # print("fps : "+ str(clock.get_fps()) ) # 초당 현재 fps 값

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?(pygame에서는 반드시 작성해야하는 문구)
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가??
            running = False  # 게임이 진행중이 아님     

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기를 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # <무기 위치조정>
    # x, y 라고 할때 100, 200인 경우 x값인 100은 변함이 없지만, y값인 200은 weapon_speed에 맞춰 감소한다
    # 100, 200 -> 190 / 180 / 170 / 160 ....
    # 500, 200 -> 190 / 180 / 170 / 160 ....
    weapons = [ [w[0], w[1] - weapon_speed ] for w in weapons] 
       # 무기가 위로 나가게끔 위치를 조정(weapons 리스트에서 값을 뽑아내서 w로 작성하고 그 w값의 [0],[1]번째에서 weapon_speed를 뺀 것임)

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ]


    
    # 4. 충돌 처리
  
    # 5. 화면에 그리기(작성한 순서에 따라서 표시됨 / 배경-무대-캐릭터-무기 순이면 해당과 같이 pygame에서는 인식함)
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    

    pygame.display.update() # 게임화면 다시그리기

# pygame 종료
pygame.quit()
