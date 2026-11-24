# a minecraft but 2D game.
#today target--a working gun(player holding the gun and shooting
#next day target--animal and day night cycle(if possible crate function)
import turtle
import time
import random

#game constants
stones = []
delay = 0.1
player_place = False
start_time = time.time()
game_pause = False
zombies = []
animals = []
trees = []
animal_zombie_steps = 5
last_time = -1
paused_time = 0
pause_start = None
player_shooting = False
bullets = []
last_direction = 'up'
select_zombie_animal_horizontal = ['left', 'right']
select_zombie_animal_vertical = ['left', 'right']
zombie_hp = 1
day_night_time_cycle = 30000
start_day_night_time_cycle = 0
animal_movement_random = ['left', 'right', 'up', 'down']
food_number = 0
block_number = 0
player_hp = 3
bg_colors = ['#90EE90', 'green']
bg_index = 0
day_count_timer = 0
crates = []
bullet_number = 0
food_eating = False
break_tree = False
#so zombies can spawn without problem
day = 1
last_shot_time = 0
COOLDOWN = 0.25  # 250 milliseconds in seconds

#all screen items settings
#screen settings
wn = turtle.Screen()
wn.setup(700, 700)
wn.title('easy minecraft 2D')
wn.bgcolor('#90EE90')
wn.tracer(0)
canvas = wn.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)  # (width_resizable, height_resizable)

# UI for the coding canvas
pen = turtle.Turtle()
pen.hideturtle()  # Hides the arrow cursor
pen.pensize(3)
pen.color('black', 'white')

# Start at the bottom-left corner of the 700x700 screen
pen.penup()
pen.goto(-350, -350)
pen.pendown()

pen.begin_fill()
for _ in range(2):
    pen.forward(700)  # Full width from left (-350) to right (+350)
    pen.left(90)      # Turn 90 degrees upward
    pen.forward(100)  # Height of the bottom UI panel (adjust as needed)
    pen.left(90)      # Turn 90 degrees left
pen.end_fill()

#bullet count pen
bulletPen = turtle.Turtle()
bulletPen.shape('square')
bulletPen.color('#C0C0C0')
bulletPen.penup()
bulletPen.goto(-35, -330)
bulletPen.write(f'Bullet:{bullet_number}', align="right", font=("Courier", 20, "normal"))
bulletPen.hideturtle()

#food pen counting the food
foodPen = turtle.Turtle()
foodPen.shape('square')
foodPen.color('brown')
foodPen.penup()
foodPen.goto(-230, -330)
foodPen.write(f'food:{food_number}', align="right", font=("Courier", 20, "normal"))
foodPen.hideturtle()

#block count pen
blockPen = turtle.Turtle()
blockPen.shape('square')
blockPen.color('grey')
blockPen.penup()
blockPen.goto(150, -330)
blockPen.write(f'block:{block_number}', align="right", font=("Courier", 20, "normal"))
blockPen.hideturtle()

#day count timer pen
dayPen = turtle.Turtle()
dayPen.shape('square')
dayPen.color('white')
dayPen.penup()
dayPen.goto(330, 310)
dayPen.write(f'day:{day_count_timer}', align="right", font=("Courier", 20, "normal"))
dayPen.hideturtle()

#food block
food = turtle.Turtle()
food.shape('circle')
food.color('brown')
food.penup()
food.speed(0)
food.goto(-280, -280)
food.shapesize(2, 2, 1)

#player body
player = turtle.Turtle()
player.shape('square')
player.color('blue')
player.penup()
player.speed(0)
player.direction = 'stop'
player.goto(0, 0)

#time recording system
timeWritting = turtle.Turtle()
timeWritting.shape('square')
timeWritting.color('white')
timeWritting.penup()
timeWritting.goto(330, -250)
timeWritting.write(f'time:0', align="right", font=("Courier", 20, "normal"))
timeWritting.hideturtle()

#stone block logo
logo_stone = turtle.Turtle()
logo_stone.shape('square')
logo_stone.color('gray')
logo_stone.penup()
logo_stone.goto(100, -280)
logo_stone.shapesize(2, 2, 2)


