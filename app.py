import pygame
import sys
from entities import Player, Enemy
from utils import WIDTH, HEIGHT

# Initialize Pygame

pygame.init()

# Window Setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wastelands")

# Instantiating Player

player: Player = Player("Kostaras", 0, 100, 5, 5, 0, 10, 0.3, [])
starting_player_health = player.health

enemy: Enemy = Enemy("Zombie", 100, 50,100, 100)
enemies = [enemy]

# Initializing Graphics / UI

background_image = pygame.image.load("sprites/bg.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
font = pygame.font.Font(None, 74)

# Check if joystick is available

if pygame.joystick.get_count() > 0:
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  print(f"Controller connect: {joystick.get_name()}")

# Main Loop

clock = pygame.time.Clock() # Adds ticks (frames)
running = True

while running:
  # Joystick Input

  x_axis = joystick.get_axis(0)
  y_axis = joystick.get_axis(1)

  percented_health = player.health / starting_player_health * 100 # Making Health a percentage instead of raw number

  # Health Text

  health_text = font.render(f'{percented_health}%', True, (255, 255, 255))
  text_rect = health_text.get_rect(center=(100, 100))

  # Adds a minimum needed input from joystick to move

  if x_axis > 0.5 or x_axis < -0.5:
    player.x_move(x_axis)
  if y_axis > 0.5 or y_axis < -0.5:
    player.y_move(y_axis)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Updates Graphics

  screen.blit(background_image, (0, 0))
  screen.blit(health_text, text_rect)
  
  # Instantiate Enemies

  for entity in enemies:
    entity.spawn(screen)
  player.spawn(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()