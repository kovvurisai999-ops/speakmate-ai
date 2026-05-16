import os
import django
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

examples_data = [
    {"en": "The book is on the table.", "te": "పుస్తకం టేబుల్ మీద ఉంది.", "explanation": "'on' is used to indicate surface."},
    {"en": "He is in the room.", "te": "అతను గదిలో ఉన్నాడు.", "explanation": "'in' is used for an enclosed space."},
    {"en": "She is waiting at the bus stop.", "te": "ఆమె బస్టాప్ వద్ద వేచి ఉంది.", "explanation": "'at' is used for a specific point or location."},
    {"en": "The picture is hanging over the sofa.", "te": "చిత్రం సోఫా పైన వేలాడుతోంది.", "explanation": "'over' means above and not touching."},
    {"en": "The cat is hiding under the bed.", "te": "పిల్లి మంచం కింద దాక్కుంది.", "explanation": "'under' means below something."},
    {"en": "They walked along the river.", "te": "వారు నది వెంబడి నడిచారు.", "explanation": "'along' means following the line of something."},
    {"en": "She walked across the street.", "te": "ఆమె వీధికి అడ్డంగా నడిచింది.", "explanation": "'across' means from one side to the other."},
    {"en": "He drove through the tunnel.", "te": "అతను సొరంగం గుండా నడిపాడు.", "explanation": "'through' means going inside and coming out the other side."},
    {"en": "The plane flew above the clouds.", "te": "విమానం మేఘాల పైన ఎగిరింది.", "explanation": "'above' is used for a higher level."},
    {"en": "There is a park near my house.", "te": "నా ఇంటికి సమీపంలో ఒక పార్క్ ఉంది.", "explanation": "'near' means close to."},
    {"en": "The school is next to the bank.", "te": "పాఠశాల బ్యాంకు పక్కన ఉంది.", "explanation": "'next to' means immediately beside."},
    {"en": "He sat between his two friends.", "te": "అతను తన ఇద్దరు స్నేహితుల మధ్య కూర్చున్నాడు.", "explanation": "'between' is used for two people or things."},
    {"en": "She stood among the crowd.", "te": "ఆమె జనాల మధ్య నిలబడింది.", "explanation": "'among' is used for more than two people or things."},
    {"en": "I will meet you at 5 PM.", "te": "నేను మిమ్మల్ని సాయంత్రం 5 గంటలకు కలుస్తాను.", "explanation": "'at' is used for specific time."},
    {"en": "My birthday is in June.", "te": "నా పుట్టినరోజు జూన్‌లో ఉంది.", "explanation": "'in' is used for months and years."},
    {"en": "We do not work on Sundays.", "te": "మేము ఆదివారాల్లో పని చేయము.", "explanation": "'on' is used for days of the week."},
    {"en": "He has been working since morning.", "te": "అతను ఉదయం నుండి పని చేస్తున్నాడు.", "explanation": "'since' indicates a specific starting point in time."},
    {"en": "I have known him for ten years.", "te": "నాకు అతను పదేళ్లుగా తెలుసు.", "explanation": "'for' indicates a duration of time."},
    {"en": "The train leaves by 6 AM.", "te": "రైలు ఉదయం 6 గంటలకల్లా బయలుదేరుతుంది.", "explanation": "'by' means not later than."},
    {"en": "She will return within an hour.", "te": "ఆమె ఒక గంటలోపు తిరిగి వస్తుంది.", "explanation": "'within' means inside a time limit."},
    {"en": "He cut the apple with a knife.", "te": "అతను కత్తితో ఆపిల్‌ను కోశాడు.", "explanation": "'with' is used for tools or instruments."},
    {"en": "This book is written by Shakespeare.", "te": "ఈ పుస్తకం షేక్స్పియర్ చేత వ్రాయబడింది.", "explanation": "'by' is used for the doer of an action."},
    {"en": "He goes to school by bus.", "te": "అతను బస్సులో పాఠశాలకు వెళ్తాడు.", "explanation": "'by' is used for modes of transport."},
    {"en": "She is suffering from fever.", "te": "ఆమె జ్వరంతో బాధపడుతోంది.", "explanation": "'from' indicates the cause or origin."},
    {"en": "The ring is made of gold.", "te": "ఉంగరం బంగారంతో తయారు చేయబడింది.", "explanation": "'of' indicates material."},
    {"en": "He is good at math.", "te": "అతను గణితంలో మంచివాడు.", "explanation": "'at' is used with adjectives to show ability."},
    {"en": "She is interested in music.", "te": "ఆమెకు సంగీతంపై ఆసక్తి ఉంది.", "explanation": "'in' is used with interested."},
    {"en": "I am fond of chocolates.", "te": "నాకు చాక్లెట్లు అంటే ఇష్టం.", "explanation": "'of' is used with fond."},
    {"en": "He is afraid of dogs.", "te": "అతనికి కుక్కలంటే భయం.", "explanation": "'of' is used with afraid."},
    {"en": "We are proud of you.", "te": "మేము నిన్ను చూసి గర్విస్తున్నాము.", "explanation": "'of' is used with proud."},
    {"en": "Please listen to me.", "te": "దయచేసి నా మాట వినండి.", "explanation": "'to' is used with listen."},
    {"en": "He depends on his parents.", "te": "అతను తన తల్లిదండ్రులపై ఆధారపడతాడు.", "explanation": "'on' is used with depend."},
    {"en": "I agree with you.", "te": "నేను మీతో ఏకీభవిస్తున్నాను.", "explanation": "'with' is used with agree for people."},
    {"en": "He apologized for his mistake.", "te": "తన తప్పుకు అతను క్షమాపణలు చెప్పాడు.", "explanation": "'for' is used with apologize for an action."},
    {"en": "She belongs to a rich family.", "te": "ఆమె ధనిక కుటుంబానికి చెందినది.", "explanation": "'to' is used with belong."},
    {"en": "The cat jumped off the wall.", "te": "పిల్లి గోడ మీది నుండి దూకింది.", "explanation": "'off' means away from a surface."},
    {"en": "Put the books into the bag.", "te": "పుస్తకాలను బ్యాగ్‌లోకి పెట్టు.", "explanation": "'into' shows movement inside something."},
    {"en": "Take the books out of the bag.", "te": "బ్యాగ్ నుండి పుస్తకాలను బయటకు తీయి.", "explanation": "'out of' shows movement outside."},
    {"en": "He walked towards the door.", "te": "అతను తలుపు వైపు నడిచాడు.", "explanation": "'towards' indicates direction."},
    {"en": "We walked around the lake.", "te": "మేము సరస్సు చుట్టూ నడిచాము.", "explanation": "'around' means in a circle or surrounding."},
    {"en": "The temperature is below zero.", "te": "ఉష్ణోగ్రత సున్నా కంటే తక్కువగా ఉంది.", "explanation": "'below' indicates a lower level."},
    {"en": "They sat opposite each other.", "te": "వారు ఒకరికొకరు ఎదురుగా కూర్చున్నారు.", "explanation": "'opposite' means facing each other."},
    {"en": "I will wait until 5 PM.", "te": "నేను సాయంత్రం 5 గంటల వరకు వేచి ఉంటాను.", "explanation": "'until' indicates up to a certain time."},
    {"en": "He walked past the hospital.", "te": "అతను ఆసుపత్రి దాటి నడిచాడు.", "explanation": "'past' means further than a place."},
    {"en": "The boy fell down the stairs.", "te": "అబ్బాయి మెట్ల మీది నుండి కిందపడ్డాడు.", "explanation": "'down' indicates movement to a lower position."},
    {"en": "He climbed up the tree.", "te": "అతను చెట్టు ఎక్కాడు.", "explanation": "'up' indicates movement to a higher position."},
    {"en": "They marched against the enemy.", "te": "వారు శత్రువుపై దండెత్తారు.", "explanation": "'against' means in opposition to."},
    {"en": "Besides being a doctor, he is a writer.", "te": "డాక్టర్ కావడమే కాకుండా, అతను ఒక రచయిత కూడా.", "explanation": "'besides' means in addition to."},
    {"en": "Come and sit beside me.", "te": "వచ్చి నా పక్కన కూర్చో.", "explanation": "'beside' means next to."},
    {"en": "Everyone attended the party except John.", "te": "జాన్ మినహా అందరూ పార్టీకి హాజరయ్యారు.", "explanation": "'except' means excluding."}
]

