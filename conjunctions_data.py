import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

examples_data = [
    {"en": "I like apples and bananas.", "te": "నాకు ఆపిల్స్ మరియు అరటిపండ్లు ఇష్టం.", "explanation": "'and' connects two similar ideas or items."},
    {"en": "He is poor but honest.", "te": "అతను పేదవాడు కానీ నిజాయితీపరుడు.", "explanation": "'but' connects contrasting ideas."},
    {"en": "You can have tea or coffee.", "te": "మీరు టీ లేదా కాఫీ తీసుకోవచ్చు.", "explanation": "'or' presents an alternative."},
    {"en": "I was tired, so I went to sleep.", "te": "నేను అలసిపోయాను, కాబట్టి నేను నిద్రపోయాను.", "explanation": "'so' indicates a result or consequence."},
    {"en": "She passed because she studied hard.", "te": "ఆమె కష్టపడి చదివినందున పాస్ అయింది.", "explanation": "'because' gives a reason."},
    {"en": "Although it was raining, we went out.", "te": "వర్షం పడుతున్నప్పటికీ, మేము బయటకు వెళ్ళాము.", "explanation": "'although' shows a contrast or concession."},
    {"en": "I will wait until you come.", "te": "నువ్వు వచ్చే వరకు నేను వేచి ఉంటాను.", "explanation": "'until' indicates a time limit."},
    {"en": "If you work hard, you will succeed.", "te": "నువ్వు కష్టపడి పనిచేస్తే, విజయం సాధిస్తావు.", "explanation": "'if' introduces a condition."},
    {"en": "Unless you hurry, you will miss the train.", "te": "నువ్వు తొందరపడకపోతే, రైలు మిస్ అవుతావు.", "explanation": "'unless' means 'if not'."},
    {"en": "He is as tall as his brother.", "te": "అతను తన సోదరుడి అంత పొడవుగా ఉన్నాడు.", "explanation": "'as...as' is used for comparison."},
    {"en": "Both Ram and Shyam are my friends.", "te": "రామ్ మరియు శ్యామ్ ఇద్దరూ నా స్నేహితులు.", "explanation": "'both...and' connects two subjects."},
    {"en": "Either you or your brother must go.", "te": "నువ్వు లేదా నీ తమ్ముడు ఖచ్చితంగా వెళ్లాలి.", "explanation": "'either...or' gives a choice between two."},
    {"en": "Neither Ram nor Shyam came.", "te": "రామ్ రాలేదు, శ్యామ్ కూడా రాలేదు.", "explanation": "'neither...nor' negates both options."},
    {"en": "He not only sings but also dances.", "te": "అతను పాడటమే కాకుండా డాన్స్ కూడా చేస్తాడు.", "explanation": "'not only...but also' adds emphasis to two actions."},
    {"en": "I didn't go to school since I was ill.", "te": "నేను అనారోగ్యంతో ఉన్నందున పాఠశాలకు వెళ్లలేదు.", "explanation": "'since' can be used to give a reason, like 'because'."},
    {"en": "Wait here while I make a phone call.", "te": "నేను ఫోన్ కాల్ చేసేంత వరకు ఇక్కడే వేచి ఉండు.", "explanation": "'while' means at the same time."},
    {"en": "As soon as he arrived, it started raining.", "te": "అతను రాగానే వర్షం మొదలైంది.", "explanation": "'as soon as' means immediately after."},
    {"en": "He is rich, yet he is unhappy.", "te": "అతను ధనవంతుడు, అయినప్పటికీ సంతోషంగా లేడు.", "explanation": "'yet' shows contrast, similar to 'but'."},
    {"en": "I went to the store for I needed milk.", "te": "నాకు పాలు కావాలి కాబట్టి నేను స్టోర్‌కి వెళ్ళాను.", "explanation": "'for' can be used as a conjunction meaning 'because'."},
    {"en": "Whether you like it or not, you have to do it.", "te": "నీకు ఇష్టమున్నా లేకపోయినా, నువ్వు దీన్ని చేయాలి.", "explanation": "'whether...or' expresses two alternatives."},
    {"en": "I am studying hard so that I can pass the exam.", "te": "పరీక్షలో ఉత్తీర్ణత సాధించడానికి నేను కష్టపడి చదువుతున్నాను.", "explanation": "'so that' expresses purpose."},
    {"en": "After we had lunch, we went for a walk.", "te": "మేము భోజనం చేసిన తర్వాత, నడవడానికి వెళ్ళాము.", "explanation": "'after' indicates a later time."},
    {"en": "Before you leave, please close the door.", "te": "నువ్వు వెళ్లే ముందు, దయచేసి తలుపు మూసివేయి.", "explanation": "'before' indicates an earlier time."},
    {"en": "I don't know where he lives.", "te": "అతను ఎక్కడ నివసిస్తున్నాడో నాకు తెలియదు.", "explanation": "'where' connects dependent clauses of place."},
    {"en": "I remember when we first met.", "te": "మనం మొదటిసారి కలిసినప్పుడు నాకు గుర్తుంది.", "explanation": "'when' connects dependent clauses of time."},
    {"en": "He ran away lest he should be caught.", "te": "పట్టుబడతానేమో అని భయంతో అతను పారిపోయాడు.", "explanation": "'lest' means 'for fear that' or 'so that...not'."},
    {"en": "As long as you are here, you are safe.", "te": "నువ్వు ఇక్కడ ఉన్నంత కాలం సురక్షితంగా ఉంటావు.", "explanation": "'as long as' means provided that."},
    {"en": "Provided that it doesn't rain, we will play.", "te": "వర్షం పడకపోతే, మేము ఆడుకుంటాము.", "explanation": "'provided that' is a conditional conjunction."},
    {"en": "Supposing he doesn't come, what will we do?", "te": "ఒకవేళ అతను రాకపోతే, మనం ఏమి చేస్తాము?", "explanation": "'supposing' introduces a hypothetical condition."},
    {"en": "He acted as if he knew everything.", "te": "అతనికి అన్నీ తెలిసినట్లు ప్రవర్తించాడు.", "explanation": "'as if' expresses how something seems."},
    {"en": "Even if it rains, I will go.", "te": "వర్షం పడినా సరే, నేను వెళ్తాను.", "explanation": "'even if' introduces a condition that won't change the outcome."},
    {"en": "She works hard, whereas her brother is lazy.", "te": "ఆమె కష్టపడి పనిచేస్తుంది, అయితే ఆమె సోదరుడు బద్ధకస్తుడు.", "explanation": "'whereas' shows contrast."},
    {"en": "He looks as though he is sick.", "te": "అతను అనారోగ్యంతో ఉన్నట్లు కనిపిస్తున్నాడు.", "explanation": "'as though' is similar to 'as if'."},
    {"en": "In case you need help, call me.", "te": "మీకు సహాయం అవసరమైతే, నాకు కాల్ చేయండి.", "explanation": "'in case' provides for a possible situation."},
    {"en": "Now that you have passed, you can relax.", "te": "ఇప్పుడు మీరు పాస్ అయ్యారు కాబట్టి, విశ్రాంతి తీసుకోవచ్చు.", "explanation": "'now that' gives a reason based on a new situation."},
    {"en": "I will go wherever you go.", "te": "నువ్వు ఎక్కడికి వెళితే నేను అక్కడికి వస్తాను.", "explanation": "'wherever' means any place that."},
    {"en": "Whenever I see him, he is smiling.", "te": "నేను అతన్ని చూసినప్పుడల్లా నవ్వుతూ ఉంటాడు.", "explanation": "'whenever' means every time that."},
    {"en": "Whoever wants to come, can join us.", "te": "ఎవరు రావాలనుకున్నా మాతో చేరవచ్చు.", "explanation": "'whoever' means any person who."},
    {"en": "Whichever book you choose, it will be good.", "te": "నువ్వు ఏ పుస్తకం ఎంచుకున్నా అది బాగుంటుంది.", "explanation": "'whichever' means any one from a set."},
    {"en": "He talks as much as he eats.", "te": "అతను ఎంత తింటాడో అంత మాట్లాడతాడు.", "explanation": "'as much as' compares quantity."},
    {"en": "I love him even though he is rude.", "te": "అతను మొరటుగా ఉన్నప్పటికీ నేను అతన్ని ప్రేమిస్తున్నాను.", "explanation": "'even though' is a stronger form of 'although'."},
    {"en": "The more you study, the better you get.", "te": "నువ్వు ఎంత ఎక్కువగా చదివితే, అంత మెరుగవుతావు.", "explanation": "'the more...the better' shows correlation."},
    {"en": "No sooner had I arrived than it rained.", "te": "నేను రాగానే వర్షం పడింది.", "explanation": "'no sooner...than' means immediately after."},
    {"en": "Hardly had I slept when the phone rang.", "te": "నేను నిద్రపోయానో లేదో ఫోన్ మోగింది.", "explanation": "'hardly...when' means immediately after."},
    {"en": "Scarcely had we left when he arrived.", "te": "మేము బయలుదేరామో లేదో అతను వచ్చాడు.", "explanation": "'scarcely...when' is similar to hardly when."},
    {"en": "He bought it, seeing that it was cheap.", "te": "ఇది చౌకగా ఉందని చూసి అతను కొన్నాడు.", "explanation": "'seeing that' gives a reason."},
    {"en": "Considering that he is young, he did well.", "te": "అతను చిన్నవాడు అని పరిశీలిస్తే, అతను బాగా చేశాడు.", "explanation": "'considering that' introduces a context."},
    {"en": "He ran fast in order that he might win.", "te": "గెలవాలని అతను వేగంగా పరిగెత్తాడు.", "explanation": "'in order that' shows purpose."},
    {"en": "I would rather die than surrender.", "te": "లొంగిపోయే బదులు నేను చనిపోవడానికి ఇష్టపడతాను.", "explanation": "'rather than' shows preference."},
    {"en": "He is not only a doctor but also a writer.", "te": "అతను డాక్టరే కాదు రచయిత కూడా.", "explanation": "Correlative conjunction pair."}
]

