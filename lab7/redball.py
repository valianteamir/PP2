import pygame as pg

pg.init()
size = [520, 520]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

XC = 260
YC = 260
radius = 20  # Ball radius
speed = 20   # Movement step

fill_color = (255, 255, 255)
circle_color = (255, 0, 0)

running = True
while running:
    screen.fill(fill_color)
    pg.draw.circle(screen, circle_color, (XC, YC), radius)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP and YC > radius:
                YC -= speed
            if event.key == pg.K_DOWN and YC < size[1] - radius:
                YC += speed
            if event.key == pg.K_RIGHT and XC < size[0] - radius:
                XC += speed
            if event.key == pg.K_LEFT and XC > radius:
                XC -= speed

    pg.display.flip()
    clock.tick(30)

pg.quit()
