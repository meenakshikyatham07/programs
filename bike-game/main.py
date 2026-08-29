"""Simple Bike Game using Pygame

Controls:
- Left/Right arrows or A/D: move bike left/right
- Space or Up or W: jump

Gameplay:
- Avoid oncoming obstacles. Score increases over time.
- Game over on collision. High score saved to highscore.txt.

Run:
1. python -m pip install -r requirements.txt
2. python main.py

This is a simple starter you can extend with images, sounds, and polish.
"""

import pygame
import random
import os
import sys

# Constants
WIDTH, HEIGHT = 800, 480
FPS = 60
GROUND_Y = HEIGHT - 80

BIKE_WIDTH, BIKE_HEIGHT = 60, 30
BIKE_COLOR = (20, 160, 220)
WHEEL_COLOR = (30, 30, 30)

OBSTACLE_COLOR = (200, 40, 40)
OBSTACLE_MIN_W, OBSTACLE_MAX_W = 20, 60
OBSTACLE_MIN_H, OBSTACLE_MAX_H = 30, 80

FONT_NAME = None
HIGHSCORE_FILE = "highscore.txt"

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bike Runner")
clock = pygame.time.Clock()
font = pygame.font.SysFont(FONT_NAME, 24)
large_font = pygame.font.SysFont(FONT_NAME, 48)

# Utility functions

def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip() or 0)
    except Exception:
        return 0


def save_highscore(score):
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(int(score)))
    except Exception:
        pass


class Bike:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.on_ground = True
        self.rect = pygame.Rect(self.x, self.y, BIKE_WIDTH, BIKE_HEIGHT)

    def update(self, dt):
        # Gravity
        if not self.on_ground:
            self.vy += 1400 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

        # bounds
        if self.x < 10:
            self.x = 10
        if self.x + BIKE_WIDTH > WIDTH - 10:
            self.x = WIDTH - 10 - BIKE_WIDTH

        # ground collision
        if self.y + BIKE_HEIGHT >= GROUND_Y:
            self.y = GROUND_Y - BIKE_HEIGHT
            self.vy = 0
            self.on_ground = True

        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, surf):
        # bike body
        pygame.draw.rect(surf, BIKE_COLOR, self.rect, border_radius=6)
        # wheels
        wheel_radius = 12
        left_wheel = (int(self.x + 12), int(self.y + BIKE_HEIGHT + wheel_radius - 2))
        right_wheel = (int(self.x + BIKE_WIDTH - 12), int(self.y + BIKE_HEIGHT + wheel_radius - 2))
        pygame.draw.circle(surf, WHEEL_COLOR, left_wheel, wheel_radius)
        pygame.draw.circle(surf, WHEEL_COLOR, right_wheel, wheel_radius)

    def jump(self):
        if self.on_ground:
            self.vy = -560
            self.on_ground = False


class Obstacle:
    def __init__(self, x):
        self.w = random.randint(OBSTACLE_MIN_W, OBSTACLE_MAX_W)
        self.h = random.randint(OBSTACLE_MIN_H, OBSTACLE_MAX_H)
        self.x = x
        self.y = GROUND_Y - self.h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self, speed, dt):
        self.x -= speed * dt
        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, surf):
        pygame.draw.rect(surf, OBSTACLE_COLOR, self.rect, border_radius=4)


def draw_ground(surf):
    pygame.draw.rect(surf, (30, 200, 70), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
    pygame.draw.line(surf, (20, 120, 40), (0, GROUND_Y), (WIDTH, GROUND_Y), 4)


def main():
    bike = Bike(120, GROUND_Y - BIKE_HEIGHT)
    obstacles = []
    spawn_timer = 0.0
    spawn_interval = 1.2
    base_speed = 220
    speed = base_speed
    score = 0.0
    highscore = load_highscore()
    running = True
    game_over = False

    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    if game_over:
                        # restart
                        bike = Bike(120, GROUND_Y - BIKE_HEIGHT)
                        obstacles = []
                        spawn_timer = 0.0
                        spawn_interval = 1.2
                        speed = base_speed
                        score = 0.0
                        game_over = False
                    else:
                        bike.jump()
                if event.key == pygame.K_r and game_over:
                    # restart with R key
                    bike = Bike(120, GROUND_Y - BIKE_HEIGHT)
                    obstacles = []
                    spawn_timer = 0.0
                    spawn_interval = 1.2
                    speed = base_speed
                    score = 0.0
                    game_over = False

        keys = pygame.key.get_pressed()
        if not game_over:
            bike.vx = 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                bike.vx = -220
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                bike.vx = 220

            bike.update(dt)

            # spawn obstacles
            spawn_timer += dt
            if spawn_timer >= spawn_interval:
                spawn_timer = 0.0
                x = WIDTH + random.randint(0, 120)
                obstacles.append(Obstacle(x))
                # gradually make the game harder
                spawn_interval = max(0.55, spawn_interval - 0.02)

            # update obstacles
            for ob in obstacles:
                ob.update(speed, dt)

            # remove off-screen obstacles
            obstacles = [o for o in obstacles if o.x + o.w > -50]

            # collision check
            for ob in obstacles:
                if bike.rect.colliderect(ob.rect):
                    game_over = True
                    highscore = max(highscore, int(score))
                    save_highscore(highscore)

            # update score and speed
            score += dt * 10
            speed = base_speed + score * 2.5

        # draw
        screen.fill((135, 206, 235))  # sky
        draw_ground(screen)

        for ob in obstacles:
            ob.draw(screen)
        bike.draw(screen)

        # HUD
        score_surf = font.render(f"Score: {int(score)}", True, (0, 0, 0))
        high_surf = font.render(f"High: {int(highscore)}", True, (0, 0, 0))
        screen.blit(score_surf, (10, 10))
        screen.blit(high_surf, (10, 36))

        if game_over:
            over_surf = large_font.render("Game Over", True, (180, 20, 20))
            hint_surf = font.render("Press Space or R to restart", True, (20, 20, 20))
            screen.blit(over_surf, (WIDTH // 2 - over_surf.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(hint_surf, (WIDTH // 2 - hint_surf.get_width() // 2, HEIGHT // 2 + 18))

        pygame.display.flip()

    pygame.quit()
    try:
        sys.exit(0)
    except SystemExit:
        pass


if __name__ == "__main__":
    main()
