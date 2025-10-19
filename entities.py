import pygame
import random
from utils import *

# Player Class

class Player: 
  def __init__(self, name: str, level: int, health: float, attack: float, defense: float, xp: int, gold: int, velocity: float, inventory: list) -> None:
    self.name = name
    self.level = level
    self.health = health
    self.attack = attack
    self.defense = defense
    self.xp = xp
    self.gold = gold
    self.velocity = velocity
    self.inventory = inventory

    self.x_scale = 108
    self.y_scale = 150

    self.x_pos = WIDTH / 2 - self.x_scale / 2
    self.y_pos = HEIGHT / 2 - self.y_scale / 2

    self.sprite = pygame.image.load("sprites/player.png").convert_alpha()
    self.sprite = pygame.transform.scale(self.sprite, (self.x_scale, self.y_scale))

  def spawn(self, screen):
    screen.blit(self.sprite, (self.x_pos, self.y_pos))

  def x_move(self, axis):
    self.x_pos += axis * self.velocity

  def y_move(self, axis):
    self.y_pos += axis * self.velocity


# Enemy Class

class Enemy:
  def __init__(self, name: str, health: float, attack: float, xp_reward: int, gold_reward: int) -> None:
    self.name = name
    self.health = health
    self.attack = attack
    self.xp_reward = xp_reward
    self.gold_reward = gold_reward

    self.x_pos = random.randint(MAP_X_MIN, MAP_X_MAX)
    self.y_pos = random.randint(MAP_Y_MIN, MAP_Y_MAX)

    self.sprite = pygame.image.load("sprites/enemy.png").convert_alpha()
    self.sprite = pygame.transform.scale(self.sprite, (100, 100))


  def spawn(self, screen):
    screen.blit(self.sprite, (self.x_pos, self.y_pos))

    
