import pygame
pygame.init()

#define classes
class Car: #car

    def __init__(self, x, y, vx, vy): #define variables for the class (x, y, vx, vy)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self): #define moving
        self.x += self.vx
        self.y += self.vy

class Light: #traffic light
    def __init__(self, state, timer, green, yellow, allred): #define traffic light state
        self.state = state
        self.timer = timer
        self.green = green
        self.yellow = yellow
        self.allred = allred

    def change(self):
        if self.state == 6:
            self.state = 1
        else:
            self.state += 1



#set window
xsize = 800
ysize = 600

#define a clock (to set the frame rate later)
clock = pygame.time.Clock()

#create window
main_disp = pygame.display.set_mode((xsize, ysize)) #create display and set dimensions
pygame.display.set_caption("the game") #set display name

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
light_size = 10
light_offset = 200
light1_hor_x = int(center_x + light_offset)
light1_hor_y = int(center_y)
light1_vert_x = int(center_x)
light1_vert_y = int(center_y + light_offset)


#set initial traffic light values
light1 = Light(1, 0, 120, 90, 60)
# light1_timing = 180 #set the time for light change
# green_time = 240
# yellow_time = 90
# allred_time = 60

light1_hor_color = green
light1_vert_color = red

#spawn cars
vx = 6 #set x velocity
vy = 2 #set y velocity
car_size = road_width/6 #set car radius
car1 = Car(0, int(center_y), vx, 0) #set pos and velecity of car 1 (horizontal)
car2 = Car(int(center_x), 0, 0, vy) #set pos and velecity of car 2 (vertical)

#run game

while True: #keeps the game running
    clock.tick(60) #set the frame rate at 60 fps
    main_disp.fill(grass_color) #set bckrd color

    pygame.draw.rect(main_disp, grey_road, (0, hor_y, xsize, road_width)) #horizonal road
    pygame.draw.rect(main_disp, white, stop_line_hor_1) #stop line horizontal
    pygame.draw.rect(main_disp, white, stop_line_hor_2) #stop line horizontal 2
    pygame.draw.rect(main_disp, grey_road, (vert_x, 0, road_width, ysize)) #vertical road
    pygame.draw.rect(main_disp, white, stop_line_ver_1) #stop line vertical
    pygame.draw.rect(main_disp, white, stop_line_ver_2) #stop line vertical 2
    
    light1_timing = 0

    if light1.state == 1:
        light1_timing = light1.green
        light1_hor_color = green
        light1_vert_color = red
        car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state == 2:
        light1_timing = light1.yellow
        light1_hor_color = yellow
        light1_vert_color = red
        if light1.timer < light1.yellow*0.67 or not stop_line_hor_1_x - 2*car_size< car1.x < stop_line_hor_1_x:
            car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state in (3, 6):
        light1_timing = light1.allred
        light1_hor_color = red
        light1_vert_color = red
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()
        if not (stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y):
            car2.move()

    if light1.state == 4:
        light1_timing = light1.green
        light1_hor_color = red
        light1_vert_color = green
        car2.move()
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()

    if light1.state == 5:
        light1_timing = light1.yellow
        light1_hor_color = red
        light1_vert_color = yellow
        if light1.timer < light1.yellow*0.67 or not stop_line_ver_1_y - 2*car_size < car2.y < stop_line_ver_1_y:
            car2.move()
        if not (stop_line_hor_1_x - 2*car_size < car1.x < stop_line_hor_1_x):
            car1.move()

    if light1.timer == light1_timing: #when the cycle passes
        light1.timer = 0 #reset the timer
        light1.change() #change the light's state

        # print("Light state has changed to:") #display light phase
        # print(light1_state)

    # if light1_state in (2, 5): #if a light is yellow
    #         print(light1_timer < yellow_time*0.67) #check if cars can still pass

    pygame.draw.circle(main_disp, light1_hor_color, (light1_hor_x, light1_hor_y), light_size) #place light1_hor
    pygame.draw.circle(main_disp, light1_vert_color, (light1_vert_x, light1_vert_y), light_size) #place light1_vert

    pygame.draw.circle(main_disp, car_color, (car1.x, car1.y), car_size) #redraw car 1 at a new position
    pygame.draw.circle(main_disp, car_color, (car2.x, car2.y), car_size) #redraw car 2 at a new position

    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit when window is closed
            pygame.quit() #quits
            exit() #runs exit

    light1.timer += 1 #add 1 to the timer

    if car1.x > xsize: #if car1 is off the screen
        car1.x = 0 #respawn car1 at the start
    if car2.y > ysize: #if car2 is off the screen
        car2.y = 0 #respawn car2 at the start

    pygame.display.flip() #flip canvas, restart the loop