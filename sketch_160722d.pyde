
w_s = 650
x = w_s*0.125
ship_x = w_s*0.475
ship_y = w_s*0.825
bullet_exists = False
hero_movement = False
number_bullets = []
x_movement = True
enemy_y = w_s*0.2
y_movement = False

# score =
# high_score =
# lives =
# level =
# credit =
# game_over =
# start_screen =

def gui():
    global w_s
    global time
    stroke(0, 255, 0)
    strokeWeight(2)
    line(w_s*0.08333333333,w_s*0.875,w_s*0.91666666666,w_s*0.875)
    line(w_s*0.4,w_s*0.875,w_s*0.4,w_s*0.965)
    line(w_s*0.6,w_s*0.875,w_s*0.6,w_s*0.965)
    stroke(255,255,255)
    line(w_s*0.08333333333,w_s*0.125,w_s*0.91666666666,w_s*0.125)
    line(w_s*0.33333333333,w_s*0.125,w_s*0.33333333333,w_s*0.035)
    line(w_s*0.66666666666,w_s*0.125,w_s*0.66666666666,w_s*0.035)
    font = loadFont("Tahoma-Bold-48.vlw")
    textFont(font,w_s*0.02)
    fill(255,255,255)
    text("Score: ",w_s*0.1,45)
    text("High Score: ",w_s*0.1,65)
    text("Time: " + str(time),w_s*0.6875, w_s*0.10833333333)
    #textAlign(CENTER,BOTTOM)
    textFont(font,w_s*0.04)
    text("Invaders",w_s*0.41,w_s*0.10833333333)
    text("Space",w_s*0.44,w_s*0.05833333333)
    fill(0,255,0)
    textFont(font,w_s*0.03)
    text("Level: ",w_s*0.45833333333,w_s*0.92083333333)
    text("Lives: ",w_s*0.125,w_s*0.94166666667)
    text("Credit: ",w_s*0.65,w_s*0.94166666667)
    

def enemy_movement():
    global enemy_y
    global x
    global x_movement
    global y_movement
    print (x_movement)
    if time % 2 == 1 and time != 0 and y_movement == False:
        if x_movement == True and x < w_s*0.33227263076: #and enemy_y == 130 :
            x = x + 1.168155
            if x >= w_s*0.33227263076:
                y_movement = True
                x_movement = False
        if x_movement == False and x >= w_s*0.125: #and enemy_y != 130:
            x = x - 1.168155
            if x <= w_s*0.125:
                y_movement = True
                x_movement = True
    if y_movement == True and time % 4 == 0 and time != 0:
        enemy_y = enemy_y + 20
        y_movement = False           
            

def display_enemy_ships(enemy_ships):
    global time
    global enemy_y
    global x
    global hero_ship
    global enemy_ships_row
    
    noStroke()
    z = 0
    enemy_movement() 
    for lst in enemy_ships:
        for ships in enemy_ships_row:
            if z < len(enemy_ships_row):
                fill(255,255,255)
                enemy_x = x+w_s*0.08125*z
                ellipse(enemy_x,enemy_y,w_s*0.04166666666,w_s*0.04166666666)
                z = z + 1

def hero_ship():
    global ship_x
    global ship_y
    global hero_movement
    global time
    global bullet_exists
    global bullet_x
    global bullet_y
    global enemy_ships
    global enemy_ships_row
    global number_bullets
    global webImg1
    noStroke()
    fill(0, 255, 0)
    rect(ship_x,ship_y, w_s/20, w_s/65)
    rect(ship_x + 3, ship_y-3.5, w_s/30+5, w_s/90)
    rect(ship_x + 11.5, ship_y-9.5, w_s/60, w_s/90)
    rect(ship_x + 15.05, ship_y-12.5, w_s/210, w_s/90)
    if keyPressed == True:
        hero_movement = True
    if keyCode == LEFT and hero_movement == True and ship_x > w_s*0.08333333333:
        ship_x = ship_x - 2.5
        hero_movement = False
    if keyCode == RIGHT and hero_movement == True and ship_x < w_s*0.91666666666-w_s/20:
        ship_x = ship_x + 2.5
        hero_movement = False
    if mousePressed == True and not bullet_exists:
        bullet_exists = True
        bullet_x = ship_x + 15
        bullet_y = ship_y
    enemy_ships_row = ["1","2","3","4","5","6","7","8"]    
    if bullet_exists == True:
        fill(0,255,0)
        if mouseButton == LEFT:
            number_bullets.append(1)
            # for bullet in number_bullets:
            #     rect(bullet_x, bullet_y, 3, 15)
            #     bullet_y = bullet_y - 2
            #     if bullet_y <= w_s*0.125:
            #         bullet_exists = False
            #     if bullet_x < w_s*0.375 and bullet_x > 0.4625 and bullet_y <= w_s*0.125+50 :
            #         enemy_ships_row.remove("1")
                
                
    
def setup():
    noCursor()
    size(w_s,w_s)
    
def draw():
    background(0,0,0)
    global time
    global bullet_exists    
    time = (millis())/1000
    gui()
    hero_ship()
    enemy_ships = [1,2,3]
    display_enemy_ships(enemy_ships)
    