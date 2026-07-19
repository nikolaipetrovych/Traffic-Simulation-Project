import pygame

pygame.init()

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

#set car variables
vx = 3 #set x velocity
vy = 4 #set y velocity
a = 0.1 #set accel/decel value
ax = ay = a
car_size = road_width/6 #set car radius
