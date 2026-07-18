import pygame
pygame.init()

## CLASSES

class Car: #car

    def __init__(self, x, y, vx, vy, ax, ay): #define variables for the class (x, y, vx, vy)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        
        self.vxmax = vx
        self.vymax = vy

    def draw(self):
        pygame.draw.circle(main_disp, car_color, (self.x, self.y), car_size) #redraw car at a new position
        if self.x > xsize: #if car is off the screen horizontally
            self.x = 0 #respawn car at the start
        if self.y > ysize: #if car is off the screen vertically
            self.y = 0 #respawn car at the start

    def move(self): #define moving
        self.x += self.vx
        self.y += self.vy

    def accel(self, value): #acceleration function (0 = decel, 1 = accel)
        if value == 0: #decel
            if (self.vx > 0 or self.vy > 0):
                self.vx -= self.ax
                self.vy -= self.ay
                if self.vx < 0: self.vx = 0
                if self.vy < 0: self.vy = 0
        elif value == 1: # accel
            if (self.vx < self.vxmax or self.vy < self.vymax):
                self.vx += self.ax
                self.vy += self.ay
                if self.vx > self.vxmax: self.vx = self.vxmax
                if self.vy > self.vymax: self.vy = self.vymax
        else:
            print("**Only values 0 or 1 are accepted for accel.value**")
            pygame.quit() #quits
            exit() #runs exit


class Light: #traffic light
    def __init__(self, state, greentime, yellowtime, allredtime): #define traffic light parameters
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
        if self.state in (1,2,3): # when color2 is red
            self.color2 = red
            if self.state == 1:
                self.color1 = green
                self.timer = self.greentime
            elif self.state == 2:
                self.color1 = yellow
                self.timer = self.yellowtime
            elif self.state == 3:
                self.color1 = red
                self.timer = self.allredtime

        elif self.state in (4,5,6): # when color1 is red
            self.color1 = red
            if self.state == 4:
                self.color2 = green
                self.timer = self.greentime
            elif self.state == 5:
                self.color2 = yellow
                self.timer = self.yellowtime
            elif self.state == 6:
                self.color2 = red
                self.timer = self.allredtime

        else:
            print("***INVALID CURRENT STATE VALUE***")
            quit()

        self.clock += 1 # add to clock after checking states

        if self.clock == self.timer: #when the cycle passes
            self.clock = 0 #reset the timer
            self.change() #change the light's state


## FUNCTIONS

def coord(coordinate_x, coordinate_y):
    return (int(coordinate_x / scale), int(coordinate_y / scale))

## VARIABLES

#set window
xsize = 800
ysize = 600

# set unit/pixel scale

scale = 10 # pixels per meter

#define a game clock and framerate
gameclock = pygame.time.Clock()
framerate = 60

#create window
main_disp = pygame.display.set_mode((xsize, ysize)) #create display and set dimensions
pygame.display.set_caption("Traffic Simulation by Nikolai Petrovych") #set display name

#define helpful coordinates
center_x = xsize/2
center_y = ysize/2

#set road dims and pos
road_width = int(xsize / 10)
vert_x = int(center_x - road_width/2)
hor_y = int(center_y - road_width/2)

#set stop lines dims and pos
stop_line_length = road_width
stop_line_width = int(road_width/10)
stop_line_hor_1_x = center_x - road_width
stop_line_hor_1_y = hor_y
stop_line_hor_2_x = center_x + road_width - stop_line_width
stop_line_hor_2_y = hor_y
stop_line_ver_1_x = vert_x
stop_line_ver_1_y = center_y - road_width
stop_line_ver_2_x = vert_x
stop_line_ver_2_y =  center_y + road_width - stop_line_width

stop_line_hor_1 = (stop_line_hor_1_x, stop_line_hor_1_y, stop_line_width, stop_line_length)
stop_line_hor_2 = (stop_line_hor_2_x, stop_line_hor_2_y, stop_line_width, stop_line_length)
stop_line_ver_1 = (stop_line_ver_1_x, stop_line_ver_1_y, stop_line_length, stop_line_width)
stop_line_ver_2 = (stop_line_ver_2_x, stop_line_ver_2_y, stop_line_length, stop_line_width)

#set colors
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
grey_road = (120, 120, 120)
car_color = (50, 50, 150)
grass_color = (50, 190, 50)


#set traffic light dims and pos
light_size = road_width/12
light_offset = 200
light1_hor_x = int(center_x + light_offset)
light1_hor_y = int(center_y)
light1_vert_x = int(center_x)
light1_vert_y = int(center_y + light_offset)


#set initial traffic light values
light1 = Light(1, 240, 90, 60)

light1_hor_color = green
light1_vert_color = red

#spawn cars
vx = 3 #set x velocity
vy = 4 #set y velocity
a = 0.1 #set accel/decel value
ax = ay = a
car_size = road_width/6 #set car radius
car1 = Car(0, int(center_y), vx, 0, ax, 0) #set pos and velecity of car 1 (horizontal)
car2 = Car(int(center_x), 0, 0, vy, 0, ay) #set pos and velecity of car 2 (vertical)

## RUN PYGAME SIMULATION

while True: #keeps the game running
    gameclock.tick(framerate) #set the frame rate at 60 fps
    main_disp.fill(grass_color) #set bckrd color

    pygame.draw.rect(main_disp, grey_road, (0, hor_y, xsize, road_width))   #horizonal road
    pygame.draw.rect(main_disp, white, stop_line_hor_1)                     #stop line horizontal
    pygame.draw.rect(main_disp, white, stop_line_hor_2)                     #stop line horizontal 2
    pygame.draw.rect(main_disp, grey_road, (vert_x, 0, road_width, ysize))  #vertical road
    pygame.draw.rect(main_disp, white, stop_line_ver_1)                     #stop line vertical
    pygame.draw.rect(main_disp, white, stop_line_ver_2)                     #stop line vertical 2

    light1.count() # go through the count function (advance by 1 frame) for light1

    if light1.state == 1:
        car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state == 2:
        if light1.clock < light1.yellowtime*0.67 or not stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x:
            car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state in (3, 6):
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state == 4:
        car2.move()
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()

    if light1.state == 5:
        if light1.clock < light1.yellowtime*0.67 or not stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y:
            car2.move()
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()

    if (light1.state in range(2,7)) and (stop_line_hor_1_x - 2*car_size  < car1.x + ((car1.vx)**2 / (2*car1.ax)) < stop_line_hor_1_x):
        car1.accel(0)
        
    if (light1.state in range(1,4) or light1.state in range (5,7)) and (stop_line_ver_1_y - 2*car_size  < car2.y + ((car2.vy)**2 / (2*car2.ay)) < stop_line_ver_1_y):
        car2.accel(0)
        
    if car1.vx < car1.vxmax and light1.state == 1:
        car1.accel(1)
        
    if car2.vy < car2.vymax and light1.state == 4:
        car2.accel(1)

    pygame.draw.circle(main_disp, light1.color1, (light1_hor_x, light1_hor_y), light_size) #place light1_hor
    pygame.draw.circle(main_disp, light1.color2, (light1_vert_x, light1_vert_y), light_size) #place light1_vert

    car1.draw() # place car at its position
    car2.draw()

    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit when window is closed
            pygame.quit() #quits
            exit() #runs exit

    pygame.display.flip() #flip canvas, restart the loop
