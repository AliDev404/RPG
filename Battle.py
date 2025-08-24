
class battle:
    def __init__(self, player, enemy):
        self.player=player
        self.enemy=enemy
    
    def start(self):
        while self.player.is_alive() and self.enemy.is_alive():
            dmg = self.enemy.take_damage(self.player.attack_damage())
            print(f"{self.player.name} hits {self.enemy.name} for {dmg} damage! ({self.enemy.hp} HP left)")

            if self.enemy.is_alive():
                dmg =self.player.take_damage(self.enemy.attack_damage())
                print(f"{self.enemy.name} hits {self.player.name} for {dmg} damage! ({self.player.hp} HP left)")

            
        if not self.player.is_alive():
            print("\a\n\n***YOU DIE!***")
            return
                    
        if not self.enemy.is_alive():
            rewards= self.enemy.drop_rewards()
            self.player.gold += rewards["gold"]
            self.player.inventory.extend(rewards["items"])
            print(f"\n***{self.player.name} defeated {self.enemy.name} and received {rewards}!***")
        