#weapon logo
logo_weapon = turtle.Turtle()
logo_weapon.shape('square')
logo_weapon.color('black')
logo_weapon.penup()
logo_weapon.goto(-100, -280)
logo_weapon.shapesize(2, 0.5, 9)
logo_weapon.setheading(135)

#weapon
weapon = turtle.Turtle()
weapon.shape('square')
weapon.color('black')
weapon.penup()
weapon.speed(0)
weapon.direction = 'stop'
weapon.goto(0, 120)
weapon.shapesize(1.5, 0.5, 1)
weapon.hideturtle()

#empty hand
hand = turtle.Turtle()
hand.shape('square')
hand.color('black')
hand.penup()
hand.direction = 'stop'
hand.hideturtle()

#player live heart thing
heart = turtle.Turtle()
heart.shape('circle')
heart.color('#39FF14')
heart.penup()
heart.goto(270, -300)
heart.shapesize(2, 2, 2)

#game pole 1
game_pole_1 = turtle.Turtle()
game_pole_1.shape('square')
game_pole_1.color('black')
game_pole_1.penup()
game_pole_1.goto(-200, -303)
game_pole_1.shapesize(5, 0.5, 9)
game_pole_1.setheading(180)

#game pole 2
game_pole_2 = turtle.Turtle()
game_pole_2.shape('square')
game_pole_2.color('black')
game_pole_2.penup()
game_pole_2.goto(0, -303)
game_pole_2.shapesize(5, 0.5, 9)
game_pole_2.setheading(180)

#game pole 3
game_pole_3 = turtle.Turtle()
game_pole_3.shape('square')
game_pole_3.color('black')
game_pole_3.penup()
game_pole_3.goto(200, -303)
game_pole_3.shapesize(5, 0.5, 9)
game_pole_3.setheading(180)
        
#player based functions
#player taking damage from zombies
def player_damage():
    global player_hp, game_pause
    if not game_pause:
        for zombie in zombies:
            if player.distance(zombie) < 20:
                player_hp -= 1
            if player_hp <= 2:
                heart.color('#FFD700')
            if player_hp <= 1:
                heart.color('red')
            if player_hp <= 0:
                player.goto(1000, 1000)
                player.clear()
                
                deathPen = turtle.Turtle()
                deathPen.color('white')
                deathPen.shape('square')
                deathPen.write(f'You died. You lose', align="center", font=("Courier", 20, "normal"))
                deathPen.hideturtle()

                wn.bgcolor('black')
                wn.update()
                game_pause = True

    wn.ontimer(player_damage, 1000)

#player hand used for breaking trees
def move_hand_with_player():
    x = player.xcor()
    y = player.ycor()
    if hand.direction == 'up':
        hand.goto(x, y + 20)
        
    if hand.direction == 'down':
        hand.goto(x, y - 20)
        
    if hand.direction == 'left':
        hand.goto(x - 20, y)

    if hand.direction == 'right':
        hand.goto(x + 20, y)
#movement of the player
#moving the player code
def move():
    if player.direction == 'left':
        x = player.xcor()
        if x - 20 >= -320:
            player.setx(x - 20)
        player.direction = 'stop'

    if player.direction == 'right':
        x = player.xcor()
        if x + 20 <= 320:
            player.setx(x + 20)
        player.direction = 'stop'

    if player.direction == 'down':
        y = player.ycor()
        if y - 20 >= -220:
            player.sety(y - 20)
        player.direction = 'stop'

    if player.direction == 'up':
        y = player.ycor()
        if y + 20 <= 320:
            player.sety(y + 20)
        player.direction = 'stop'


#keyboard control functions
def move_up():
    if game_pause:
        return
    global last_direction
    player.direction = 'up'
    weapon.direction = 'up'
    hand.direction = 'up'    
    last_direction = 'up'
    if player.distance(weapon) <= 20:
        weapon.shapesize(1.5, 0.5, 1)
    
def move_down():
    if game_pause:
        return
    global last_direction
    player.direction = 'down'
    weapon.direction = 'down'
    hand.direction = 'down'
    last_direction = 'down'
    if player.distance(weapon) <= 20:
        weapon.shapesize(1.5, 0.5, 1)
    
    
