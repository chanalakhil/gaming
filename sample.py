from abc import ABC, abstractmethod
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class Entity(ABC):
    """Base class for all entities in the game."""
    def __init__(self, position, health):
        self.position = position
        self.health = health

    @abstractmethod
    def update(self):
        """Update the entity's state."""
        pass

    @abstractmethod
    def render(self):
        """Render the entity."""
        pass

class Character(Entity):
    """The player character."""
    def __init__(self, position, health, name, inventory):
        super().__init__(position, health)
        self.name = name
        self.inventory = inventory
        self.weapon = None

    def attack(self, direction):
        """Attack in a direction."""
        if self.weapon:
            damage = self.weapon.damage
            print(f"Attacking {direction.name} with {self.weapon.blade_type} for {damage} damage!")
        else:
            print("You don't have a weapon equipped!")

    def equip_weapon(self, weapon):
        """Equip a weapon."""
        self.weapon = weapon
        print(f"Equipped {weapon.blade_type}!")

class Enemy(Entity, ABC):
    """Base class for all enemies."""
    def __init__(self, position, health, attack_power, defense):
        super().__init__(position, health)
        self.attack_power = attack_power
        self.defense = defense

    @abstractmethod
    def attack_character(self, character):
        """Attack the character."""
        pass

class Skeleton(Enemy):
    """A skeleton enemy."""
    def __init__(self, position, health, attack_power, defense, bone_type):
        super().__init__(position, health, attack_power, defense)
        self.bone_type = bone_type

    def attack_character(self, character):
        """Attack the character."""
        damage = self.attack_power
        print(f"Attacking {character.name} for {damage} damage!")
        character.health -= damage

class Ghost(Enemy):
    """A ghost enemy."""
    def __init__(self, position, health, attack_power, defense, transparency):
        super().__init__(position, health, attack_power, defense)
        self.transparency = transparency

    def attack_character(self, character):
        """Attack the character."""
        damage = self.attack_power
        print(f"Attacking {character.name} for {damage} damage!")
        character.health -= damage

class Goblin(Enemy):
    """A goblin enemy."""
    def __init__(self, position, health, attack_power, defense, tribe):
        super().__init__(position, health, attack_power, defense)
        self.tribe = tribe

    def attack_character(self, character):
        """Attack the character."""
        damage = self.attack_power
        print(f"Attacking {character.name} for {damage} damage!")
        character.health -= damage

class Weapon(ABC):
    """Base class for all weapons."""
    def __init__(self, damage, range, blade_type):
        self.damage = damage
        self.range = range
        self.blade_type = blade_type

    @abstractmethod
    def use(self, character):
        """Use the weapon."""
        pass

class Sword(Weapon):
    """A sword weapon."""
    def __init__(self, damage, range, blade_type):
        super().__init__(damage, range, blade_type)

    def use(self, character):
        """Use the sword."""
        character.attack(Direction.NORTH)

class Spear(Weapon):
    """A spear weapon."""
    def __init__(self, damage, range, shaft_type):
        super().__init__(damage, range, shaft_type)

    def use(self, character):
        """Use the spear."""
        character.attack(Direction.EAST)

class Crossbow(Weapon):
    """A crossbow weapon."""
    def __init__(self, damage, range, bolt_type):
        super().__init__(damage, range, bolt_type)

    def use(self, character):
        """Use the crossbow."""
        character.attack(Direction.SOUTH)

# Example usage:
player = Character((0, 0), 100, "Hero", [])
sword = Sword(10, 1, "Longsword")
player.equip_weapon(sword)

skeleton = Skeleton((1, 1), 50, 5, 2, "Ribs")
ghost = Ghost((2, 2), 75, 10, 3, 0.5)
goblin = Goblin((3, 3), 25, 3, 1, "Orc")

player.attack(Direction.NORTH)  # Output: Attacking NORTH with Longsword for 10 damage!
skeleton.attack_character(player)  # Output: Attacking Hero for 5 damage!
ghost.attack_character(player)  # Output: Attacking Hero for 10 damage!
goblin.attack_character(player)  # Output: Attacking Hero for 3 damage!