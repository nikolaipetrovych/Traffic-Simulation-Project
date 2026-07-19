import sys

import config as cfg
import pygame


class Car:
    def __init__(self, x, y, vx, vy, ax, ay):  # define variables for the class (x, y, vx, vy)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

        self.vxmax = vx
        self.vymax = vy

    def draw(self):
        pygame.draw.circle(cfg.main_disp, cfg.car_color, (self.x, self.y), cfg.car_size)  # redraw car at a new position
        if self.x > cfg.xsize:  # if car is off the screen horizontally
            self.x = 0  # respawn car at the start
        if self.y > cfg.ysize:  # if car is off the screen vertically
            self.y = 0  # respawn car at the start

    def move(self):  # define moving
        self.x += self.vx
        self.y += self.vy

    def accel(self, value):  # acceleration function (0 = decel, 1 = accel)
        if value == 0:  # decel
            if (self.vx > 0 or self.vy > 0):
                self.vx -= self.ax
                self.vy -= self.ay
                if self.vx < 0:
                    self.vx = 0
                if self.vy < 0:
                    self.vy = 0
        elif value == 1:  # accel
            if (self.vx < self.vxmax or self.vy < self.vymax):
                self.vx += self.ax
                self.vy += self.ay
                if self.vx > self.vxmax:
                    self.vx = self.vxmax
                if self.vy > self.vymax:
                    self.vy = self.vymax
        else:
            print("**Only values 0 or 1 are accepted for accel.value**")
            pygame.quit()  # quits
            sys.exit()  # runs exit

    def canmove(self, dir):
        if dir == 'x':
            return not (cfg.stop_line_hor_1_x - 2*cfg.car_size < self.x < cfg.stop_line_hor_1_x)
        if dir == 'y':
            return not (cfg.stop_line_ver_1_y - 2*cfg.car_size < self.y < cfg.stop_line_ver_1_y)

        print("dir has to be a string of x or y.")
        sys.exit()

    def shouldbrake(self, dir):
        if dir == 'x':
            return (cfg.stop_line_hor_1_x - 2*cfg.car_size  < self.x + ((self.vx)**2 / (2*self.ax)) < cfg.stop_line_hor_1_x)
        if dir == 'y':
            return (cfg.stop_line_ver_1_y - 2*cfg.car_size  < self.y + ((self.vy)**2 / (2*self.ay)) < cfg.stop_line_ver_1_y)

        print("dir has to be a string of x or y.")
        sys.exit()


class Light:
    def __init__(self, state, greentime, yellowtime, allredtime):  # define traffic light parameters
        self.state = state
        self.greentime = greentime
        self.yellowtime = yellowtime
        self.allredtime = allredtime

        self.clock = 0

    def change(self):
        if self.state in range(1,6):
            self.state += 1
        else:
            self.state = 1

    def count(self):
        if self.state in (1,2,3):  # when color2 is red
            self.color2 = cfg.red
            if self.state == 1:
                self.color1 = cfg.green
                self.timer = self.greentime
            elif self.state == 2:
                self.color1 = cfg.yellow
                self.timer = self.yellowtime
            elif self.state == 3:
                self.color1 = cfg.red
                self.timer = self.allredtime

        elif self.state in (4,5,6):  # when color1 is red
            self.color1 = cfg.red
            if self.state == 4:
                self.color2 = cfg.green
                self.timer = self.greentime
            elif self.state == 5:
                self.color2 = cfg.yellow
                self.timer = self.yellowtime
            elif self.state == 6:
                self.color2 = cfg.red
                self.timer = self.allredtime

        else:
            print("***INVALID CURRENT STATE VALUE***")
            sys.exit()

        self.clock += 1  # add to clock after checking states

        if self.clock == self.timer:  # when the cycle passes
            self.clock = 0  # reset the timer
            self.change()  # change the light's state


# def coord(coordinate_x, coordinate_y):
#     return (int(coordinate_x / cfg.scale), int(coordinate_y / cfg.scale))