blanks_data = [
    {"question": "I want tea ___ coffee.", "correct_answer": "and", "telugu_meaning": "నాకు టీ మరియు కాఫీ కావాలి.", "explanation": "Adds two things together.", "options": ["but", "or", "and", "so"]},
    {"question": "He is rich ___ he is unhappy.", "correct_answer": "but", "telugu_meaning": "అతను ధనవంతుడు కానీ సంతోషంగా లేడు.", "explanation": "Shows contrast.", "options": ["and", "or", "so", "but"]},
    {"question": "Do you want tea ___ coffee?", "correct_answer": "or", "telugu_meaning": "మీకు టీ కావాలా లేక కాఫీ కావాలా?", "explanation": "Offers a choice.", "options": ["and", "but", "or", "so"]},
    {"question": "It was raining, ___ I took an umbrella.", "correct_answer": "so", "telugu_meaning": "వర్షం పడుతోంది, కాబట్టి నేను గొడుగు తీసుకున్నాను.", "explanation": "Shows the result.", "options": ["and", "but", "or", "so"]},
    {"question": "I didn't go to school ___ I was sick.", "correct_answer": "because", "telugu_meaning": "నేను అనారోగ్యంతో ఉన్నందున పాఠశాలకు వెళ్ళలేదు.", "explanation": "Gives a reason.", "options": ["so", "because", "but", "and"]},
    {"question": "___ it was raining, we played outside.", "correct_answer": "Although", "telugu_meaning": "వర్షం పడుతున్నప్పటికీ, మేము బయట ఆడుకున్నాము.", "explanation": "Shows a surprising contrast.", "options": ["Because", "Although", "Since", "If"]},
    {"question": "I will wait ___ you come back.", "correct_answer": "until", "telugu_meaning": "నువ్వు తిరిగి వచ్చే వరకు నేను వేచి ఉంటాను.", "explanation": "Up to the time that.", "options": ["until", "because", "if", "unless"]},
    {"question": "___ you work hard, you will pass.", "correct_answer": "If", "telugu_meaning": "నువ్వు కష్టపడి పనిచేస్తే, పాస్ అవుతావు.", "explanation": "Sets a condition.", "options": ["Unless", "Although", "If", "Because"]},
    {"question": "___ you study, you will fail.", "correct_answer": "Unless", "telugu_meaning": "నువ్వు చదవకపోతే, ఫెయిల్ అవుతావు.", "explanation": "Means 'if not'.", "options": ["Unless", "If", "Because", "Since"]},
    {"question": "He is ___ tall as his father.", "correct_answer": "as", "telugu_meaning": "అతను తన తండ్రి అంత పొడవుగా ఉన్నాడు.", "explanation": "Used for comparison.", "options": ["so", "too", "as", "very"]},
    {"question": "___ Ram and Shyam went to the party.", "correct_answer": "Both", "telugu_meaning": "రామ్ మరియు శ్యామ్ ఇద్దరూ పార్టీకి వెళ్ళారు.", "explanation": "Pairs with 'and'.", "options": ["Either", "Neither", "Both", "Not only"]},
    {"question": "You can ___ walk or take a bus.", "correct_answer": "either", "telugu_meaning": "నువ్వు నడవవచ్చు లేదా బస్సు తీసుకోవచ్చు.", "explanation": "Pairs with 'or'.", "options": ["neither", "both", "either", "whether"]},
    {"question": "___ Ram nor Shyam knows the answer.", "correct_answer": "Neither", "telugu_meaning": "రామ్‌కి తెలియదు, శ్యామ్‌కి కూడా సమాధానం తెలియదు.", "explanation": "Pairs with 'nor'.", "options": ["Either", "Both", "Neither", "Not only"]},
    {"question": "He speaks ___ only English but also Telugu.", "correct_answer": "not", "telugu_meaning": "అతను ఇంగ్లీష్ మాత్రమే కాదు తెలుగు కూడా మాట్లాడతాడు.", "explanation": "Pairs with 'but also'.", "options": ["not", "both", "either", "neither"]},
    {"question": "Wait here ___ I get the tickets.", "correct_answer": "while", "telugu_meaning": "నేను టిక్కెట్లు తెచ్చేంత వరకు ఇక్కడే ఉండు.", "explanation": "At the same time that.", "options": ["because", "if", "while", "unless"]},
    {"question": "___ he is poor, he is very generous.", "correct_answer": "Though", "telugu_meaning": "అతను పేదవాడైనప్పటికీ, అతను చాలా ఉదారంగా ఉంటాడు.", "explanation": "Similar to 'although'.", "options": ["Because", "Though", "Since", "If"]},
    {"question": "I went to bed early ___ I was tired.", "correct_answer": "as", "telugu_meaning": "నేను అలసిపోయినందున త్వరగా పడుకున్నాను.", "explanation": "Used to state a reason.", "options": ["so", "as", "but", "or"]},
    {"question": "Let me know ___ you are coming or not.", "correct_answer": "whether", "telugu_meaning": "నువ్వు వస్తున్నావో లేదో నాకు తెలియజేయి.", "explanation": "Pairs with 'or not'.", "options": ["if", "whether", "unless", "until"]},
    {"question": "Speak loudly ___ everyone can hear you.", "correct_answer": "so that", "telugu_meaning": "అందరూ వినేలా గట్టిగా మాట్లాడు.", "explanation": "Shows purpose.", "options": ["because", "so that", "if", "unless"]},
    {"question": "I will call you ___ I reach the station.", "correct_answer": "after", "telugu_meaning": "నేను స్టేషన్ చేరుకున్న తర్వాత నీకు కాల్ చేస్తాను.", "explanation": "Later in time.", "options": ["before", "after", "while", "until"]},
    {"question": "Wash your hands ___ you eat.", "correct_answer": "before", "telugu_meaning": "నువ్వు తినే ముందు నీ చేతులు కడుక్కో.", "explanation": "Earlier in time.", "options": ["before", "after", "while", "until"]},
    {"question": "He acts ___ he is the boss.", "correct_answer": "as if", "telugu_meaning": "అతను బాస్‌లా ప్రవర్తిస్తాడు.", "explanation": "Shows how something seems.", "options": ["as if", "even if", "unless", "so that"]},
    {"question": "I will go ___ it rains.", "correct_answer": "even if", "telugu_meaning": "వర్షం పడినా సరే నేను వెళ్తాను.", "explanation": "Shows condition won't affect outcome.", "options": ["as if", "even if", "unless", "because"]},
    {"question": "Take an umbrella ___ it rains.", "correct_answer": "in case", "telugu_meaning": "ఒకవేళ వర్షం పడితే అని గొడుగు తీసుకువెళ్ళు.", "explanation": "Precaution against a possible event.", "options": ["in case", "so that", "unless", "until"]},
    {"question": "___ long as you are with me, I am happy.", "correct_answer": "As", "telugu_meaning": "నువ్వు నాతో ఉన్నంత కాలం నేను సంతోషంగా ఉంటాను.", "explanation": "Provided that.", "options": ["So", "Too", "As", "Very"]},
    {"question": "You can play outside ___ that you finish your homework.", "correct_answer": "provided", "telugu_meaning": "నీ హోంవర్క్ పూర్తి చేస్తే నువ్వు బయట ఆడుకోవచ్చు.", "explanation": "On the condition that.", "options": ["provided", "unless", "whether", "although"]},
    {"question": "He failed ___ he tried hard.", "correct_answer": "even though", "telugu_meaning": "అతను కష్టపడినప్పటికీ ఫెయిల్ అయ్యాడు.", "explanation": "Stronger form of 'although'.", "options": ["because", "since", "even though", "so"]},
    {"question": "He is smart, ___ his brother is dull.", "correct_answer": "whereas", "telugu_meaning": "అతను చురుకైనవాడు, అయితే అతని సోదరుడు మందబుద్ధి.", "explanation": "Shows contrast between two facts.", "options": ["so", "because", "whereas", "unless"]},
    {"question": "___ you are ready, let's start.", "correct_answer": "Now that", "telugu_meaning": "ఇప్పుడు నువ్వు సిద్ధంగా ఉన్నావు కాబట్టి, మనం ప్రారంభిద్దాం.", "explanation": "Because of a new situation.", "options": ["Unless", "Now that", "Although", "Even if"]},
    {"question": "I will follow you ___ you go.", "correct_answer": "wherever", "telugu_meaning": "నువ్వు ఎక్కడికి వెళ్లినా నేను వస్తాను.", "explanation": "Any place that.", "options": ["wherever", "whenever", "whoever", "whichever"]}
]

