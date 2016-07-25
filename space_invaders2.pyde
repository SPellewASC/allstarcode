w_s = 650
x = w_s*0.125
# score =
# high_score =
# lives =
# level =
# credit =
# game_over =
# start_screen =
ship_x = w_s*0.475
ship_y = w_s*0.825
bullet_exists = False
hero_movement = False
def enemy_movement():
    global y
    global x
    if time % 8  == 0:
        y = y - 50 + 50
            
def display_enemy_ships(enemy_ships):
    global time
    global y
    global x
    global hero_ship
    global enemy_ships_row
    
    noStroke()
    y = w_s*0.2
    z = 0
    enemy_movement()
    for lst in enemy_ships:
        for ships in enemy_ships_row:
            if z < len(enemy_ships_row):
                fill(255,255,255)
                ellipse(x+w_s*0.08125*z,y,w_s*0.04166666666,w_s*0.04166666666)
                z = z + 1            
hero_movement = False    
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
    
    noStroke()
    fill(0, 255, 0)
    rect(ship_x,ship_y, w_s/20, w_s/30)
    if keyPressed == True:
        hero_movement = True
    if keyCode == LEFT and hero_movement == True:
        ship_x = ship_x - 2.5
        hero_movement = False
    if keyCode == RIGHT and hero_movement == True:
        ship_x = ship_x + 2.5
        hero_movement = False
    if mousePressed == True and not bullet_exists:
        bullet_exists = True
        bullet_x = ship_x + 15
        bullet_y = ship_y
    enemy_ships_row = [1,2,3,4,5,6,7]    
    if bullet_exists == True:
        fill(0,255,0)
        number_bullets = []
        if mouseButton == LEFT:
            number_bullets.append(1)
            for bullet in number_bullets:
                rect(bullet_x, bullet_y, 3, 15)
                bullet_y = bullet_y - 2
                if bullet_y <= w_s*0.125:
                    bullet_exists = False
                if bullet_x < w_s*0.375 and bullet_x > 0.4625 and bullet_y <= w_s*0.125+50 :
                    enemy_ships_row.remove(1)
                
    
def setup():
    noCursor()
    delay(200)
    size(w_s,w_s)
def draw():    
    background(0,0,0)
    global time
    global bullet_exists    
    time = (millis())/1000
    hero_ship()
    enemy_ships = [1,2,3]
    display_enemy_ships(enemy_ships)
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
    