import Character as c
import Battle as b
import save

file = save.SaveLoader()


def Start():
    while True:
        new=input("1) New game: \n2) Load Game\n3) Show all saves\n").strip()
        if new=='1' or new == '2':
            name=input("Enter your name: ").strip().lower()
            if new=='1':
                Save(name,0)
                break
            elif new=='2':
                Load(name)
                break
        elif new=='3':
            All_saves()

        else:
            pass
        

enemy1= c.Enemy("Goblin", hp=15, atk=2, defense=1, reward_gold=5, reward_items=["Rusty Dagger"])






def Fight():
    battle = b.battle(player1,enemy1)
    battle.start()

def Load(name):
    return file.load(name)

def All_saves():
    return file.show_all_save()

def Save(name,current_level):
    return file.save(name,current_level)

name = Start()
player = c.Player(name)
print(player)