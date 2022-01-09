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


# 공 만들기(4개 크기에 대해 따로 처리)
ball_images = [     
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]


# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #index 0,1,2,3에 해당하는 값


# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50, # 공의 y좌표
    "img_idx" : 0, # 공의 이미지 index
    "to_x" : 3, #공의 x축 이동방향, -3이면 왼쪽으로, +3이면 오른쪽으로 이동
    "to_y" : -6, # y축 이동방향
    "init_spd_y" :  ball_speed_y[0]})  # y 최초 속도


# 사라질 무기, 공 정보 저장변수
weapon_to_remove = -1
ball_to_remove = -1


# font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작시간 정의


# 게임종료 메시지 / Time out, Mission Complete, Game Over
game_result = "Game Over"


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

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 공이 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_val["to_x"] = ball_val["to_x"] * -1


        # 세로 위치
        # 스테이지에 닿은 후 튕겨서 다시 올라가는 모양(처음만)
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
        

    # 4. 충돌 처리

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터의 충돌체크
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들의 충돌체크
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기를 없애기 위한 값설정
                ball_to_remove = ball_idx # 해당 공을 없애기 위한 값설정

                #가장 작은 크기의 공이 아니라면, 다음 작은 단계의 공으로 나누어 주는 처리
                if ball_img_idx < 3:
                    # 현재 공 크기의 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공의 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 index
                        "to_x" : -3, #공의 x축 이동방향, -3이면 왼쪽으로, +3이면 오른쪽으로 이동
                        "to_y" : -6, # y축 이동방향
                        "init_spd_y" :  ball_speed_y[ball_img_idx + 1]})  # y 최초 속도

                    # 오른쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 index
                        "to_x" : 3, #공의 x축 이동방향, -3이면 왼쪽으로, +3이면 오른쪽으로 이동
                        "to_y" : -6, # y축 이동방향
                        "init_spd_y" :  ball_speed_y[ball_img_idx + 1]})  # y 최초 속도

                break

    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


  
    # 5. 화면에 그리기(작성한 순서에 따라서 표시됨 / 배경-무대-캐릭터-무기 순이면 해당과 같이 pygame에서는 인식함)
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s단위로 변경
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))


    # 시간을 초과했다면
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update() # 게임화면 다시그리기

# 게임오버 메시지 저장
msg = game_font.render(game_result, True, (255, 255, 0)) #노란색
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update() # 게임화면 다시그리기

pygame.time.delay(2000)


# pygame 종료
pygame.quit()
