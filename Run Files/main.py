import pygame
from classes import Car, Light, coord
import config as cfg

#spawn traffic light and set initial values
light1 = Light(1, 240, 90, 60)

#spawn cars and set initial values
car1 = Car(0, int(cfg.center_y), cfg.vx, 0, cfg.ax, 0) #set pos and velecity of car 1 (horizontal)
car2 = Car(int(cfg.center_x), 0, 0, cfg.vy, 0, cfg.ay) #set pos and velecity of car 2 (vertical)

## RUN PYGAME SIMULATION

while True: #keeps the game running
    cfg.gameclock.tick(cfg.framerate) #set the frame rate at 60 fps
    cfg.main_disp.fill(cfg.grass_color) #set bckrd color

    pygame.draw.rect(cfg.main_disp, cfg.grey_road, (0, cfg.hor_y, cfg.xsize, cfg.road_width))   #horizonal road
    pygame.draw.rect(cfg.main_disp, cfg.white, cfg.stop_line_hor_1)                     #stop line horizontal
    pygame.draw.rect(cfg.main_disp, cfg.white, cfg.stop_line_hor_2)                     #stop line horizontal 2
    pygame.draw.rect(cfg.main_disp, cfg.grey_road, (cfg.vert_x, 0, cfg.road_width, cfg.ysize))  #vertical road
    pygame.draw.rect(cfg.main_disp, cfg.white, cfg.stop_line_ver_1)                     #stop line vertical
    pygame.draw.rect(cfg.main_disp, cfg.white, cfg.stop_line_ver_2)                     #stop line vertical 2

    light1.count() # go through the count function (advance by 1 frame) for light1

    if light1.state == 1:
        car1.move()
        if not (cfg.stop_line_ver_1_y - 2*cfg.car_size < car2.y < cfg.stop_line_ver_1_y):
            car2.move()

    if light1.state == 2:
        if light1.clock < light1.yellowtime*0.67 or not cfg.stop_line_hor_1_x - 2*cfg.car_size < car1.x < cfg.stop_line_hor_1_x:
            car1.move()
        if not (cfg.stop_line_ver_1_y - 2*cfg.car_size < car2.y < cfg.stop_line_ver_1_y):
            car2.move()

    if light1.state in (3, 6):
        if not (cfg.stop_line_hor_1_x - 2*cfg.car_size < car1.x < cfg.stop_line_hor_1_x):
            car1.move()
        if not (cfg.stop_line_ver_1_y - 2*cfg.car_size < car2.y < cfg.stop_line_ver_1_y):
            car2.move()

    if light1.state == 4:
        car2.move()
        if not (cfg.stop_line_hor_1_x - 2*cfg.car_size < car1.x < cfg.stop_line_hor_1_x):
            car1.move()

    if light1.state == 5:
        if light1.clock < light1.yellowtime*0.67 or not cfg.stop_line_ver_1_y - 2*cfg.car_size < car2.y < cfg.stop_line_ver_1_y:
            car2.move()
        if not (cfg.stop_line_hor_1_x - 2*cfg.car_size < car1.x < cfg.stop_line_hor_1_x):
            car1.move()

    if (light1.state in range(2,7)) and (cfg.stop_line_hor_1_x - 2*cfg.car_size  < car1.x + ((car1.vx)**2 / (2*car1.ax)) < cfg.stop_line_hor_1_x):
        car1.accel(0)
        
    if (light1.state in range(1,4) or light1.state in range (5,7)) and (cfg.stop_line_ver_1_y - 2*cfg.car_size  < car2.y + ((car2.vy)**2 / (2*car2.ay)) < cfg.stop_line_ver_1_y):
        car2.accel(0)
        
    if car1.vx < car1.vxmax and light1.state == 1:
        car1.accel(1)
        
    if car2.vy < car2.vymax and light1.state == 4:
        car2.accel(1)

    pygame.draw.circle(cfg.main_disp, light1.color1, (cfg.light1_hor_x, cfg.light1_hor_y), cfg.light_size) #place light1_hor
    pygame.draw.circle(cfg.main_disp, light1.color2, (cfg.light1_vert_x, cfg.light1_vert_y), cfg.light_size) #place light1_vert

    car1.draw() # place car at its position
    car2.draw()

    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit when window is closed
            pygame.quit() #quits
            exit() #runs exit

    pygame.display.flip() #flip canvas, restart the loop
