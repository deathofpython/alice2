import pygame
import requests
import argparse
from params import get_map_params

parser = argparse.ArgumentParser()

parser.add_argument('--coords', nargs=2, type=float)
parser.add_argument('--spn', type=float)
parser.add_argument('--value', type=float)

coords = parser.parse_args().coords
spn = parser.parse_args().spn
value = parser.parse_args().value
dx = 10
dy = 10

map_api_server = "http://static-maps.yandex.ru/1.x/"

pygame.init()
screen = pygame.display.set_mode((600, 450))


def check_key_event():
    global spn, value, dx, dy
    if pygame.key.get_pressed()[pygame.K_PAGEUP]:
        if spn < 90:
            spn += value
    if pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
        if spn > 0:
            spn -= value

    if pygame.key.get_pressed()[pygame.K_UP]:
        if coords[1] != 80:
            coords[1] += dy
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if coords[1] != -80:
            coords[1] -= dy
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if coords[0] != 170:
            coords[0] += dx
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if coords[0] != -180:
            coords[0] -= dx


def show_picture():
    response = requests.get(map_api_server, params=get_map_params(','.join([str(coords[0]), str(coords[1])]), str(spn) + ',' + str(spn)))
    file = open('file.png', 'wb')
    file.write(response.content)
    screen.blit(pygame.image.load('file.png'), (0, 0))


while pygame.event.wait().type != pygame.QUIT:
    check_key_event()
    show_picture()
    pygame.display.update()
