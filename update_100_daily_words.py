import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

def main():
    content = """What are Daily Words?

Daily Words ante: "Manam prati roju life lo use chese common English words."

Examples:
- eat
- water
- school
- mobile
- sleep
- money
- friend

Ivi daily conversations lo ekkuva use avutayi.

Why Daily Words Important?
✅ Spoken English improve avutundi
✅ Fast communication vastundi
✅ Confidence perugutundi
✅ Real-life conversations easy avutayi"""

    rules = """KEY RULES

Rule 1: Word ni sentence lo use cheyyadam nerchukovali.
Example: Water
Sentence: I drink water every morning.

Rule 2: Daily life situations lo practice cheyyali.
Example: Bus
Sentence: I go to college by bus."""

    raw_data = """
1
Word: Water
Sentence: I drink warm water in the morning.
Meaning: Nenu morning lo warm water taguthanu.
Explanation
“drink” → daily action
“in the morning” → time expression
2
Word: Mobile
Sentence: My mobile battery is low.
Meaning: Naa mobile battery takkuva undi.
Explanation
“is” because singular subject
3
Word: Breakfast
Sentence: I had breakfast at 8 AM.
Meaning: Nenu 8 AM ki breakfast chesanu.
Explanation
“had” → past tense
4
Word: Bus
Sentence: The bus arrived late today.
Meaning: Bus eeroju late gaa vachindi.
5
Word: Teacher
Sentence: Our teacher explained the lesson clearly.
Meaning: Maa teacher lesson clear gaa explain chesaru.
6
Word: Money
Sentence: I saved some money this month.
Meaning: Ee month konchem money save chesanu.
7
Word: Market
Sentence: My mother went to the market.
Meaning: Maa amma market ki vellindi.
8
Word: Friend
Sentence: My friend helped me yesterday.
Meaning: Naa friend ninna help chesadu.
9
Word: Laptop
Sentence: I use my laptop for coding practice.
Meaning: Coding practice kosam laptop use chesthanu.
10
Word: Rain
Sentence: It is raining heavily outside.
Meaning: Bayata heavy rain padutundi.
Explanation
Present continuous tense
11
Word: Coffee
Sentence: My father drinks coffee every evening.
Meaning: Maa nanna every evening coffee tagutaru.
12
Word: Book
Sentence: I bought a new English book.
Meaning: Nenu kottha English book konnanu.
13
Word: Shoes
Sentence: These shoes are very comfortable.
Meaning: Ee shoes chala comfortable gaa unnayi.
14
Word: Hospital
Sentence: She works in a hospital.
Meaning: Aame hospital lo work chestundi.
15
Word: Lunch
Sentence: We ate lunch together.
Meaning: Memu kalisi lunch chesam.
16
Word: Internet
Sentence: The internet is very slow today.
Meaning: Internet eeroju chala slow gaa undi.
17
Word: Fan
Sentence: Please switch on the fan.
Meaning: Fan on cheyyandi.
18
Word: Movie
Sentence: We watched a comedy movie last night.
Meaning: Memu comedy movie chusam.
19
Word: Exam
Sentence: My exam starts tomorrow.
Meaning: Naa exam repu start avutundi.
20
Word: Bike
Sentence: He rides his bike carefully.
Meaning: Athanu bike jagrathaga nadustadu.
21
Word: Phone
Sentence: My phone is charging now.
Meaning: Naa phone ippudu charging lo undi.
22
Word: Bag
Sentence: I forgot my bag at college.
Meaning: Naa bag college lo marchipoyanu.
23
Word: Milk
Sentence: The milk is hot.
Meaning: Paalu vediga unnayi.
24
Word: Door
Sentence: Please close the door.
Meaning: Door close cheyyandi.
25
Word: Computer
Sentence: My computer stopped working.
Meaning: Naa computer work cheyyadam aapesindi.
26
Word: Road
Sentence: The road is very crowded.
Meaning: Road chala crowd gaa undi.
27
Word: Rice
Sentence: My mother cooked rice.
Meaning: Maa amma rice cook chesindi.
28
Word: Pen
Sentence: Can I borrow your pen?
Meaning: Nee pen konchem use cheyacha?
29
Word: Chair
Sentence: This chair is broken.
Meaning: Ee chair damage ayindi.
30
Word: Garden
Sentence: There are many flowers in the garden.
Meaning: Garden lo chala flowers unnayi.
31
Word: Clothes
Sentence: She washed the clothes yesterday.
Meaning: Aame battalu utikindi.
32
Word: Train
Sentence: The train left early.
Meaning: Train tondaraga vellipoyindi.
33
Word: Password
Sentence: Don't share your password.
Meaning: Nee password share cheyyaku.
34
Word: Office
Sentence: My brother works in an IT office.
Meaning: Maa anna IT office lo work chestadu.
35
Word: Pillow
Sentence: This pillow is very soft.
Meaning: Ee pillow chala soft gaa undi.
36
Word: Clock
Sentence: The clock shows 9 PM.
Meaning: Clock 9 PM chupistundi.
37
Word: Soap
Sentence: Please buy soap from the shop.
Meaning: Shop nunchi soap konandi.
38
Word: Fruits
Sentence: Fruits are good for health.
Meaning: Fruits health ki manchivi.
39
Word: Key
Sentence: I lost my bike key.
Meaning: Naa bike key pogottukunnanu.
40
Word: Tea
Sentence: My grandmother makes tasty tea.
Meaning: Maa ammamma tasty tea chestundi.
41
Word: Homework
Sentence: I completed my homework.
Meaning: Naa homework complete chesanu.
42
Word: Window
Sentence: Open the window please.
Meaning: Window open cheyyandi.
43
Word: Electricity
Sentence: There is no electricity now.
Meaning: Ippudu current ledu.
44
Word: Medicine
Sentence: Take your medicine on time.
Meaning: Time ki medicine teesuko.
45
Word: Hotel
Sentence: We stayed in a good hotel.
Meaning: Memu manchi hotel lo unnam.
46
Word: Water Bottle
Sentence: Carry a water bottle with you.
Meaning: Water bottle meetho teesukellandi.
47
Word: Student
Sentence: Every student should practice English daily.
Meaning: Prati student daily English practice cheyyali.
48
Word: Salary
Sentence: He received his salary yesterday.
Meaning: Athanu ninna salary pondadu.
49
Word: Helmet
Sentence: Always wear a helmet while driving.
Meaning: Driving chestappudu helmet pettukondi.
50
Word: Weather
Sentence: The weather is pleasant today.
Meaning: Eeroju weather bagundi.
51
Word: Fan
Sentence: The fan is making noise.
Meaning: Fan sound chestundi.
52
Word: Ticket
Sentence: I booked the movie tickets online.
Meaning: Movie tickets online lo book chesanu.
53
Word: Kitchen
Sentence: My mother is cooking in the kitchen.
Meaning: Maa amma kitchen lo cooking chestundi.
54
Word: Mobile Charger
Sentence: Where is my mobile charger?
Meaning: Naa mobile charger ekkada undi?
55
Word: Temple
Sentence: We visited the temple yesterday.
Meaning: Memu temple ki vellam.
56
Word: Pillow
Sentence: I need another pillow.
Meaning: Naku inko pillow kavali.
57
Word: Mirror
Sentence: She looked at herself in the mirror.
Meaning: Aame mirror lo chusukundi.
58
Word: Shirt
Sentence: He bought a blue shirt.
Meaning: Athanu blue shirt konnadu.
59
Word: Juice
Sentence: I drank orange juice.
Meaning: Nenu orange juice taganu.
60
Word: Driver
Sentence: The driver stopped the car suddenly.
Meaning: Driver car sudden gaa aapadu.
61
Word: Table
Sentence: The books are on the table.
Meaning: Books table meeda unnayi.
62
Word: Grocery
Sentence: We bought groceries this evening.
Meaning: Eeroju groceries konnam.
63
Word: Light
Sentence: Please turn off the light.
Meaning: Light off cheyyandi.
64
Word: Medicine
Sentence: This medicine works quickly.
Meaning: Ee medicine fast gaa work chestundi.
65
Word: Raincoat
Sentence: Carry a raincoat during rainy season.
Meaning: Rainy season lo raincoat teesukellandi.
66
Word: Newspaper
Sentence: My grandfather reads the newspaper daily.
Meaning: Maa thatha daily newspaper chadutaaru.
67
Word: Remote
Sentence: I can't find the TV remote.
Meaning: TV remote dorakatledu.
68
Word: Ice Cream
Sentence: The children are eating ice cream.
Meaning: Pillalu ice cream tintunnaru.
69
Word: Bus Stop
Sentence: I waited at the bus stop.
Meaning: Bus stop daggara wait chesanu.
70
Word: Fan
Sentence: The ceiling fan rotates slowly.
Meaning: Ceiling fan slow gaa tirugutundi.
71
Word: Vegetable
Sentence: Fresh vegetables are healthy.
Meaning: Fresh vegetables health ki manchivi.
72
Word: Notebook
Sentence: She writes notes in her notebook.
Meaning: Aame notebook lo notes rasthundi.
73
Word: Village
Sentence: My grandparents live in a village.
Meaning: Maa grandparents village lo untaru.
74
Word: Salary
Sentence: She saves part of her salary.
Meaning: Aame salary lo kontha save chestundi.
75
Word: Fan
Sentence: The fan stopped suddenly.
Meaning: Fan sudden gaa aagipoyindi.
76
Word: Wallet
Sentence: I forgot my wallet at home.
Meaning: Naa wallet intlo marchipoyanu.
77
Word: Camera
Sentence: He bought a new camera.
Meaning: Athanu kottha camera konnadu.
78
Word: Station
Sentence: The train reached the station late.
Meaning: Train station ki late gaa vachindi.
79
Word: AC
Sentence: The AC is not working properly.
Meaning: AC proper gaa work cheyyatledu.
80
Word: Fruits
Sentence: She cut the fruits carefully.
Meaning: Aame fruits cut chesindi.
81
Word: Dinner
Sentence: We had dinner at a restaurant.
Meaning: Memu restaurant lo dinner chesam.
82
Word: Clock
Sentence: The wall clock is expensive.
Meaning: Wall clock costly gaa undi.
83
Word: School
Sentence: The children went to school early.
Meaning: Pillalu school ki tondaraga vellaru.
84
Word: Mobile Data
Sentence: My mobile data is over.
Meaning: Naa mobile data aipoyindi.
85
Word: Tap
Sentence: The tap is leaking water.
Meaning: Tap nunchi water leak avutundi.
86
Word: Bed
Sentence: The baby is sleeping on the bed.
Meaning: Baby bed meeda padukundi.
87
Word: Shoes
Sentence: His shoes are dirty.
Meaning: Athani shoes dirty gaa unnayi.
88
Word: Project
Sentence: I submitted my project yesterday.
Meaning: Nenu naa project submit chesanu.
89
Word: Lift
Sentence: The lift is under repair.
Meaning: Lift repair lo undi.
90
Word: Shop
Sentence: The shop opens at 9 AM.
Meaning: Shop 9 AM ki open avutundi.
91
Word: Rice Bag
Sentence: The rice bag is heavy.
Meaning: Rice bag baruvuga undi.
92
Word: Employee
Sentence: Every employee attended the meeting.
Meaning: Prati employee meeting ki vacharu.
93
Word: Earphones
Sentence: My earphones are missing.
Meaning: Naa earphones kanapadatledu.
94
Word: Garden
Sentence: Children are playing in the garden.
Meaning: Pillalu garden lo aadutunnaru.
95
Word: Blackboard
Sentence: The teacher wrote on the blackboard.
Meaning: Teacher blackboard meeda rasaru.
96
Word: Fan Switch
Sentence: Turn on the fan switch.
Meaning: Fan switch on cheyyi.
97
Word: Breakfast Box
Sentence: I packed my breakfast box.
Meaning: Naa breakfast box pack chesanu.
98
Word: Parking
Sentence: There is no parking space here.
Meaning: Ikkada parking place ledu.
99
Word: Dustbin
Sentence: Throw the waste in the dustbin.
Meaning: Waste dustbin lo veyyi.
100
Word: Watch
Sentence: My watch stopped working yesterday.
Meaning: Naa watch ninna work cheyyadam aapesindi.
"""

    examples = []
    lines = [line.strip() for line in raw_data.strip().split('\n') if line.strip()]
    
    current_item = {}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.isdigit():
            if current_item:
                examples.append(current_item)
            current_item = {"word": "", "en": "", "te": "", "sound": "Practice", "explanation": ""}
            i += 1
            if i < len(lines) and lines[i].startswith("Word:"):
                current_item["word"] = lines[i].replace("Word:", "").strip()
                i += 1
            if i < len(lines) and lines[i].startswith("Sentence:"):
                current_item["en"] = lines[i].replace("Sentence:", "").strip()
                i += 1
            if i < len(lines) and lines[i].startswith("Meaning:"):
                current_item["te"] = lines[i].replace("Meaning:", "").strip()
                i += 1
        else:
            if current_item:
                if line == "Explanation":
                    explanation_lines = []
                    i += 1
                    while i < len(lines) and not lines[i].isdigit():
                        explanation_lines.append(lines[i])
                        i += 1
                    current_item["explanation"] = " ".join(explanation_lines)
                    continue
            i += 1

    if current_item:
        examples.append(current_item)

    print(f"Parsed {len(examples)} examples.")

    level1, _ = Level.objects.get_or_create(number=1, defaults={'title': 'Basics', 'description': 'Learn basics'})

    daily_words, created = Concept.objects.get_or_create(
        slug='daily-words',
        defaults={
            'name': 'Daily Words',
            'level': level1,
            'formula': 'Word + Context'
        }
    )

    daily_words.content = content
    daily_words.grammar_rules = rules
    daily_words.examples = examples
    daily_words.save()
    
    print(f"Database updated successfully! Concept {'created' if created else 'updated'} with 100 examples.")

if __name__ == "__main__":
    main()
