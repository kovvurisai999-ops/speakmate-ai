from roadmap.models import Concept, Exercise

def update_phonics():
    concept = Concept.objects.get(slug='phonics')
    
    phonics_content = """
Phonics means using letter sounds to read and pronounce words correctly.
Simple gaa: A letter ela sound chestundi? Aa sounds kalipi word ela form avutundi?

WHY PHONICS IMPORTANT?
1. Correct pronunciation vastundi
2. Reading fast avvutundi
3. English fear tagguthundi
    """
    
    phonics_rules = """
PHONICS TYPES:
- Letter Sounds: A, B, C sounds
- Blending: c-a-t = cat
- Digraphs: sh, ch, th (Two letters, one sound)
    """
    
    # Updated with Word + Sentence + Meaning + Phonics Sound
    phonics_examples = [
        {"word": "Apple", "en": "I eat an apple every morning.", "te": "Nenu prati morning apple tintanu.", "sound": "A -> 'aa'", "explanation": "A for Apple: The 'A' makes the 'aa' sound."},
        {"word": "Ant", "en": "The ant is carrying food.", "te": "Cheema food teesukuntundi.", "sound": "A -> 'aa'", "explanation": "A for Ant: Similar to Apple, the 'A' is short and crisp."},
        {"word": "Ball", "en": "The boy is playing with a ball.", "te": "Abbayi ball tho aaduthunnadu.", "sound": "B -> 'buh'", "explanation": "B for Ball: The 'B' makes the 'buh' sound."},
        {"word": "Bag", "en": "My bag is on the chair.", "te": "Naa bag chair pai undi.", "sound": "B -> 'buh'", "explanation": "B for Bag: 'B' makes the 'buh' sound."},
        {"word": "Cat", "en": "The cat is sleeping.", "te": "Pilli padukundi.", "sound": "C -> 'kuh'", "explanation": "C for Cat: The 'C' makes the 'kuh' sound."},
        {"word": "Car", "en": "My father drives a car.", "te": "Naa father car naduptharu.", "sound": "C -> 'kuh'", "explanation": "C for Car: Hard 'k' sound."},
        {"word": "Dog", "en": "The dog is barking loudly.", "te": "Kukka gattiga arustundi.", "sound": "D -> 'duh'", "explanation": "D for Dog: 'D' makes the 'duh' sound."},
        {"word": "Door", "en": "Please close the door.", "te": "Door close cheyyi.", "sound": "D -> 'duh'", "explanation": "D for Door: Hard 'D' sound."},
        {"word": "Egg", "en": "I eat eggs daily.", "te": "Nenu daily eggs tintanu.", "sound": "E -> 'eh'", "explanation": "E for Egg: The 'E' makes the short 'eh' sound."},
        {"word": "Elephant", "en": "The elephant is very big.", "te": "Enugu chala peddadi.", "sound": "E -> 'eh'", "explanation": "E for Elephant: Initial 'E' is short 'eh'."},
        {"word": "Fish", "en": "The fish is swimming.", "te": "Chepa swim chestundi.", "sound": "F -> 'fuh'", "explanation": "F for Fish: 'F' is an airy 'fuh' sound."},
        {"word": "Fan", "en": "Turn on the fan.", "te": "Fan on cheyyi.", "sound": "F -> 'fuh'", "explanation": "F for Fan: Feel the air as you say 'F'."},
        {"word": "Girl", "en": "The girl is studying.", "te": "Ammayi chaduthundi.", "sound": "G -> 'guh'", "explanation": "G for Girl: The 'G' is a hard 'guh' sound."},
        {"word": "Garden", "en": "There are flowers in the garden.", "te": "Garden lo puvvulu unnayi.", "sound": "G -> 'guh'", "explanation": "G for Garden: Hard 'G' sound."},
        {"word": "House", "en": "Their house is beautiful.", "te": "Valla illu andamga undi.", "sound": "H -> 'huh'", "explanation": "H for House: 'H' is a breathy 'huh' sound."},
        {"word": "Hat", "en": "He is wearing a hat.", "te": "Atanu hat vesukunnadu.", "sound": "H -> 'huh'", "explanation": "H for Hat: Short 'a' after 'H'."},
        {"word": "Ink", "en": "The pen has blue ink.", "te": "Pen lo blue ink undi.", "sound": "I -> 'ih'", "explanation": "I for Ink: Short 'ih' sound."},
        {"word": "Ice", "en": "The ice is melting.", "te": "Ice karuguthundi.", "sound": "I -> 'ai'", "explanation": "I for Ice: Long 'ai' sound."},
        {"word": "Juice", "en": "She drinks mango juice.", "te": "Ame mango juice taguthundi.", "sound": "J -> 'juh'", "explanation": "J for Juice: 'J' makes the 'juh' sound."},
        {"word": "Jar", "en": "The jar is full of cookies.", "te": "Jar lo cookies unnayi.", "sound": "J -> 'juh'", "explanation": "J for Jar: Hard 'J' sound."},
        {"word": "Kite", "en": "The kite is flying high.", "te": "Gaalipata ekkuvaga eguruthundi.", "sound": "K -> 'kuh'", "explanation": "K for Kite: 'K' makes the 'kuh' sound."},
        {"word": "Key", "en": "I found my room key.", "te": "Naa room key dorikindi.", "sound": "K -> 'kuh'", "explanation": "K for Key: Same 'k' sound as 'Cat'."},
        {"word": "Lion", "en": "The lion roars loudly.", "te": "Simham gattiga garjisthundi.", "sound": "L -> 'luh'", "explanation": "L for Lion: 'L' is a smooth 'luh' sound."},
        {"word": "Lamp", "en": "The lamp is very bright.", "te": "Lamp chala bright gaa undi.", "sound": "L -> 'luh'", "explanation": "L for Lamp: Tongue touches the roof of mouth."},
        {"word": "Mango", "en": "Mango is sweet.", "te": "Mamidi pandu sweet gaa untundi.", "sound": "M -> 'muh'", "explanation": "M for Mango: 'M' is a humming 'mmm' sound."},
        {"word": "Mobile", "en": "My mobile is charging.", "te": "Naa mobile charging lo undi.", "sound": "M -> 'muh'", "explanation": "M for Mobile: Closed lips for 'M'."},
        {"word": "Nest", "en": "The bird built a nest.", "te": "Pakshi goodu kattindi.", "sound": "N -> 'nuh'", "explanation": "N for Nest: 'N' is a nasal 'nnn' sound."},
        {"word": "Nose", "en": "My nose is cold.", "te": "Naa mukku challaga undi.", "sound": "N -> 'nuh'", "explanation": "N for Nose: Feel the sound in your nose."},
        {"word": "Orange", "en": "The orange is juicy.", "te": "Orange juicy gaa undi.", "sound": "O -> 'o'", "explanation": "O for Orange: Round mouth for 'o' sound."},
        {"word": "Owl", "en": "The owl can see at night.", "te": "Gudlaguba ratri choostundi.", "sound": "O -> 'ow'", "explanation": "O for Owl: 'Ow' sound."},
        {"word": "Pen", "en": "This pen writes smoothly.", "te": "Ee pen smooth gaa rayuthundi.", "sound": "P -> 'puh'", "explanation": "P for Pen: Pop the sound with your lips."},
        {"word": "Phone", "en": "My phone is ringing.", "te": "Naa phone ring avutundi.", "sound": "PH -> 'f'", "explanation": "Ph for Phone: 'PH' together make the 'f' sound."},
        {"word": "Queen", "en": "The queen wore a crown.", "te": "Rani crown vesukundi.", "sound": "Q -> 'kwuh'", "explanation": "Q for Queen: 'Q' is almost always 'kwuh'."},
        {"word": "Question", "en": "The student asked a question.", "te": "Student oka question adigadu.", "sound": "Q -> 'kwuh'", "explanation": "Q for Question: 'KW' sound."},
        {"word": "Rabbit", "en": "The rabbit is running fast.", "te": "Kundelu fast gaa parigeduthundi.", "sound": "R -> 'ruh'", "explanation": "R for Rabbit: Curl your tongue for 'ruh'."},
        {"word": "Rain", "en": "It is raining outside.", "te": "Bayata varsham paduthundi.", "sound": "R -> 'ruh'", "explanation": "R for Rain: Smooth 'R' sound."},
        {"word": "Sun", "en": "The sun is very hot today.", "te": "Eeroju suryudu chala vediga unnadu.", "sound": "S -> 'sss'", "explanation": "S for Sun: Hissing 'sss' sound."},
        {"word": "School", "en": "Children are going to school.", "te": "Pillalu school ki velthunnaru.", "sound": "S -> 'sss'", "explanation": "S for School: 'S' followed by 'k' sound."},
        {"word": "Tiger", "en": "The tiger is strong.", "te": "Puli balanga untundi.", "sound": "T -> 'tuh'", "explanation": "T for Tiger: Tap your tongue for 'tuh'."},
        {"word": "Table", "en": "The books are on the table.", "te": "Books table pai unnayi.", "sound": "T -> 'tuh'", "explanation": "T for Table: Crisp 'T' sound."},
        {"word": "Umbrella", "en": "Take an umbrella with you.", "te": "Umbrella teesuko.", "sound": "U -> 'uh'", "explanation": "U for Umbrella: Short 'uh' sound."},
        {"word": "Uniform", "en": "Students wear uniforms.", "te": "Students uniforms vestharu.", "sound": "U -> 'yu'", "explanation": "U for Uniform: Long 'yu' sound."},
        {"word": "Van", "en": "The van stopped near the shop.", "te": "Van shop daggara aagindi.", "sound": "V -> 'vuh'", "explanation": "V for Van: Vibrate your lower lip on teeth."},
        {"word": "Village", "en": "My grandparents live in a village.", "te": "Naa grandparents village lo untaru.", "sound": "V -> 'vuh'", "explanation": "V for Village: Similar to 'Van'."},
        {"word": "Water", "en": "Drink more water daily.", "te": "Daily ekkuva neeru tagandi.", "sound": "W -> 'wuh'", "explanation": "W for Water: Round your lips for 'wuh'."},
        {"word": "Watch", "en": "My watch shows the time.", "te": "Naa watch time chupisthundi.", "sound": "W -> 'wuh'", "explanation": "W for Watch: Quick 'W' sound."},
        {"word": "Xylophone", "en": "The child plays the xylophone.", "te": "Pillavadu xylophone aaduthunnadu.", "sound": "X -> 'zzz'", "explanation": "X for Xylophone: Here 'X' sounds like 'Z'."},
        {"word": "Yellow", "en": "Yellow is my favorite color.", "te": "Yellow naa favorite color.", "sound": "Y -> 'yuh'", "explanation": "Y for Yellow: Tongue starts high for 'yuh'."},
        {"word": "Yogurt", "en": "I eat yogurt after lunch.", "te": "Lunch tarvata yogurt tintanu.", "sound": "Y -> 'yuh'", "explanation": "Y for Yogurt: Same as Yellow."},
        {"word": "Zebra", "en": "The zebra has black stripes.", "te": "Zebra ki black lines untayi.", "sound": "Z -> 'zzz'", "explanation": "Z for Zebra: Buzzing 'zzz' sound."},
    ]
    
    concept.content = phonics_content
    concept.grammar_rules = phonics_rules
    concept.examples = phonics_examples
    concept.save()
    print("Phonics successfully updated with Full Sentences!")

if __name__ == "__main__":
    update_phonics()