blanks_data = [
    {"question": "The keys are ___ the table.", "correct_answer": "on", "telugu_meaning": "తాళాలు టేబుల్ మీద ఉన్నాయి.", "explanation": "Used for surface.", "options": ["in", "on", "at", "under"]},
    {"question": "She is waiting ___ the bus stop.", "correct_answer": "at", "telugu_meaning": "ఆమె బస్టాప్ వద్ద వేచి ఉంది.", "explanation": "Used for a specific point.", "options": ["in", "on", "at", "over"]},
    {"question": "The fish is swimming ___ the water.", "correct_answer": "in", "telugu_meaning": "చేప నీటిలో ఈదుతోంది.", "explanation": "Used for an enclosed area/substance.", "options": ["in", "on", "at", "with"]},
    {"question": "The cat is hiding ___ the sofa.", "correct_answer": "under", "telugu_meaning": "పిల్లి సోఫా కింద దాక్కుంది.", "explanation": "Below a physical object.", "options": ["over", "above", "under", "in"]},
    {"question": "The plane flew ___ the mountains.", "correct_answer": "over", "telugu_meaning": "విమానం పర్వతాల పైనుండి ఎగిరింది.", "explanation": "Movement above something without touching.", "options": ["under", "below", "over", "at"]},
    {"question": "I will see you ___ Monday.", "correct_answer": "on", "telugu_meaning": "నేను నిన్ను సోమవారం కలుస్తాను.", "explanation": "Days of the week use 'on'.", "options": ["in", "on", "at", "by"]},
    {"question": "Her birthday is ___ August.", "correct_answer": "in", "telugu_meaning": "ఆమె పుట్టినరోజు ఆగస్టులో.", "explanation": "Months use 'in'.", "options": ["in", "on", "at", "for"]},
    {"question": "The movie starts ___ 6 PM.", "correct_answer": "at", "telugu_meaning": "సినిమా సాయంత్రం 6 గంటలకు ప్రారంభమవుతుంది.", "explanation": "Specific time uses 'at'.", "options": ["in", "on", "at", "by"]},
    {"question": "We have been living here ___ 2010.", "correct_answer": "since", "telugu_meaning": "మేము 2010 నుండి ఇక్కడ నివసిస్తున్నాము.", "explanation": "Specific starting point in time.", "options": ["for", "since", "from", "in"]},
    {"question": "They have been waiting ___ three hours.", "correct_answer": "for", "telugu_meaning": "వారు మూడు గంటలుగా ఎదురుచూస్తున్నారు.", "explanation": "Duration of time uses 'for'.", "options": ["for", "since", "from", "in"]},
    {"question": "He cut the cake ___ a knife.", "correct_answer": "with", "telugu_meaning": "అతను కత్తితో కేక్ కట్ చేశాడు.", "explanation": "Instrument or tool.", "options": ["by", "with", "from", "in"]},
    {"question": "The letter was written ___ Mary.", "correct_answer": "by", "telugu_meaning": "ఉత్తరం మేరీ చేత రాయబడింది.", "explanation": "Doer of an action.", "options": ["by", "with", "from", "of"]},
    {"question": "She goes to work ___ car.", "correct_answer": "by", "telugu_meaning": "ఆమె కారులో పనికి వెళ్తుంది.", "explanation": "Mode of transportation.", "options": ["in", "on", "by", "with"]},
    {"question": "He died ___ cancer.", "correct_answer": "of", "telugu_meaning": "అతను క్యాన్సర్‌తో మరణించాడు.", "explanation": "Cause of death from a disease.", "options": ["from", "of", "with", "by"]},
    {"question": "She is suffering ___ a bad cold.", "correct_answer": "from", "telugu_meaning": "ఆమె తీవ్రమైన జలుబుతో బాధపడుతోంది.", "explanation": "Suffering is followed by 'from'.", "options": ["from", "of", "with", "by"]},
    {"question": "I am good ___ playing chess.", "correct_answer": "at", "telugu_meaning": "నేను చదరంగం ఆడటంలో మంచివాడిని.", "explanation": "'Good at' is a fixed prepositional phrase.", "options": ["in", "on", "at", "with"]},
    {"question": "He is interested ___ politics.", "correct_answer": "in", "telugu_meaning": "అతనికి రాజకీయాలంటే ఆసక్తి.", "explanation": "'Interested in' is a fixed phrase.", "options": ["in", "on", "at", "with"]},
    {"question": "She is fond ___ reading.", "correct_answer": "of", "telugu_meaning": "ఆమెకు చదవడం అంటే ఇష్టం.", "explanation": "'Fond of' is a fixed phrase.", "options": ["of", "off", "from", "with"]},
    {"question": "Are you afraid ___ spiders?", "correct_answer": "of", "telugu_meaning": "నీకు సాలీడులంటే భయమా?", "explanation": "'Afraid of' is a fixed phrase.", "options": ["of", "from", "with", "by"]},
    {"question": "Please listen ___ your parents.", "correct_answer": "to", "telugu_meaning": "దయచేసి మీ తల్లిదండ్రుల మాట వినండి.", "explanation": "'Listen to' is a fixed phrase.", "options": ["for", "to", "at", "with"]},
    {"question": "He depends ___ his salary.", "correct_answer": "on", "telugu_meaning": "అతను తన జీతం మీద ఆధారపడతాడు.", "explanation": "'Depend on' is a fixed phrase.", "options": ["in", "on", "at", "with"]},
    {"question": "I agree ___ you completely.", "correct_answer": "with", "telugu_meaning": "నేను మీతో పూర్తిగా ఏకీభవిస్తున్నాను.", "explanation": "Agree 'with' a person.", "options": ["to", "with", "on", "for"]},
    {"question": "He apologized ___ his rude behavior.", "correct_answer": "for", "telugu_meaning": "తన మొరటు ప్రవర్తనకు అతను క్షమాపణలు చెప్పాడు.", "explanation": "Apologize 'for' an action.", "options": ["to", "with", "for", "on"]},
    {"question": "This bag belongs ___ me.", "correct_answer": "to", "telugu_meaning": "ఈ బ్యాగ్ నాది (నాకు చెందినది).", "explanation": "'Belong to' is a fixed phrase.", "options": ["to", "for", "with", "of"]},
    {"question": "The boy jumped ___ the wall.", "correct_answer": "off", "telugu_meaning": "బాలుడు గోడ మీద నుండి దూకాడు.", "explanation": "Movement away from a surface.", "options": ["of", "off", "from", "out"]},
    {"question": "Pour the milk ___ the glass.", "correct_answer": "into", "telugu_meaning": "గ్లాసులో పాలు పోయండి.", "explanation": "Movement from outside to inside.", "options": ["in", "into", "on", "onto"]},
    {"question": "Take your phone ___ of your pocket.", "correct_answer": "out", "telugu_meaning": "మీ జేబులో నుండి మీ ఫోన్‌ని తీయండి.", "explanation": "Movement from inside to outside ('out of').", "options": ["out", "off", "from", "away"]},
    {"question": "We walked ___ the beach.", "correct_answer": "along", "telugu_meaning": "మేము బీచ్ వెంబడి నడిచాము.", "explanation": "Movement parallel to a line.", "options": ["along", "across", "through", "over"]},
    {"question": "Be careful when walking ___ the street.", "correct_answer": "across", "telugu_meaning": "వీధి దాటుతున్నప్పుడు జాగ్రత్తగా ఉండండి.", "explanation": "From one side to the other.", "options": ["along", "across", "through", "over"]},
    {"question": "The train went ___ the tunnel.", "correct_answer": "through", "telugu_meaning": "రైలు సొరంగం గుండా వెళ్ళింది.", "explanation": "Entering one side and exiting the other.", "options": ["along", "across", "through", "over"]}
]

