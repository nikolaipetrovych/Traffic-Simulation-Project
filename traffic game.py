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

#set window
xsize = 800
ysize = 600

#define a clock (to set the frame rate later)
clock = pygame.time.Clock()

#create window
main_disp = pygame.display.set_mode((xsize, ysize)) #create display and set dimensions
pygame.display.set_caption("the game") #set display name

#set road dims and pos
road_width = int(xsize / 10)
vert_x = int(xsize/2 - road_width/2)
hor_y = int(ysize/2 - road_width/2)

#set traffic light colors
green = (0, 255, 0)
red = (255, 0, 0)

#set traffic light dims and pos
light1_size = 10
light1_offset = 200
light1_hor_x = int(xsize/2 + light1_offset)
light1_hor_y = int(ysize/2)
light1_vert_x = int(xsize/2)
light1_vert_y = int(ysize/2 + light1_offset)


#set initial traffic light values
light1_state = False #True for red, False for green
light1_timer = 0 #start at 0
light1_timing = 180 #set the time for light change

#spawn cars
vx = 3 #set x velocity
vy = 2 #set y velocity
car_width = road_width/4 #set car width
car_length = road_width/2 #set car length
car1 = Car(0, int(hor_y + road_width/2 - car_width/2), vx, 0) #set pos and velecity of car 1 (horizontal)
car2 = Car(int(vert_x + road_width/2 - car_width/2), 0, 0, vy) #set pos and velecity of car 2 (vertical)

#run game
while True: #keeps the game running
    clock.tick(60) #set the frame rate at 60 fps
    main_disp.fill((50, 190, 50)) #set bckrd color 
    pygame.draw.rect(main_disp, (120, 120, 120), (0, hor_y, xsize, road_width)) #horizonal road
    pygame.draw.rect(main_disp, (255,255,255), (vert_x - car_length, hor_y, int(car_length/5), road_width)) #stop line horizontal
    pygame.draw.rect(main_disp, (255,255,255), (vert_x + road_width + car_length - int(car_length/5), hor_y, int(car_length/5), road_width)) #stop line horizontal 2
    pygame.draw.rect(main_disp, (120, 120, 120), (vert_x, 0, road_width, ysize)) #vertical road
    pygame.draw.rect(main_disp, (255,255,255), (vert_x, hor_y - car_length, road_width, int(car_length/5))) #stop line vertical
    pygame.draw.rect(main_disp, (255,255,255), (vert_x, hor_y + road_width + car_length - int(car_length/5), road_width, int(car_length/5))) #stop line vertical 2
    pygame.draw.circle(main_disp, red if light1_state else green, (light1_hor_x, light1_hor_y), light1_size) #place light1_hor
    pygame.draw.circle(main_disp, green if light1_state else red, (light1_vert_x, light1_vert_y), light1_size) #place light1_vert

    if light1_timer == light1_timing: #when x seconds passes (x seconds * 60 frames)
        light1_timer = 0 #reset the timer
        light1_state = not light1_state #change the light's state
        print("The light value has changed")

    pygame.draw.rect(main_disp, (50, 50, 150), (car1.x, car1.y, car_length, car_width)) #redraw car 1 at a new position
    pygame.draw.rect(main_disp, (50, 50, 150), (car2.x, car2.y, car_width, car_length)) #redraw car 2 at a new position

    for event in pygame.event.get(): #check for events
        if event.type == pygame.QUIT: #exit when window is closed
            pygame.quit() #quits
            exit() #runs exit

    light1_timer += 1 #add 1 to the timer

    if light1_state == True: #if horizontal light is red
        car2.move() #car2 keeps moving
        if not (vert_x - int(2.5*car_length) < car1.x < vert_x - car_length): #if car1 is not close to the stop line
            car1.move() #car1 keeps moving

    else: #if vertical light is red
        car1.move() #car1 keeps moving
        if not (hor_y - int(2.5*car_length) < car2.y < hor_y - car_length): #if car2 is not close to the stop line
            car2.move() #car2 keeps moving

    if car1.x > xsize: #if car1 is off the screen
        car1.x = 0 #respawn car1 at the start
    if car2.y > ysize: #if car2 is off the screen
        car2.y = 0 #respawn car2 at the start

    pygame.display.flip() #flip canvas