def move_left():
    if game_pause:
        return
    global last_direction
    player.direction = 'left'
    weapon.direction = 'left'
    last_direction = 'left'
    hand.direction = 'left'
    if player.distance(weapon) <= 20:
        weapon.shapesize(0.5, 1.5, 1)

def move_right():
    if game_pause:
        return
    global last_direction
    player.direction = 'right'
    weapon.direction = 'right'
    hand.direction = 'right'
    last_direction = 'right'
    if player.distance(weapon) <= 20:
        weapon.shapesize(0.5, 1.5, 1)
    
#placing block functions
#placing the block commands
def player_command_place():
    if game_pause:
        return
    global player_place
    if block_number > 0:
        player_place = True
    

def place_block():
    global player_place, last_direction, block_number
    if player_place:
        player_place = False

        if block_number > 0:
            block_number -= 1
            blockPen.clear()
            blockPen.write(f'block:{block_number}', align="right", font=("Courier", 20, "normal"))
            #stone block place
            stone = turtle.Turtle()
            stone.shape('square')
            stone.color('gray')
            stone.penup()

            stone.hp = 2
            
            y = player.ycor()
            x = player.xcor()
            ix = stone.xcor()
            iy = stone.ycor()
            player.direction = last_direction
            if last_direction == 'up':
                stone.setheading(90)
                stone.goto(x, y + 20)
                player.direction = 'stop'
                
            if last_direction == 'down':
                stone.setheading(270)
                stone.goto(x, y - 20)
                player.direction = 'stop'

            if last_direction == 'left':
                stone.setheading(180)
                stone.goto(x - 20, y)
                player.direction = 'stop'

            if last_direction == 'right':
                stone.setheading(0)
                stone.goto(x + 20, y)
                player.direction = 'stop'
                
            stones.append(stone)
            player_place = False

def block_damage():
    for zombie in zombies:
        # Reduce cooldown every frame
        if zombie.cooldown > 0:
            zombie.cooldown -= 1

        for stone in stones[:]:  # Loop over a copy to safely remove items
            if zombie.distance(stone) < 25:
                if zombie.cooldown == 0:
                    stone.hp -= 1
                    zombie.backward(5)
                    zombie.cooldown = 30  # Wait 30 frames (~0.5–1 sec) before hitting again

                if stone.hp <= 0:
                    stone.goto(1000, 1000)
                    stones.remove(stone)

                
#game time system management functions
def day_count():
    global day_count_timer
    if not game_pause:
        day_count_timer += 1

        dayPen.clear()
        dayPen.write(f'day:{day_count_timer}', align="right", font=("Courier", 20, "normal"))
    wn.ontimer(day_count, 60000)
#day night system
def change_bgcolor():
    if not game_pause:
        global bg_index
        wn.bgcolor(bg_colors[bg_index])
        
        # Move to the next color, and wrap back to 0 at the end of the list
        bg_index = (bg_index + 1) % len(bg_colors)
    
    # Run this function again in 30 seconds (30,000 milliseconds)
    wn.ontimer(change_bgcolor, 30000)
    
#game timer
def game_timer():
    global start_time, last_time, paused_time
    timer = int(time.time() - start_time - paused_time)
    if timer != last_time:
        last_time = timer
        timeWritting.clear()
        timeWritting.write(f'time:{timer}', align="right", font=("Courier", 20, "normal"))


#game pause
def pause():
    global game_pause, paused_time, pause_start
    game_pause = not game_pause
    if game_pause:
        pause_start = time.time()
        wn.title('easy minecraft 2D - PAUSED')
    else:
        if pause_start is not None:
            paused_time += time.time() - pause_start
            pause_start = None
        wn.title('easy minecraft 2D')

#zombie based functions
# add zombie every 30 seconds
def add_zombie():
    global day
    if not game_pause:
        zombies_to_spawn = (day + 1) // 2

        for _ in range(zombies_to_spawn):
            zombie = turtle.Turtle()
            zombie.avoid_timer = 0
            zombie.shape("square")
            zombie.color("#50C878")
            zombie.penup()
            zombie.speed(0)

            zombie.hp = 1
            zombie.alive = True
            zombie.direction = "stop"
            zombie.cooldown = 0
            
            x = random.randint(-240, 300)
            y = random.randint(-240, 300)
            zombie.goto(x, y)

            zombies.append(zombie)

        day += 1

    wn.ontimer(add_zombie, 30000)

