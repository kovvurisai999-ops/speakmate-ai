import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def add_exercises(concept_slug, exercises_data):
    try:
        concept = Concept.objects.get(slug=concept_slug)
        # We overwrite to ensure Telugu meanings are updated
        print(f"Updating exercises for {concept_slug}...")
        Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
        
        for q, ans, hint, exp, opts in exercises_data:
            Exercise.objects.create(
                concept=concept,
                type='FILL_BLANK',
                question=q,
                correct_answer=ans,
                hint=hint,
                explanation=exp,
                options=opts
            )
        print(f"Finished {concept_slug}. Total: {len(exercises_data)}")
    except Concept.DoesNotExist:
        print(f"Concept {concept_slug} not found.")

def main():
    # 1. ALPHABETS (20)
    alphabets_exercises = [
        ("The letter after 'C' is _____.", "D", "C tarvata vachae letter.", "Alphabet sequence lo A, B, C tarvata D vastundi.", ["D", "E", "F"]),
        ("The letter before 'Z' is _____.", "Y", "Z mundu vachae letter.", "Z anedi last letter, dini mundu Y untundi.", ["X", "Y", "W"]),
        ("Apple starts with the letter _____.", "A", "Apple ae aksharam tho modalu avutundi?", "Apple ane padaniki modati aksharam A.", ["A", "B", "C"]),
        ("The last letter of the alphabet is _____.", "Z", "Alphabet lo chivari aksharam.", "English alphabet lo 26th letter Z.", ["X", "Y", "Z"]),
        ("There are _____ vowels in English.", "five", "English lo enni vowels (achulu) unnayi?", "Vowels: A, E, I, O, U - ivvi motham 5.", ["four", "five", "six"]),
        ("The letter 'B' comes after _____.", "A", "B deni tarvata vastundi?", "Alphabet lo modati aksharam A, tarvata B vastundi.", ["A", "C", "D"]),
        ("The word 'Cat' starts with _____.", "C", "Cat ae letter tho start avutundi?", "Cat lo modati aksharam C.", ["K", "C", "S"]),
        ("The letter between 'G' and 'I' is _____.", "H", "G mariyu I madhyalo vachae letter.", "Sequence lo G tarvata H, tarvata I vastundi.", ["H", "J", "F"]),
        ("The letter 'M' comes before _____.", "N", "M deni mundu vastundi?", "Sequence lo L, M, N... kabatti M tarvata N vastundi.", ["L", "O", "N"]),
        ("Small letter of 'G' is _____.", "g", "G ki small letter cheppandi.", "Capital 'G' ni small letters lo 'g' ani rastam.", ["q", "p", "g"]),
        ("The first letter of a name starts with a _____ letter.", "capital", "Peru lo modati aksharam katchitanga _____ ga undali.", "Evari peraina modata capital letter tho start cheyyali.", ["small", "capital", "middle"]),
        ("The letter 'Q' is followed by _____.", "R", "Q tarvata vachae letter.", "P, Q tarvata vachae aksharam R.", ["P", "S", "R"]),
        ("The word 'Sun' starts with _____.", "S", "Sun ae aksharam tho start avutundi?", "Sun ane padaniki modati aksharam S.", ["C", "S", "Z"]),
        ("How many letters are there in 'English'? _____.", "seven", "English ane padam lo enni aksharalu unnayi?", "E-n-g-l-i-s-h count chesthe 7 letters.", ["six", "seven", "eight"]),
        ("The letter after 'P' is _____.", "Q", "P tarvata vachae letter.", "O, P tarvata Q vastundi.", ["O", "Q", "R"]),
        ("The letter before 'F' is _____.", "E", "F mundu vachae letter.", "E tarvata F vastundi, kabatti F mundu E untundi.", ["D", "E", "G"]),
        ("The letter 'K' is for _____.", "Kite", "K tho modalaayae padam.", "Kite (gali patam) K letter tho start avutundi.", ["Apple", "Kite", "Dog"]),
        ("The letter 'L' is for _____.", "Lion", "L tho modalaayae jantuuvu peru.", "Lion (simham) L letter tho start avutundi.", ["Tiger", "Lion", "Cat"]),
        ("The letter 'O' is a _____.", "vowel", "O anedi vowel aa leka consonant aa?", "A, E, I, O, U lo O okati, kabatti idi vowel.", ["vowel", "consonant", "number"]),
        ("The letter 'T' comes after _____.", "S", "T deni tarvata vastundi?", "Sequence lo S tarvata T vastundi.", ["R", "S", "U"]),
    ]

    # 2. PHONICS (20)
    phonics_exercises = [
        ("The sound of 'B' is _____.", "buh", "B aksharam yokka sound.", "B ni 'buh' ani palukutham, udaharana: Boy.", ["buh", "cuh", "duh"]),
        ("The 'A' in Apple sounds like _____.", "ah", "Apple lo A sound ela untundi?", "Apple lo A 'ah' ani palukutham.", ["ah", "ay", "ee"]),
        ("The 'C' in Cat sounds like _____.", "cuh", "Cat lo C sound.", "C aksharam ikkada 'k' (cuh) sound chestundi.", ["cuh", "suh", "guh"]),
        ("The 'S' in Snake sounds like _____.", "sss", "Snake lo S sound.", "S aksharam 'sss' ane sound chestundi.", ["sss", "zzz", "mmm"]),
        ("Which letter makes the 'puh' sound? _____.", "P", "'puh' sound ae aksharam chestundi?", "P letter 'puh' ani sound chestundi (Pen).", ["B", "P", "D"]),
        ("The 'E' in Egg sounds like _____.", "eh", "Egg lo E sound.", "Egg lo E ni 'eh' ani palukutham.", ["ee", "eh", "ay"]),
        ("The 'F' in Fish sounds like _____.", "fff", "Fish lo F sound.", "F letter gali vadilinattu 'fff' ani sound chestundi.", ["fff", "vvv", "ppp"]),
        ("The 'G' in Goat sounds like _____.", "guh", "Goat lo G sound.", "G letter 'guh' ani sound chestundi.", ["juh", "guh", "kuh"]),
        ("The 'H' in Hat sounds like _____.", "huh", "Hat lo H sound.", "H letter 'huh' ani breath sound chestundi.", ["huh", "aaa", "ooo"]),
        ("The 'I' in Igloo sounds like _____.", "ih", "Igloo lo I sound.", "Igloo lo I 'ih' ani chinna sound chestundi.", ["eye", "ih", "ee"]),
        ("Which letter sounds like 'mmm'? _____.", "M", "'mmm' sound ae aksharam chestundi?", "M letter noti tho 'mmm' ani hum sound chestundi.", ["N", "M", "L"]),
        ("The 'D' in Dog sounds like _____.", "duh", "Dog lo D sound.", "D letter 'duh' ani sound chestundi.", ["tuh", "duh", "buh"]),
        ("The 'T' in Tiger sounds like _____.", "tuh", "Tiger lo T sound.", "T letter 'tuh' ani sound chestundi.", ["duh", "tuh", "puh"]),
        ("The 'V' in Van sounds like _____.", "vvv", "Van lo V sound.", "V letter vibrating sound 'vvv' chestundi.", ["vvv", "fff", "bbb"]),
        ("The 'W' in Watch sounds like _____.", "wuh", "Watch lo W sound.", "W letter 'wuh' ani lips tho sound chestundi.", ["wuh", "vuh", "ooo"]),
        ("The 'J' in Jug sounds like _____.", "juh", "Jug lo J sound.", "J letter 'juh' ani sound chestundi.", ["juh", "yuh", "guh"]),
        ("The 'K' in Kite sounds like _____.", "kuh", "Kite lo K sound.", "K letter 'kuh' ani hard sound chestundi.", ["cuh", "kuh", "guh"]),
        ("The 'L' in Lamp sounds like _____.", "lll", "Lamp lo L sound.", "L letter నాలుకతో 'lll' sound chestundi.", ["lll", "rrr", "nnn"]),
        ("The 'N' in Net sounds like _____.", "nnn", "Net lo N sound.", "N letter mukkutho 'nnn' sound chestundi.", ["nnn", "mmm", "lll"]),
        ("The 'R' in Rat sounds like _____.", "rrr", "Rat lo R sound.", "R letter 'rrr' ani sound chestundi.", ["rrr", "lll", "www"]),
    ]

    # 3. SELF INTRODUCTION (20)
    self_intro_exercises = [
        ("My name _____ Sai.", "is", "Naa peru Sai ani cheppali.", "Singular subjects (peru) ki 'is' use chestham.", ["is", "am", "are"]),
        ("I _____ from Hyderabad.", "am", "Nenu Hyderabad nunchi vachanu.", "I tho eppudu 'am' use cheyyali.", ["is", "am", "are"]),
        ("I _____ 20 years old.", "am", "Naa vayasau 20 ellu.", "Vayasau cheppadaniki 'I am' antam.", ["is", "am", "are"]),
        ("My hobby _____ reading books.", "is", "Pusthakalu chaduvadam naa hobby.", "Okka hobby gurinchi cheppetappudu 'is' vadutham.", ["is", "are", "am"]),
        ("I _____ studying B.Tech.", "am", "Nenu B.Tech chaduvutunnanu.", "I am + studying (continuous action).", ["am", "is", "are"]),
        ("Thank you for _____ me this opportunity.", "giving", "Ee avakasam ichinanduku dhanyavadhamulu.", "Modata start cheyyadaniki 'giving' use chestham.", ["giving", "gave", "give"]),
        ("I completed my graduation _____ 2023.", "in", "Nenu 2023 lo graduation poorthi chesanu.", "Years (samvatsaralu) mundu 'in' vadali.", ["on", "at", "in"]),
        ("There are four members _____ my family.", "in", "Maa family lo naluguru unnaru.", "Kutumbam lo ani cheppadaniki 'in' vadali.", ["in", "at", "on"]),
        ("My father _____ a teacher.", "is", "Maa nanna teacher.", "He/She/It singular nouns ki 'is' vadali.", ["is", "am", "are"]),
        ("I want to _____ a software engineer.", "become", "Nenu software engineer avvali ani anukuntunnanu.", "Future goal cheppadaniki 'become' vadutham.", ["be", "become", "doing"]),
        ("My strengths _____ hard work and honesty.", "are", "Naa balaalu hard work mariyu honesty.", "Plural (ekkuva) strengths unnappudu 'are' vadali.", ["is", "are", "am"]),
        ("I am _____ in frontend technologies.", "skilled", "Naku frontend technologies lo pranyanyam undi.", "Manaku unna skills ni describe cheyyadaniki 'skilled' vadutham.", ["skilled", "skill", "skilling"]),
        ("Currently, I am _____ in Guntur.", "living", "Ippudu nenu Guntur lo untunnanu.", "Ippudu unna place gurinchi 'living' antam.", ["live", "living", "lived"]),
        ("My short-term goal is to _____ a job.", "get", "Naa goal job kottadam.", "Goal poorthi cheyyadaniki 'get' a job antam.", ["get", "got", "getting"]),
        ("I _____ like to play cricket.", "also", "Naku cricket aadadam kuda istam.", "Inka extra vishayalu cheppadaniki 'also' vadutham.", ["too", "also", "very"]),
        ("Nice to _____ you all.", "meet", "Mimmalni kalavadam santosham.", "Closing phrase lo 'nice to meet you' antam.", ["see", "meet", "talk"]),
        ("I can _____ English fluently.", "speak", "Nenu English baga matladagalanu.", "Ability (saamarthyam) cheppadaniki 'speak' vadali.", ["talk", "speak", "say"]),
        ("I am a self-motivated _____.", "person", "Nenu self-motivated vyakthini.", "Nee gurinchi okka word lo cheppadaniki 'person' vadutham.", ["person", "boy", "student"]),
        ("My native place _____ Visakhapatnam.", "is", "Maadi Visakhapatnam.", "Native place singular kabatti 'is' vadutham.", ["is", "am", "was"]),
        ("That's _____ about me.", "all", "Naa gurinchi anthe.", "Intro finish cheyyadaniki 'That's all' antam.", ["all", "everything", "finished"]),
    ]

    # 4. DAILY WORDS (20)
    daily_words_exercises = [
        ("I eat _____ in the morning.", "breakfast", "Udayam nenu tine tindi.", "Morning meal ni 'breakfast' antaru.", ["lunch", "dinner", "breakfast"]),
        ("Please _____ the door.", "open", "Door (talupu) teeyi.", "Action cheppadaniki 'open' vadutham.", ["open", "eat", "run"]),
        ("I drink _____ every day.", "water", "Nenu roju idi tagutanu.", "Batikundadaniki water chala mukhyam.", ["food", "water", "book"]),
        ("I go to _____ at 9 AM.", "office", "Nenu 9 gantulaki ikkadiki velthanu.", "Work place ni 'office' antaru.", ["bed", "office", "park"]),
        ("Brush your _____ twice a day.", "teeth", "Roju rendu sarlu pallu tomukovali.", "Pallu ni English lo 'teeth' antaru.", ["hair", "teeth", "face"]),
        ("I read the _____ daily.", "newspaper", "Roju nenu paper chaduvuthanu.", "Information source ni 'newspaper' antaru.", ["movie", "newspaper", "music"]),
        ("Wash your _____ before eating.", "hands", "Tinetappudu chethulu kadukkondi.", "Chethulu ante 'hands'.", ["legs", "face", "hands"]),
        ("Switch off the _____ when leaving.", "lights", "Bayataki velleppudu light aapandi.", "Energy save cheyyadaniki lights off cheyyali.", ["fan", "lights", "door"]),
        ("I use a _____ to write.", "pen", "Nenu rayadaniki idi vadutanu.", "Rayadaniki 'pen' vadutham.", ["pen", "phone", "key"]),
        ("Put your clothes in the _____.", "cupboard", "Battalu indulo pettu.", "Battalu pette place ni 'cupboard' antaru.", ["table", "cupboard", "floor"]),
        ("I sleep on a _____.", "bed", "Nenu dini meeda padukuntanu.", "Furniture ni 'bed' antaru.", ["chair", "table", "bed"]),
        ("Cook food in the _____.", "kitchen", "Vanta ikkada chestharu.", "Vanta gadini 'kitchen' antaru.", ["bedroom", "kitchen", "bathroom"]),
        ("Watch _____ in the evening.", "television", "Sayantram nenu idi chusthanu.", "Entertainment device ni 'television' antaru.", ["television", "radio", "book"]),
        ("Drive your _____ safely.", "car", "Nee bandini jagrathaga nadupu.", "Vehicle ni 'car' or bike antam.", ["car", "house", "tree"]),
        ("Wear your _____ before going out.", "shoes", "Bayataki velle mundu shoes vesuko.", "Footwear ni 'shoes' antam.", ["hat", "shoes", "gloves"]),
        ("I use a _____ to call my friend.", "mobile", "Friend ki call cheyyadaniki idi vadutham.", "Phone ni 'mobile' antam.", ["mobile", "book", "pen"]),
        ("The _____ is shining brightly.", "sun", "Akasham lo bright ga velugutundi.", "Daytime light source 'sun'.", ["moon", "sun", "star"]),
        ("I am feeling _____ today.", "happy", "Nenu eeroju santoshamga unnanu.", "Positive feeling ni 'happy' antam.", ["happy", "sad", "angry"]),
        ("Take a _____ every morning.", "bath", "Roju udayam snanam cheyyali.", "Snanam ni 'bath' antaru.", ["bath", "meal", "walk"]),
        ("Keep your surroundings _____.", "clean", "Chuttu pakkala pranthanni subhranga unchandi.", "Subhranga undadanni 'clean' antaru.", ["dirty", "clean", "messy"]),
    ]

    # 5. FAMILY VOCABULARY (20)
    family_exercises = [
        ("My father's brother is my _____.", "uncle", "Nanna tammudu/anna.", "Tandri tammudini English lo 'uncle' antam.", ["uncle", "aunt", "cousin"]),
        ("My mother's sister is my _____.", "aunt", "Amma akka/tellelu.", "Talli sodarini 'aunt' antam.", ["uncle", "aunt", "sister"]),
        ("I have one elder _____.", "brother", "Naku okka anna unnadu.", "Maga sibling ni 'brother' antam.", ["brother", "sister", "mother"]),
        ("My father and mother are my _____.", "parents", "Nanna mariyu amma ni kalipi emantaru?", "Parents ante tallidandrulu.", ["parents", "grandparents", "siblings"]),
        ("My son's sister is my _____.", "daughter", "Koduku akka/tellelu naku emavutundi?", "Koduku sister ni 'daughter' antam.", ["son", "daughter", "niece"]),
        ("My sister's son is my _____.", "nephew", "Akka koduku.", "Sodari kodukuni 'nephew' antam.", ["nephew", "niece", "cousin"]),
        ("My sister's daughter is my _____.", "niece", "Akka kuthuru.", "Sodari kuthuruni 'niece' antam.", ["nephew", "niece", "cousin"]),
        ("My father's father is my _____.", "grandfather", "Nanna nanna.", "Thatha ni 'grandfather' antam.", ["grandfather", "grandmother", "uncle"]),
        ("My mother's mother is my _____.", "grandmother", "Amma amma.", "Amma amma ni 'grandmother' antam.", ["grandfather", "grandmother", "aunt"]),
        ("My uncle's child is my _____.", "cousin", "Babai/Pinni pillalu.", "Uncle/Aunt pillalani 'cousin' antam.", ["cousin", "brother", "sister"]),
        ("I live in a joint _____.", "family", "Memu kalisi untunnam.", "Family motham kalisi undadanni 'joint family' antaru.", ["house", "family", "village"]),
        ("My _____ is a housewife.", "mother", "Maa amma housewife.", "Amma ni 'mother' antaru.", ["father", "mother", "brother"]),
        ("We are _____ brothers and sisters.", "four", "Memu mugguram brothers, okka sister.", "Count chesi cheppali.", ["one", "four", "many"]),
        ("My brother's wife is my _____.", "sister-in-law", "Anna pellam.", "Vadinani 'sister-in-law' antam.", ["sister-in-law", "sister", "aunt"]),
        ("My sister's husband is my _____.", "brother-in-law", "Akka bhartha.", "Bava ni 'brother-in-law' antam.", ["brother-in-law", "brother", "uncle"]),
        ("My parents love me _____.", "very much", "Maa parents nannu chala premistaru.", "Chala ekkuva ani cheppadaniki 'very much' vadutham.", ["too", "very much", "so"]),
        ("I respect my _____.", "elders", "Nenu peddalani gouravistanu.", "Peddalani 'elders' antaru.", ["friends", "elders", "kids"]),
        ("We celebrate festivals with our _____.", "relatives", "Pandugalu memu bandhuvulatho chesukuntam.", "Bandhuvulani 'relatives' antaru.", ["relatives", "strangers", "teachers"]),
        ("My _____ is the head of the family.", "grandfather", "Maa thatha family head.", "Family lo pedda vyakthi 'grandfather'.", ["father", "grandfather", "son"]),
        ("I have a small _____.", "family", "Nadi chinna kutumbam.", "Chinna group of relatives 'family'.", ["family", "house", "car"]),
    ]

    add_exercises('alphabets', alphabets_exercises)
    add_exercises('phonics', phonics_exercises)
    add_exercises('self-introduction', self_intro_exercises)
    add_exercises('daily-words', daily_words_exercises)
    add_exercises('family-vocabulary', family_exercises)

if __name__ == "__main__":
    main()
