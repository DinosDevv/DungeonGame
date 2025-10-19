class level:
  def __init__(self, name: str, level_difficulty: int, amount_of_enemies: int, amount_of_loot: int) -> None:
    self.name = name
    self.level_difficulty = level_difficulty
    self.amount_of_enemies = amount_of_enemies
    self.amount_of_loot = amount_of_loot

  def text_introduction(self) -> str:
    return 

level_01: level = level("Scavenger", 1, 5, 0)
level_02: level = level("Iron Thief", 2, 5, 10)
level_03: level = level("Toxic Raider", 3, 2, 20)
level_04: level = level("Ashen Behemoth", 4, 1, 500)
level_05: level = level("Wasteland Colossus", 5, 1, 1000)

levels = [level_01, level_02, level_03, level_04, level_05]