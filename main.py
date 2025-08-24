import Character as c
import Battle as b

def Start():
    name=input("Enter your name: ")
    return name





    print("\nYou are an adventurer traveling through a kingdom plagued by a dark curse.\
The King has promised a reward to anyone who can defeat the Shadow Beast that dwells deep within the cursed forest.")
    print("You are in a small village.\nThe villagers warn you about the dangers ahead.\n")
    choose=input("***\n1)Buy a healing potion from the shop.\n2)Speak to the old wise man.\n3)Head straight into the forest.\n***\n")
    

player1 = c.Player(Start())
print(player1)
enemy1= c.Enemy("Goblin", hp=15, atk=2, defense=1, reward_gold=5, reward_items=["Rusty Dagger"])

def fight():
    battle = b.battle(player1,enemy1)
    battle.start()

fight()