speaking_data = [
    {"question": "The pen is on the table.", "telugu_meaning": "పెన్ టేబుల్ మీద ఉంది.", "explanation": "Emphasize 'on' for surface."},
    {"question": "She is in the kitchen.", "telugu_meaning": "ఆమె వంటగదిలో ఉంది.", "explanation": "Emphasize 'in' for enclosed space."},
    {"question": "I am at the bus stop.", "telugu_meaning": "నేను బస్టాప్ వద్ద ఉన్నాను.", "explanation": "Emphasize 'at' for a specific point."},
    {"question": "The cat is under the bed.", "telugu_meaning": "పిల్లి మంచం కింద ఉంది.", "explanation": "Focus on pronouncing 'under'."},
    {"question": "The bird flew over the tree.", "telugu_meaning": "పక్షి చెట్టు పైనుండి ఎగిరింది.", "explanation": "Focus on pronouncing 'over'."},
    {"question": "Let's meet on Sunday.", "telugu_meaning": "మనం ఆదివారం కలుద్దాం.", "explanation": "Notice the use of 'on' before days."},
    {"question": "I was born in October.", "telugu_meaning": "నేను అక్టోబర్‌లో జన్మించాను.", "explanation": "Notice the use of 'in' before months."},
    {"question": "The train leaves at 8 PM.", "telugu_meaning": "రైలు రాత్రి 8 గంటలకు బయలుదేరుతుంది.", "explanation": "Notice the use of 'at' before time."},
    {"question": "I have been here since morning.", "telugu_meaning": "నేను ఉదయం నుండి ఇక్కడే ఉన్నాను.", "explanation": "'since' indicates a starting point."},
    {"question": "He studied for three hours.", "telugu_meaning": "అతను మూడు గంటలు చదువుకున్నాడు.", "explanation": "'for' indicates a duration."},
    {"question": "She cut the apple with a knife.", "telugu_meaning": "ఆమె కత్తితో ఆపిల్‌ను కోసింది.", "explanation": "'with' indicates an instrument."},
    {"question": "This picture was painted by him.", "telugu_meaning": "ఈ చిత్రం అతనిచే వేయబడింది.", "explanation": "'by' indicates the doer."},
    {"question": "They travel by train.", "telugu_meaning": "వారు రైలులో ప్రయాణిస్తారు.", "explanation": "'by' is used for transport modes."},
    {"question": "He died of a heart attack.", "telugu_meaning": "అతను గుండెపోటుతో మరణించాడు.", "explanation": "Notice 'of' used with diseases."},
    {"question": "She is suffering from a headache.", "telugu_meaning": "ఆమె తలనొప్పితో బాధపడుతోంది.", "explanation": "Notice 'from' used with suffering."},
    {"question": "I am good at math.", "telugu_meaning": "నేను గణితంలో మంచివాడిని.", "explanation": "Fixed phrase 'good at'."},
    {"question": "He is interested in art.", "telugu_meaning": "అతనికి కళల పట్ల ఆసక్తి ఉంది.", "explanation": "Fixed phrase 'interested in'."},
    {"question": "She is fond of dogs.", "telugu_meaning": "ఆమెకు కుక్కలంటే ఇష్టం.", "explanation": "Fixed phrase 'fond of'."},
    {"question": "Are you afraid of the dark?", "telugu_meaning": "నీకు చీకటి అంటే భయమా?", "explanation": "Fixed phrase 'afraid of'."},
    {"question": "Listen to the teacher.", "telugu_meaning": "ఉపాధ్యాయుడి మాట విను.", "explanation": "Fixed phrase 'listen to'."},
    {"question": "It depends on the weather.", "telugu_meaning": "ఇది వాతావరణంపై ఆధారపడి ఉంటుంది.", "explanation": "Fixed phrase 'depends on'."},
    {"question": "I agree with your plan.", "telugu_meaning": "నేను మీ ప్రణాళికతో ఏకీభవిస్తున్నాను.", "explanation": "Fixed phrase 'agree with'."},
    {"question": "He apologized for the delay.", "telugu_meaning": "ఆలస్యానికి అతను క్షమాపణ చెప్పాడు.", "explanation": "Fixed phrase 'apologized for'."},
    {"question": "This book belongs to me.", "telugu_meaning": "ఈ పుస్తకం నాది.", "explanation": "Fixed phrase 'belongs to'."},
    {"question": "He jumped off the wall.", "telugu_meaning": "అతను గోడ పైనుండి దూకాడు.", "explanation": "Pronounce 'off' clearly."},
    {"question": "She walked into the room.", "telugu_meaning": "ఆమె గదిలోకి నడిచింది.", "explanation": "Focus on 'into'."},
    {"question": "They walked along the road.", "telugu_meaning": "వారు రోడ్డు వెంబడి నడిచారు.", "explanation": "Focus on 'along'."},
    {"question": "We drove through the tunnel.", "telugu_meaning": "మేము సొరంగం గుండా కారు నడిపాము.", "explanation": "Focus on 'through'."},
    {"question": "He walked past the shop.", "telugu_meaning": "అతను దుకాణాన్ని దాటి వెళ్ళాడు.", "explanation": "Focus on 'past'."},
    {"question": "She sat beside her mother.", "telugu_meaning": "ఆమె తన తల్లి పక్కన కూర్చుంది.", "explanation": "Focus on 'beside'."}
]

concept = Concept.objects.filter(name='Prepositions').first()
if concept:
    concept.examples = examples_data
    concept.save()
    
    Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
    Exercise.objects.filter(concept=concept, type='READ_ALOUD').delete()
    
    for item in blanks_data:
        Exercise.objects.create(
            concept=concept,
            type='FILL_BLANK',
            question=item['question'],
            correct_answer=item['correct_answer'],
            explanation=item['explanation'],
            telugu_meaning=item['telugu_meaning'],
            options=item['options']
        )
    for item in speaking_data:
        Exercise.objects.create(
            concept=concept,
            type='READ_ALOUD',
            question=item['question'],
            telugu_meaning=item['telugu_meaning'],
            explanation=item['explanation']
        )
    print("Prepositions completed successfully.")
else:
    print("Concept 'Prepositions' not found.")