#zombie damage upon shot
def damage_zombie(zombie):
    if not zombie.alive:
        return
    # Check the EXISTING bullet, do NOT create a new one here
    for bullet in bullets:
        if bullet.isvisible() and bullet.distance(zombie) <= 20:
            zombie.color('#8B0000')
            zombie.hp -= 0.5
            bullet.hideturtle()  # Optional: hide bullet on hit so it doesn't hit 10 times
            
#zombie died so removed
def remove_zombie(zombie):
    if zombie.hp <= 0:
        zombie.goto(1000, 1000)
        zombie.clear()
        zombie.hideturtle()
        zombie.direction = 'stop'
        zombie.alive = False
        if zombie in zombies:
            zombies.remove(zombie)
#zombie additions in game
def zombie_blocked(zombie):
    if not zombie.alive:
        return
    for stone in stones:
        if zombie.distance(stone) < 25:
            # Pick a perpendicular direction to walk around the stone
            if zombie.direction in ['left', 'right']:
                zombie.direction = random.choice(['up', 'down'])
            else:
                zombie.direction = random.choice(['left', 'right'])
            
            # Force the zombie to follow this detour for 10 frames
            zombie.avoid_timer = 10
            break
#zombie movement
def zombie_movement(zombie):
    global animal_zombie_steps
    if not zombie.alive:
        return
    ix = zombie.xcor()
    iy = zombie.ycor()

    # 1. If avoiding a stone, move in the detour direction first
    if zombie.avoid_timer > 0:
        zombie.avoid_timer -= 1
        next_x, next_y = ix, iy

        if zombie.direction == 'left':
            next_x -= animal_zombie_steps
        elif zombie.direction == 'right':
            next_x += animal_zombie_steps
        elif zombie.direction == 'up':
            next_y += animal_zombie_steps
        elif zombie.direction == 'down':
            next_y -= animal_zombie_steps

        # Only take the step if it doesn't walk into another stone
        if not any(stone.distance(next_x, next_y) < 22 for stone in stones):
            zombie.goto(next_x, next_y)
        else:
            # Hit a corner or second stone; pick a new direction next frame
             zombie.avoid_timer = 0
        return

    # 2. Otherwise, chase the player normally
    x = player.xcor()
    y = player.ycor()
    if zombie.distance(player) > 20:
        if x < ix:
            if x - 20 >= -340:
                zombie.setx(ix - animal_zombie_steps)
                zombie.direction = 'left'
        elif x > ix:
            if x + 20 <= 340:
                zombie.setx(ix + animal_zombie_steps)
                zombie.direction = 'right'

        if y < iy:
            if y - 20 >= -240:
                zombie.sety(iy - animal_zombie_steps)
                zombie.direction = 'down'
        elif y > iy:
            if y + 20 <= 340:
                zombie.sety(iy + animal_zombie_steps)
                zombie.direction = 'up'
   
#animal based functions
#add animal in game
def add_animal():
    if game_pause:
        return
    if not game_pause:
        #animal
        animal = turtle.Turtle()
        animal.shape('square')
        animal.color('brown')
        animal.penup()
        animal.speed(0)
        animal.direction = 'stop'
        animal.goto(0, 140)

        animal.hp = 1.5
        animal.alive = True
        animal.direction = 'stop'
        
        x = random.randint(-240, 300)
        y = random.randint(-240, 300)
        animal.goto(x, y)

        animals.append(animal)

    wn.ontimer(add_animal, 60000)
    
# Animal damage system
def damage_animal(animal):
    if not animal.alive:
        return
    for bullet in bullets:
        if bullet.isvisible() and bullet.distance(animal) <= 20:
            animal.color('#8B0000')
            animal.hp -= 0.5
            bullet.hideturtle()

# Animal died so removed
def remove_animal(animal):
    global food_number
    if animal.hp <= 0 and animal.alive:
        animal.goto(1000, 1000)
        animal.hideturtle()
        animal.clear()
        animal.direction = 'stop'
        animal.alive = False
        if animal in animals:
            animals.remove(animal)

        food_number += 1
        foodPen.clear()
        foodPen.write(f'food:{food_number}', align="right", font=("Courier", 20, "normal"))

