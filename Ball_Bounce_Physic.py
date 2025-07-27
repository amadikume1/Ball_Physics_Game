import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
Circle_X = WIDTH / 2
Circle_Y = HEIGHT / 2
velocity_X = 0
velocity_Y = 0
bounce_factor = 0.6
gravity = .9
radius = 10
mass = radius

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

dragging = False
prev_mouse_pos = None
mouse_vel_x = 0
mouse_vel_y = 0

# Game loop
running = True
while running:

  
    dt = clock.tick(60) / 1000.0  # time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity_Y += -20

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (Circle_X - mouse_x) ** 2 + (Circle_Y - mouse_y) ** 2 <= radius ** 2:  # radius 10 squared
                dragging = True
                velocity_X = 0
                velocity_Y = 0
                prev_mouse_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:

            dragging = False
            velocity_X = mouse_vel_x * .03
            velocity_Y = mouse_vel_y * .03

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if bounce_factor >= .1 and radius < 70:
                    radius += 5
                    bounce_factor -= .03

            elif event.key == pygame.K_DOWN:

                if bounce_factor >= .1 and radius > 10:
                    radius -= 5
                    bounce_factor += .03

            elif event.key == pygame.K_LEFT:

                    velocity_X = -10

            elif event.key == pygame.K_RIGHT:
                    velocity_X = 10
                

        
        if event.type == pygame.MOUSEMOTION and dragging:
            Circle_X, Circle_Y = event.pos
            if prev_mouse_pos:
                dx = event.pos[0] - prev_mouse_pos[0]
                dy = event.pos[1] - prev_mouse_pos[1]
                mouse_vel_x = dx / dt
                mouse_vel_y = dy / dt

            prev_mouse_pos = event.pos

    # Fill screen with a color
    screen.fill((0, 100, 200))  # RGB blueish color

    # Gravity effect
    if not dragging:
        velocity_Y += gravity
        Circle_X += velocity_X 
        Circle_Y += velocity_Y

    # Bounce if ball hits the bottom or sides
    if Circle_Y >= HEIGHT - radius:
        Circle_Y = HEIGHT - radius
        velocity_Y = -velocity_Y * bounce_factor

    if Circle_Y <= radius:
        Circle_Y = radius
        velocity_Y = -velocity_Y * bounce_factor

    if Circle_X <= radius / 2:
        Circle_X = radius / 2
        velocity_X = -velocity_X * bounce_factor

    elif Circle_X >= WIDTH - radius / 2:
        Circle_X = WIDTH - radius / 2
        velocity_X = -velocity_X * bounce_factor

    if Circle_Y == HEIGHT - radius:

        if velocity_X < 0:
            velocity_X += .07

        else:
            velocity_X += -.07

        if -.7 <= velocity_X and velocity_X < .7:

            velocity_X = 0

    # Drawing
    screen.fill((0, 100, 200))
    pygame.draw.circle(screen, (0, 255, 0), (int(Circle_X), int(Circle_Y)), radius)

    pygame.display.flip()

pygame.quit()
sys.exit()
