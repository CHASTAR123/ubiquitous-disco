import random
import pgzrun, pyautogui

WIDTH, HEIGHT = pyautogui.size()
TITLE = "GALGA"

ship= Actor('spacew.png')
ship.pos =WIDTH - 200, HEIGHT // 2
ship.dead= False
ship.respawn_timer =0
ship.shoot_cooldown =0

bullets =[]
enemies =[]

score = 0
lifeline = 3
bgy = 0

game_state = "menu"


def spawn_enemy():
    if game_state =="playing":
        enemy =Actor('battleship')
        enemy.pos = 0,random.randint(50, HEIGHT - 50)
        enemies.append(enemy)
def start_game():
    global game_state, score, lifeline
    game_state = "playing"
    score = 0
    lifeline = 3

    bullets.clear()
    enemies.clear()

    ship.dead = False
    ship.respawn_timer = 0
    ship.shoot_cooldown = 0
    ship.pos = WIDTH - 200, HEIGHT // 2

    clock.unschedule(spawn_enemy)
    clock.schedule_interval(spawn_enemy, 0.6)
def on_key_down(key):
    if key ==keys.RETURN:
        if game_state =="menu":
            start_game()
        elif game_state =="gameover":
            start_game()
def draw():
    screen.blit('spimg', (bgy, 0))
    if game_state == "menu":
        screen.draw.text("Space shooter",center=(WIDTH // 2, HEIGHT // 2 - 180),fontsize=100, color="white")
        screen.draw.text("Press ENTER to Start \n Use ↑ ↓ To control the ship \n Press SPACE to shoot \n Kill the alian ship \n bullet -→ Kill enemy \n Alian ship can cost a lifeline",center=(WIDTH // 2, HEIGHT // 2),fontsize=50,color="yellow")

    elif game_state == "playing":
        if ship.dead == False:
            ship.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text("Score: " + str(score), (10, 10), fontsize=40, color="white")
        screen.draw.text("Lives: " + str(lifeline), (10, 60), fontsize=40, color="white")

    elif game_state == "gameover":
        screen.draw.text(
            "GAME OVER",center=(WIDTH // 2, HEIGHT // 2 - 40),fontsize=90,color="red")
        screen.draw.text("Press ENTER to Restart",center=(WIDTH // 2, HEIGHT // 2 + 40),fontsize=40,color="white")

def update():
    global score, lifeline, bgy, game_state
    if game_state != "playing":
        return
    bgy -= 2
    if bgy <= -500:
        bgy = 0
    if lifeline <= 0:
        game_state = "gameover"
        clock.unschedule(spawn_enemy)
        return
    if ship.dead == False:
        if keyboard.up and ship.y > 50:
            ship.y -= 5
        if keyboard.down and ship.y < HEIGHT - 50:
            ship.y += 5
    if ship.shoot_cooldown > 0:
        ship.shoot_cooldown -= 1

    if keyboard.space:
        if ship.dead == False:
            if ship.shoot_cooldown == 0:
                bullet = Actor('bullet')
                bullet.pos = ship.x - 32, ship.y
                bullets.append(bullet)
                ship.shoot_cooldown = 15

    for bullet in bullets[:]:
        bullet.x -= 8
        if bullet.x < 0:
            bullets.remove(bullet)

    for enemy in enemies[:]:
        enemy.x += 3

        if enemy.x > WIDTH:
            enemies.remove(enemy)

        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10                
        if ship.dead == False and ship.colliderect(enemy):
            enemies.remove(enemy)
            ship.dead = True
            ship.respawn_timer = 120
            lifeline -= 1
    if ship.dead == True:
        ship.respawn_timer -= 1
        if ship.respawn_timer <= 0:
            ship.dead = False
            ship.pos = WIDTH - 200, HEIGHT // 2


pgzrun.go()
