#!/usr/bin/env python
"""
https://en.wikipedia.org/wiki/Quindar_tones
"""
import quindar_tones
import pygame
import numpy as np
from time import sleep
pygame.display.init()
pygame.display.set_mode((500, 40))
pygame.display.set_caption('Quindar: Left/right. ToneRemote: Up.  Nextel: Down.')


def main():
    """
    In a real program, the "while True" would be asyncio / thread
    """
    S0, S1 = quindar_tones.genquindar()
    Sr = quindar_tones.gentoneremote()
    Sn = quindar_tones.nextel_chirp()

    print('Press Esc to stop')

    while True:
        sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                on_press(event, S0, S1, Sr, Sn)


def on_press(e, S0: np.ndarray, S1: np.ndarray, Sr: np.ndarray, Sn: np.ndarray):
    """https://www.pygame.org/docs/ref/key.html"""
    if e.key == (pygame.K_ESCAPE or pygame.K_q):
        raise SystemExit
    elif e.key == pygame.K_LEFT:
        S0.play()
    elif e.key == pygame.K_RIGHT:
        S1.play()
    elif e.key == pygame.K_UP:
        Sr.play()
    elif e.key == pygame.K_DOWN:
        Sn.play()
    else:
        print(e.key)


if __name__ == '__main__':
    main()
