TITLE="The Cursed Forest"

STARTING="You are a wandering adventurer with a rusty sword, a small lantern, and a pouch with 3 gold coins. Legends speak of a cursed forest that hides a treasure guarded by something terrible. Tonight, you stand before its dark edge."

level_no ={
	"1" : "At the Forest’s Edge",
	"2" : "The Whispering Path",
	"3" : "The Old Hermit",
	"4" : "Battle with the Wolf",
	"5" : "The Bargain",
	"6" : "The Healing Herb",
	"7" : "The Clearing",
	"8" : "Final Battle",
	"9" : "The Trick"
	}

level_story={
	"1" : "The trees loom tall and silent, their branches twisting like claws. A narrow path disappears into the shadows.",
	"2" : "As you walk, the lantern flickers. Voices whisper from the trees. Suddenly, a pair of glowing yellow eyes appear.It’s a wolf, blocking the path.",
	"3" : "You find a crooked hut. An old hermit waves you closer. He says, “The forest hides what you seek, but beware the Shadow Beast.” He offers you a choice:",
	"4" : "You swing your sword. The wolf lunges. After a brief fight, you manage to wound it, but it scratches your arm. You lose some strength, yet the beast flees.You continue deeper.",
	"5" : "You toss a coin onto the path. The wolf sniffs it, growls, then slinks away into the shadows. You’re safe, but poorer.",
	"6" : "The herb restores your energy. Feeling stronger, you step into the forest.",
	"7" : "The path opens to a moonlit clearing. At its center lies a stone altar, upon which rests a silver chest. But from the shadows rises the Shadow Beast, tall, horned, and wrapped in darkness.",
	"8" : "The fight is fierce. If you took the hermit’s herb (Section 6), you strike with renewed strength and the beast dissolves into smoke. Inside the chest is a golden crown—the treasure is yours. Victory!",
	"9" : "You toss your lantern high, its flame flaring bright. The beast snarls and shields its eyes. You dash to the chest, grab it, and run.",
}

choices={
	"1" : ("enter the forest","circle around the forest"),
"2" : ("fight the wolf","offer it a gold coin"),
"3" : ("accept his advice and take a healing herb","ignore him and head back into the forest"),
"4" : ("",""),
"5" : ("",""),
"6" : ("",""),
"7" : ("fight the Shadow Beast","try to trick it and flee with the chest"),
"8" : ("","")
}

choice_outputs{
	{}
}
The trees loom tall and silent, their branches twisting like claws. A narrow path disappears into the shadows.

If you enter the forest, go to Section 2.
If you circle around the forest, go to Section 3.

Section 2 – The Whispering Path

As you walk, the lantern flickers. Voices whisper from the trees. Suddenly, a pair of glowing yellow eyes appear.
It’s a wolf, blocking the path.

If you fight the wolf, go to Section 4.
If you offer it a gold coin, go to Section 5.

Section 3 – The Old Hermit

You find a crooked hut. An old hermit waves you closer. He says, “The forest hides what you seek, but beware the Shadow Beast.” He offers you a choice:

If you accept his advice and take a healing herb, go to Section 6.
If you ignore him and head back into the forest, go to Section 2.

Section 4 – Battle with the Wolf

You swing your sword. The wolf lunges. After a brief fight, you manage to wound it, but it scratches your arm. You lose some strength, yet the beast flees.
You continue deeper. Go to Section 7.

Section 5 – The Bargain

You toss a coin onto the path. The wolf sniffs it, growls, then slinks away into the shadows. You’re safe, but poorer.
Go to Section 7.

Section 6 – The Healing Herb

The herb restores your energy. Feeling stronger, you step into the forest.
Go to Section 7.

Section 7 – The Clearing

The path opens to a moonlit clearing. At its center lies a stone altar, upon which rests a silver chest. But from the shadows rises the Shadow Beast, tall, horned, and wrapped in darkness.

If you fight the Shadow Beast, go to Section 8.

If you try to trick it and flee with the chest, go to Section 9.

Section 8 – Final Battle

The fight is fierce. If you took the hermit’s herb (Section 6), you strike with renewed strength and the beast dissolves into smoke. Inside the chest is a golden crown—the treasure is yours. Victory!

If you didn’t take the herb, the beast overpowers you. Darkness consumes you. The End.

Section 9 – The Trick

You toss your lantern high, its flame flaring bright. The beast snarls and shields its eyes. You dash to the chest, grab it, and run.
END="When you finally escape the forest, you open it… only to find nothing but ashes. The curse remains unbroken. The End."