# Random movement for ALL animals every 500ms
def random_movement():
    if not game_pause:
        global animal_zombie_steps
        for animal in animals:
            if animal.alive:
                x = animal.xcor()
                y = animal.ycor()
                animal.direction = random.choice(animal_movement_random)
                
                if animal.direction == 'left':
                    if x - 20 >= -340:
                        animal.setx(x - animal_zombie_steps)
                elif animal.direction == 'right':
                    if x + 20 <= 340:
                        animal.setx(x + animal_zombie_steps)
                
                elif animal.direction == 'up':
                    if y + 20 <= 340:
                        animal.sety(y + animal_zombie_steps)
                elif animal.direction == 'down':
                    if y - 20 >= -240:
                     animal.sety(y - animal_zombie_steps)

    wn.ontimer(random_movement, 250)

    
#weapon(object name) based functions
#moving the weapon with the player
def move_weapon_with_player():
    x = player.xcor()
    y = player.ycor()
    if weapon.direction == 'up':
        weapon.goto(x, y + 20)
        
    if weapon.direction == 'down':
        weapon.goto(x, y - 20)
        
    if weapon.direction == 'left':
        weapon.goto(x - 20, y)

    if weapon.direction == 'right':
        weapon.goto(x + 20, y)

# shooting from the weapon
def shooting():
    global player_shooting, bullets, last_direction, bullet_number
    
    # Removed the time check from here so it doesn't conflict with shoot()
    if player_shooting and bullet_number >= 1:
        # bullet
        bullet = turtle.Turtle()
        bullet.shape('triangle')
        bullet.color('#dcdcdc')
        bullet.penup()
        bullet.speed(0)
        bullet.hideturtle()
        
        ix = weapon.xcor()
        iy = weapon.ycor()
        bullet.direction = last_direction
        
        if bullet.direction == 'up':
            bullet.setheading(90)
            bullet.goto(ix, iy + 20)
        elif bullet.direction == 'down':
            bullet.setheading(270)
            bullet.goto(ix, iy - 20)
        elif bullet.direction == 'left':
            bullet.setheading(180)
            bullet.goto(ix - 20, iy)
        elif bullet.direction == 'right':
            bullet.setheading(0)
            bullet.goto(ix + 20, iy)
        
        bullet.showturtle()
        bullets.append(bullet)
        bullet_number -= 1
        bulletPen.clear()
        bulletPen.write(f'Bullet:{bullet_number}', align="right", font=("Courier", 20, "normal"))

        player_shooting = False

# moving the bullet
def move_bullet():
    global bullets
    for bullet in bullets:
        if bullet.direction == 'up':
            bullet.sety(bullet.ycor() + 15)
        elif bullet.direction == 'down':
            bullet.sety(bullet.ycor() - 15)
        elif bullet.direction == 'left':
            bullet.setx(bullet.xcor() - 15)
        elif bullet.direction == 'right':
            bullet.setx(bullet.xcor() + 15)

# keyboard commands for shooting
def shoot():
    if game_pause:
        return
    global player_shooting, last_shot_time
    
    current_time = time.time()
    
    # Only allow shooting if weapon is visible AND 250ms have passed
    if weapon.isvisible() and (current_time - last_shot_time >= COOLDOWN):
        player_shooting = True
        last_shot_time = current_time

# unleash the gun or unhold the gun (toggles visibility ONLY)
def hold_unhold_weapon():
    if game_pause:
        return
    if weapon.isvisible():
        weapon.hideturtle()      # Hide it
    else:
        weapon.showturtle()      # Show it
#crate system
#take loot from the crate
def crate_loot():
    global bullet_number  # Allows this function to update your total bullet count
    
    # Loop through a copy of the list so we can safely remove collected crates
    for crate in crates[:]:
        if player.distance(crate) < 20:  # 20 is usually a better hitbox size for turtles
            # 1. Generate a random drop for THIS crate and add it to the total
            drop = random.randint(3, 10)
            bullet_number += drop
            
            # 2. Update the on-screen bullet counter
            bulletPen.clear()
            bulletPen.write(f"Bullets: {bullet_number}", align="right", font=("Courier", 20, "normal"))
            
            # 3. Hide the crate and remove it from the active list
            crate.hideturtle()
            crate.goto(1000, 1000)
            crates.remove(crate)


