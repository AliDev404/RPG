class Character:
    def __init__(self, name, hp, atk, defense=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def attack_damage(self):
        return self.atk

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name.capitalize()} | HP: {self.hp}/{self.max_hp} | ATK: {self.atk} | DEF: {self.defense}"


class Player(Character):
    def __init__(self, name, hp=20, atk=5, defense=2, gold=10, weapon=("Normal Sword", 0)):
        super().__init__(name, hp, atk, defense)
        self.gold = gold
        self.inventory = []
        self.weapon = weapon

    def attack_damage(self):
        return self.atk + self.weapon[1]

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def add_item(self, item):
        self.inventory.append(item)

    def change_weapon(self, weapon_name, bonus):
        self.weapon = (weapon_name, bonus)

    def __str__(self):
        return (f"{self.name.capitalize()} | HP: {self.hp}/{self.max_hp} | "
                f"ATK: {self.atk}+{self.weapon[1]} | DEF: {self.defense} | "
                f"Gold: {self.gold} | Weapon: {self.weapon[0]} | "
                f"Inventory: {self.inventory}")


class Enemy(Character):
    def __init__(self, name, hp, atk, defense=0, reward_gold=0, reward_items=None):
        super().__init__(name, hp, atk, defense)
        self.reward_gold = reward_gold
        self.reward_items = reward_items if reward_items else []

    def drop_rewards(self):
        if not self.is_alive():
            return {"gold": self.reward_gold, "items": self.reward_items}
        return {"gold": 0, "items": []}

    def __str__(self):
        return (f"{self.name.capitalize()} | HP: {self.hp}/{self.max_hp} | "
                f"ATK: {self.atk} | DEF: {self.defense} | "
                f"Reward: {self.reward_gold} gold, {self.reward_items}")



