import pygame
import requests
import argparse
from get_params import get_params

parser = argparse.ArgumentParser()
parser.add_argument('--coords', nargs=2, type=str)
parser.add_argument('--spn', type=float)
parser.add_argument('--value', type=float)

coords = parser.parse_args().coords
spn = parser.parse_args().spn
value = parser.parse_args().value

map_api_server = "http://static-maps.yandex.ru/1.x/"

pygame.init()
screen = pygame.display.set_mode((600, 450))


def check_key_event():
    global spn, value
    if pygame.key.get_pressed()[pygame.K_PAGEUP]:
        if spn < 90:
            spn += value
    if pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
        if spn > 0:
            spn -= value


def show_picture():
    response = requests.get(map_api_server, params=get_params(','.join(coords), str(spn) + ',' + str(spn)))
    file = open('file.png', 'wb')
    file.write(response.content)
    screen.blit(pygame.image.load('file.png'), (0, 0))


while pygame.event.wait().type != pygame.QUIT:
    print(spn)
    check_key_event()
    show_picture()
    pygame.display.update()
