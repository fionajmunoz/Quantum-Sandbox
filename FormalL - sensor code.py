import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particles Moving Away from Cursor")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
    (0, 255, 255), (255, 0, 255), (23, 54, 119)
]

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(5, 12)
        self.color = random.choice(RANDOM_COLORS)

    def move_away(self, target_x, target_y):
        # Calculate the vector away from the target (mouse cursor)
        dx = self.x - target_x
        dy = self.y - target_y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalize the vector and move the particle away
        if distance != 0:
            dx /= distance
            dy /= distance
        self.x += dx * 2  # Move further away by a factor of 2
        self.y += dy * 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Main loop
particles = []
running = True
clock = pygame.time.Clock()

# Particle generation rate (how often to create a new particle, in milliseconds)
particle_generation_rate = 45  # milliseconds
last_generated_time = pygame.time.get_ticks()  # Time when the last particle was generated

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if it's time to create a new particle
    current_time = pygame.time.get_ticks()
    if current_time - last_generated_time > particle_generation_rate:
        # Create a new particle at a random position
        x = random.randint(0, width)
        y = random.randint(0, height)
        particles.append(Particle(x, y))
        last_generated_time = current_time  # Update the last generated time

    # Update and move particles
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for particle in particles:
        particle.move_away(mouse_x, mouse_y)
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
