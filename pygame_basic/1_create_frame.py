import pygame

pygame.init()  # 반드시 필요한 작업!

#화면크기 설정
screen_width = 480 # 스크린 가로크기
screen_height = 640 # 스크린 세로크기
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기설정

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 제목
