###Fiona
###Quantum Sandbox Mix

#Particles
import pygame
import random
import math

#Sensors
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

import pygame
import random
import math

#Initialize pygame
pygame.init()

#Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particles Moving Away from Cursor")

# Colors - Shades of Purple, Red, and Blue
COLOR_PALETTE = [
    (128, 0, 128), (75, 0, 130), (139, 0, 139), (102,0,204),  # Purples
    (255, 0, 0), (178, 34, 34), (220, 20, 60),   # Reds
    (0, 0, 255), (30, 144, 255), (70, 130, 180)  # Blues
]

#article class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(5, 12)
        self.color = random.choice(COLOR_PALETTE)

    def move_away(self, target_x, target_y):
        dx = self.x - target_x
        dy = self.y - target_y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance != 0:
            dx /= distance
            dy /= distance
        self.x += dx * 3  # Increased speed away from cursor
        self.y += dy * 3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
class PhidgetSensor:
    def __init__ (self, port, sensor_type=VoltageRatioSensorType.SENSOR_TYPE_1108):
        self.sensors = []
        self.port = port
        self.sensor_type = sensor_type 
    
    def on_sensor_change(self, sensor, sensorValue, sensorUnit):
        print(f"Sensor on Hub {sensor.getHubPort()} - Value: {sensorValue} {sensorUnit.symbol}")
        print("----------")
        
    def sensor_starts(self):
        for port in self.port:
            sensor = VoltageRatioInput()
            sensor.setIsHubPortDevice(True)
            sensor.setHubPort(port)
            sensor.setOnSensorChangeHandler(self.on_sensor_change)
            sensor.openWaitForAttachment(5000)
            sensor.setSensorType(self.sensor_type)
            self.sensors.append(sensor)
            
    def close_sensor(self):
        for sensor in self.sensors:
            sensor.close()
            
    def run(self):
        try:
            input("Press Enter to stop...\n")
        except (Exception, KeyboardInterrupt):
            pass
        finally:
            self.close_sensors()

#Main loop
particles = []
running = True
clock = pygame.time.Clock()

#Increased Particle Generation Rate
particle_generation_rate = 10
last_generated_time = pygame.time.get_ticks()


while running:    
    #screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Generate more particles at a higher rate
    current_time = pygame.time.get_ticks()
    if current_time - last_generated_time > particle_generation_rate:
        x = random.randint(0, width)
        y = random.randint(0, height)
        particles.append(Particle(x, y))
        last_generated_time = current_time

    #Update and move particles
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for particle in particles:
        particle.move_away(mouse_x, mouse_y)
        particle.draw(screen)
        
    sensorsets = PhidgetSensor(port=[1, 2, 3, 4])
    sensorsets.sensor_starts()
    sensorsets.run()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