speaking_data = [
    {"question": "I like apples and bananas.", "telugu_meaning": "నాకు ఆపిల్స్ మరియు అరటిపండ్లు ఇష్టం.", "explanation": "Focus on 'and'."},
    {"question": "He is poor but honest.", "telugu_meaning": "అతను పేదవాడు కానీ నిజాయితీపరుడు.", "explanation": "Focus on 'but'."},
    {"question": "Do you want tea or coffee?", "telugu_meaning": "మీకు టీ కావాలా లేదా కాఫీ కావాలా?", "explanation": "Focus on 'or'."},
    {"question": "I was sick, so I stayed home.", "telugu_meaning": "నేను అనారోగ్యంతో ఉన్నాను, కాబట్టి నేను ఇంట్లోనే ఉన్నాను.", "explanation": "Focus on 'so'."},
    {"question": "I stayed home because I was sick.", "telugu_meaning": "నేను అనారోగ్యంతో ఉన్నందున ఇంట్లోనే ఉన్నాను.", "explanation": "Focus on 'because'."},
    {"question": "Although it rained, we played.", "telugu_meaning": "వర్షం పడినప్పటికీ, మేము ఆడుకున్నాము.", "explanation": "Focus on 'although'."},
    {"question": "Wait until I return.", "telugu_meaning": "నేను తిరిగి వచ్చే వరకు వేచి ఉండు.", "explanation": "Focus on 'until'."},
    {"question": "If it rains, we will stay.", "telugu_meaning": "వర్షం పడితే, మేము ఉండిపోతాము.", "explanation": "Focus on 'if'."},
    {"question": "Unless you hurry, you will be late.", "telugu_meaning": "నువ్వు తొందరపడకపోతే, నీకు ఆలస్యం అవుతుంది.", "explanation": "Focus on 'unless'."},
    {"question": "He is as tall as me.", "telugu_meaning": "అతను నా అంత ఎత్తు ఉన్నాడు.", "explanation": "Focus on 'as...as'."},
    {"question": "Both Ram and Shyam came.", "telugu_meaning": "రామ్ మరియు శ్యామ్ ఇద్దరూ వచ్చారు.", "explanation": "Focus on 'both...and'."},
    {"question": "Either you or I must go.", "telugu_meaning": "నువ్వు లేదా నేను ఖచ్చితంగా వెళ్లాలి.", "explanation": "Focus on 'either...or'."},
    {"question": "Neither Ram nor Shyam came.", "telugu_meaning": "రామ్ రాలేదు, శ్యామ్ కూడా రాలేదు.", "explanation": "Focus on 'neither...nor'."},
    {"question": "I haven't seen him since Monday.", "telugu_meaning": "నేను సోమవారం నుండి అతన్ని చూడలేదు.", "explanation": "Focus on 'since'."},
    {"question": "Read a book while you wait.", "telugu_meaning": "నువ్వు వేచి ఉన్న సమయంలో ఒక పుస్తకం చదువు.", "explanation": "Focus on 'while'."},
    {"question": "Call me as soon as you arrive.", "telugu_meaning": "నువ్వు రాగానే నాకు కాల్ చేయి.", "explanation": "Focus on 'as soon as'."},
    {"question": "He is rich, yet unhappy.", "telugu_meaning": "అతను ధనవంతుడు, అయినప్పటికీ సంతోషంగా లేడు.", "explanation": "Focus on 'yet'."},
    {"question": "Tell me whether you will come or not.", "telugu_meaning": "నువ్వు వస్తావో లేదో నాకు చెప్పు.", "explanation": "Focus on 'whether'."},
    {"question": "Speak up so that I can hear you.", "telugu_meaning": "నేను వినగలిగేలా గట్టిగా మాట్లాడు.", "explanation": "Focus on 'so that'."},
    {"question": "I will go after dinner.", "telugu_meaning": "నేను భోజనం తర్వాత వెళ్తాను.", "explanation": "Focus on 'after'."},
    {"question": "Wash hands before eating.", "telugu_meaning": "తినే ముందు చేతులు కడుక్కో.", "explanation": "Focus on 'before'."},
    {"question": "I don't know where he went.", "telugu_meaning": "అతను ఎక్కడికి వెళ్ళాడో నాకు తెలియదు.", "explanation": "Focus on 'where'."},
    {"question": "I know when the train leaves.", "telugu_meaning": "రైలు ఎప్పుడు బయలుదేరుతుందో నాకు తెలుసు.", "explanation": "Focus on 'when'."},
    {"question": "He acts as if he knows everything.", "telugu_meaning": "అతనికి అన్నీ తెలిసినట్లు ప్రవర్తిస్తాడు.", "explanation": "Focus on 'as if'."},
    {"question": "I will go even if it rains.", "telugu_meaning": "వర్షం పడినా నేను వెళ్తాను.", "explanation": "Focus on 'even if'."},
    {"question": "Take an umbrella in case it rains.", "telugu_meaning": "వర్షం పడితే అని గొడుగు తీసుకువెళ్ళు.", "explanation": "Focus on 'in case'."},
    {"question": "As long as you are safe, it's fine.", "telugu_meaning": "నువ్వు సురక్షితంగా ఉన్నంత వరకు పర్వాలేదు.", "explanation": "Focus on 'as long as'."},
    {"question": "I will go wherever you go.", "telugu_meaning": "నువ్వు ఎక్కడికి వెళ్లినా నేను వస్తాను.", "explanation": "Focus on 'wherever'."},
    {"question": "Come whenever you are free.", "telugu_meaning": "నువ్వు ఫ్రీగా ఉన్నప్పుడు రా.", "explanation": "Focus on 'whenever'."},
    {"question": "He failed even though he studied.", "telugu_meaning": "అతను చదివినప్పటికీ ఫెయిల్ అయ్యాడు.", "explanation": "Focus on 'even though'."}
]

concept = Concept.objects.filter(name='Conjunctions').first()
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
    print("Conjunctions completed successfully.")
else:
    print("Concept 'Conjunctions' not found.")
