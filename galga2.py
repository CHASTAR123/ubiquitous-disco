import random
import pgzrun

WIDTH, HEIGHT = 800, 600
TITLE = 'GALGA'

ship = Actor('spaceimg')
ship.pos = WIDTH - 100, HEIGHT / 2  

bullets = []
enemies = []

ship.dead = False
ship.countdown = 90

score = 0
lifeline = 3

def spawn_enemy():
    enemy = Actor('enemy')  
    enemy.pos = 0, random.randint(50, HEIGHT - 50)
    enemies.append(enemy)

def draw():
    screen.blit('sp.png', (0, 0)) 
    if lifeline > 0:

        if not ship.dead:
            ship.draw()
        for bullet in bullets:
            bullet.draw()

        for enemy in enemies:
            enemy.draw()

    screen.draw.text("Score: "+str(score), (10, 10), fontsize=40, color="white")

    if lifeline <= 0:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=80, color="red")

def update():
    global score
    global lifeline
    print(lifeline)
    if lifeline > 0:

        if keyboard.up and ship.y > 50 and not ship.dead:
            ship.y -= 3
        elif keyboard.down and ship.y < HEIGHT - 50 and not ship.dead:
            ship.y += 3

        # Shoot bullets 
        if keyboard.space and not ship.dead:        
            bullet = Actor('bult')
            bullet.pos = ship.x - 32, ship.y
            bullets.append(bullet)

        # Move bullets
        for bullet in bullets:
            bullet.x -= 5
            if bullet.x < 0:
                bullets.remove(bullet)
        for enemy in enemies:
            enemy.x += 2
            if enemy.x > WIDTH:
                enemies.remove(enemy)
            for bullet in bullets:
                if enemy.colliderect(bullet):
                    if enemy in enemies:
                        enemies.remove(enemy)
                    if bullet in bullets:
                        bullets.remove(bullet)
                    score += 10
            if not ship.dead and ship.colliderect(enemy):
                ship.dead = True
                lifeline -= 1
                if enemy in enemies:
                    enemies.remove(enemy)

        if ship.dead:
            ship.countdown -= 1
            if ship.countdown <= 0:
                ship.dead = False
                ship.countdown = 190

clock.schedule_interval(spawn_enemy, 0.6)

pgzrun.go()