def add_crate():
    if not game_pause:
        crate = turtle.Turtle()
        crate.shape("square")
        crate.color("#ff4500", "orange")
        crate.penup()
        
        # Spawn randomly across the screen (assuming a 600x600 window)
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        crate.goto(x, y)
        
        # Add this new crate to the list
        crates.append(crate)
        
    # Schedule the next crate to spawn in 60 seconds (60000 ms)
    wn.ontimer(add_crate, 30000)

# food eating and hp restores
def food_eat():
    global food_number, player_hp, food_eating
    
    if food_eating == True:
        # 1. Only eat if the player has food AND needs healing
        if food_number > 0 and player_hp < 3:
            food_number -= 1
            player_hp += 1
            
            # Update the on-screen food text
            foodPen.clear()
            foodPen.write(f'food:{food_number}', align="right", font=("Courier", 20, "normal"))
        
        # 2. Always reset food_eating to False so it doesn't get stuck
        food_eating = False

    # 3. Update heart color based on current HP (check from highest to lowest)
    if player_hp >= 3:
        heart.color('#39FF14')  # Change this to whatever your full-health color is
    elif player_hp == 2:
        heart.color('#FFD700')
    elif player_hp == 1:
        heart.color('red')
    elif player_hp <= 0:
        player.goto(1000, 1000)
        player.hideturtle()

#tree based functions
#add trees in game
def tree_grow():
    if not game_pause:
        #tree
        tree = turtle.Turtle()
        tree.shape('square')
        tree.color('white')
        tree.penup()
        tree.goto(0, 180)

        tree.hp = random.randint(3, 10)

        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        tree.goto(x, y)
        
        trees.append(tree)

    wn.ontimer(tree_grow, 60000)

#break tree
def key_break_tree():
    global block_number, break_tree
    for tree in trees[:]:
        if break_tree == True and not weapon.isvisible():
            if hand.distance(tree) <= 20:
                tree.hp -= 1
                break_tree = False

            if tree.hp <= 0:
                block_number += random.randint(2, 5)

                blockPen.clear()
                blockPen.write(f'block:{block_number}', align="right", font=("Courier", 20, "normal"))

                break_tree = False
                tree.hideturtle()
                trees.remove(tree)
            
#command for breaking tree
def command_key_break_tree():
    if game_pause:
        return
    global break_tree
    if not break_tree:
        break_tree = True

#player key command
def command_eating():
    if game_pause:
        return
    global food_eating
    if food_eating == False:
        food_eating = True

# keyboard bindings
wn.onkeypress(move_up, 'Up')
wn.onkeypress(move_down, 'Down')
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(player_command_place, 'Q')
wn.onkeypress(player_command_place, 'q')
wn.onkeypress(pause, 'P')
wn.onkeypress(pause, 'p')
wn.onkeypress(shoot, 's')
wn.onkeypress(shoot, 'S')
wn.onkeypress(command_eating, 'e')
wn.onkeypress(command_eating, 'E')
wn.onkeyrelease(hold_unhold_weapon, 'u')
wn.onkeyrelease(hold_unhold_weapon, 'U')
wn.onkeypress(command_key_break_tree, 'b')
wn.onkeypress(command_key_break_tree, 'B')


wn.listen()

# main game loop using ontimer
def game_loop():
    global player_shooting
    if not game_pause:
        game_timer()
        move()
        shooting()
        move_bullet()
        for zombie in zombies[:]:
            zombie_blocked(zombie)
            zombie_movement(zombie)
            damage_zombie(zombie)
            remove_zombie(zombie)
        
        for animal in animals[:]:
            damage_animal(animal)
            remove_animal(animal)

        # REMOVED hold_unhold_weapon() from here!
        move_hand_with_player()
        move_weapon_with_player()
        place_block()
        block_damage()
        crate_loot()
        food_eat()
        key_break_tree()
    
    wn.update()
    wn.ontimer(game_loop, int(delay * 1000))

tree_grow()
add_crate()
day_count()
change_bgcolor()
player_damage()
add_zombie()
add_animal()
random_movement()
game_loop()
wn.mainloop()

