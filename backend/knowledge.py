# backend/knowledge.py

questions = {
    'anxiety': 'Do you often feel anxious or worried?',
    'depression': 'Do you feel persistent sadness or loss of interest?',
    'insomnia': 'Do you have trouble sleeping?',
    'irritability': 'Do you often feel irritable or easily angered?',
    'fatigue': 'Do you often feel fatigued or have low energy?',
    'difficulty_concentrating': 'Do you have difficulty concentrating or making decisions?'
}

diseases = {
    'generalized_anxiety_disorder': ['anxiety', 'fatigue', 'difficulty_concentrating'],
    'major_depressive_disorder': ['depression', 'insomnia', 'fatigue', 'difficulty_concentrating'],
    'insomnia_disorder': ['insomnia', 'fatigue', 'irritability'],
    'bipolar_disorder': ['depression', 'irritability', 'anxiety']
}

rules = [
    {'if': ['anxiety', 'fatigue', 'difficulty_concentrating'], 'then': 'generalized_anxiety_disorder'},
    {'if': ['depression', 'insomnia', 'fatigue', 'difficulty_concentrating'], 'then': 'major_depressive_disorder'},
    {'if': ['insomnia', 'fatigue', 'irritability'], 'then': 'insomnia_disorder'},
    {'if': ['depression', 'irritability', 'anxiety'], 'then': 'bipolar_disorder'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
