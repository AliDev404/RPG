Premise="The world of Eryndor was once united under the power of the Crystal of Eternity, a relic that kept balance between light and shadow. But the crystal has been shattered, scattering its fragments across dangerous lands. Monsters born of shadow now roam free. You are a chosen hero, bound by fate to gather the fragments and restore the crystal before darkness consumes all."
Player_Background_Choices={
1:"Knight⚔️ - Strong in combat, honorable, high HP & Defense.",
2:"Rogue🗡 - Agile and cunning, can unlock hidden paths, high Crit chance.",
3:"Mystic🔮 - Wielder of magic, can sense secrets, high Mana & Spell damage."
}


playable_characters={
"kinght":{"name" : "Knight",
"hp" : 35,
"atk" : 7,
"defense" : 6,
"gold" : 15,
"weapon" : ("Steel Sword", 2),
},
"rogue": { 
    "name": "Rogue",
    "hp": 25,
    "atk": 6,
    "defense": 3,
    "gold": 20,
    "weapon": ("Dagger", 1),
    "crit_chance": 0.25,
    "ability": "Unlock Hidden Paths"
},
"mystic": {
    "name": "Mystic",
    "hp": 18,
    "atk": 4,
    "defense": 2,
    "gold": 15,
    "weapon": ("Magic Staff", 2),
    "mana": 40,
    "spell_power": 8,
    "ability": "Sense Secrets"
},
}



print(Premise,"\n")
for choice,chara in Player_Background_Choices.items():
	print(f"{choice}: {chara}")

Chapters={
    'c1':{
        '1':" The Burning Village",
        '2':"The Crossroads",
        '3': "The Betrayal"
        },

'c2':{
    },
}

bosses={
    'b1':{'b':"abc"

    }
}
choice_outputs={
    'c1':{
        '1':"Fight → Battle against 𝕊𝕙𝕒𝕕𝕠𝕨  𝕎𝕠𝕝𝕧𝕖𝕤.",
        '2':"Search → You save a child, who later gives you a healing charm.",
        '3':"Escape → You avoid damage but miss loot.",
    },
}




def CH1():
	s1="You awaken in the ruins of your home village, attacked by 𝑺𝒉𝒂𝒅𝒐𝒘 𝒄𝒓𝒆𝒂𝒕𝒖𝒓𝒆𝒔."
	while True:
		c1=input("You can search 𝘴𝘶𝘳𝘷𝘪𝘷𝘰𝘳𝘴, 𝘧𝘪𝘨𝘩𝘵 𝘵𝘩𝘦 𝘢𝘵𝘵𝘢𝘤𝘬𝘦𝘳𝘴, or 𝘦𝘴𝘤𝘢𝘱𝘦. (1,2,3)\n").strip()
		if c1=="1" or c1=="2" or c1 =="3":
			print(c1_output[c1])
			break
		else:
			pass

CH1()