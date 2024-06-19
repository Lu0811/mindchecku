# backend/anxiety_knowledge.py

questions = {
    'ansiedad': '¿Siente ansiedad o preocupación excesiva con frecuencia?',
    'ataques_de_panico': '¿Experimenta ataques de pánico súbitos e intensos?',
    'fobias': '¿Evita ciertas situaciones debido a un miedo intenso?',
    'ansiedad_social': '¿Siente un miedo intenso a ser juzgado en situaciones sociales?',
    'preocupacion_excesiva': '¿Se preocupa excesivamente por diferentes aspectos de su vida?',
    'dificultad_para_relajarse': '¿Tiene dificultad para relajarse?',
    'tension_muscular': '¿Siente tensión muscular constante?',
    'problemas_para_dormir': '¿Tiene problemas para dormir debido a la ansiedad?',
    'ritmo_cardiaco_acelerado': '¿Siente que su corazón late más rápido de lo normal?',
    'dificultad_para_respirar': '¿Tiene dificultad para respirar?',
    'sudoracion_excesiva': '¿Suda excesivamente en situaciones de ansiedad?',
    'temblores': '¿Siente temblores o sacudidas en su cuerpo?',
    'sensacion_de_irrealidad': '¿Siente que las cosas a su alrededor no son reales?',
    'miedo_a_perder_el_control': '¿Tiene miedo a perder el control?',
    'evitacion': '¿Evita actividades o situaciones debido a la ansiedad?',
    'dificultad_para_concentrarse': '¿Tiene dificultad para concentrarse debido a la preocupación?'
}

diseases = {
    'trastorno_de_ansiedad_generalizada': ['ansiedad', 'preocupacion_excesiva', 'dificultad_para_relajarse', 'tension_muscular', 'problemas_para_dormir', 'dificultad_para_concentrarse'],
    'trastorno_de_panico': ['ataques_de_panico', 'ritmo_cardiaco_acelerado', 'dificultad_para_respirar', 'sudoracion_excesiva', 'temblores', 'miedo_a_perder_el_control'],
    'trastorno_de_ansiedad_social': ['ansiedad_social', 'preocupacion_excesiva', 'evitacion', 'ritmo_cardiaco_acelerado', 'sudoracion_excesiva', 'temblores'],
    'fobia_especifica': ['fobias', 'ansiedad', 'evitacion', 'ritmo_cardiaco_acelerado', 'dificultad_para_respirar'],
    'trastorno_obsesivo_compulsivo': ['obsesiones', 'compulsiones', 'ansiedad'],
    'trastorno_por_estrés_postraumático': ['flashbacks', 'evitacion', 'ansiedad', 'problemas_para_dormir', 'irritabilidad']
}

rules = [
    {'if': ['ansiedad', 'preocupacion_excesiva', 'dificultad_para_relajarse', 'tension_muscular', 'problemas_para_dormir'], 'then': 'trastorno_de_ansiedad_generalizada'},
    {'if': ['ataques_de_panico', 'ritmo_cardiaco_acelerado', 'dificultad_para_respirar', 'sudoracion_excesiva', 'temblores', 'miedo_a_perder_el_control'], 'then': 'trastorno_de_panico'},
    {'if': ['ansiedad_social', 'preocupacion_excesiva', 'evitacion', 'ritmo_cardiaco_acelerado', 'sudoracion_excesiva', 'temblores'], 'then': 'trastorno_de_ansiedad_social'},
    {'if': ['fobias', 'ansiedad', 'evitacion', 'ritmo_cardiaco_acelerado', 'dificultad_para_respirar'], 'then': 'fobia_especifica'},
    {'if': ['obsesiones', 'compulsiones', 'ansiedad'], 'then': 'trastorno_obsesivo_compulsivo'},
    {'if': ['flashbacks', 'evitacion', 'ansiedad', 'problemas_para_dormir', 'irritabilidad'], 'then': 'trastorno_por_estrés_postraumático'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
