# backend/ocd_knowledge.py

questions = {
    'obsesiones': '¿Tiene pensamientos persistentes e indeseados?',
    'compulsiones': '¿Realiza comportamientos repetitivos para reducir la ansiedad?',
    'pensamientos_intrusivos': '¿Experimenta pensamientos intrusivos y angustiantes?',
    'temor_a_la_contaminacion': '¿Tiene un temor excesivo a la contaminación?',
    'dudas_excesivas': '¿Duda excesivamente de sus acciones?',
    'necesidad_de_simetria': '¿Siente una necesidad de que las cosas estén perfectamente ordenadas o simétricas?',
    'conductas_de_verificacion': '¿Verifica repetidamente cosas como cerraduras, electrodomésticos, etc.?',
    'lavado_excesivo': '¿Se lava las manos excesivamente?',
    'acumulacion': '¿Acumula objetos y tiene dificultad para deshacerse de ellos?',
    'rituales_mentales': '¿Realiza rituales mentales para aliviar la ansiedad?',
    'pensamientos_de_agresion': '¿Tiene pensamientos intrusivos de agresión hacia otros?',
    'pensamientos_de_naturaleza_sexual': '¿Tiene pensamientos intrusivos de naturaleza sexual?',
    'miedo_a_hacer_daño': '¿Tiene miedo de causar daño a otros de alguna manera?',
    'pensamientos_blafemos': '¿Experimenta pensamientos intrusivos de naturaleza blasfema o religiosa?'
}

diseases = {
    'trastorno_obsesivo_compulsivo': ['obsesiones', 'compulsiones', 'pensamientos_intrusivos', 'temor_a_la_contaminacion', 'dudas_excesivas', 'necesidad_de_simetria', 'conductas_de_verificacion', 'lavado_excesivo', 'acumulacion'],
    'toc_puro': ['obsesiones', 'pensamientos_intrusivos', 'rituales_mentales', 'pensamientos_de_agresion', 'pensamientos_de_naturaleza_sexual', 'miedo_a_hacer_daño', 'pensamientos_blafemos'],
    'toc_de_contaminacion': ['obsesiones', 'temor_a_la_contaminacion', 'lavado_excesivo', 'conductas_de_verificacion'],
    'toc_de_verificacion': ['obsesiones', 'dudas_excesivas', 'conductas_de_verificacion']
}

rules = [
    {'if': ['obsesiones', 'compulsiones'], 'then': 'trastorno_obsesivo_compulsivo'},
    {'if': ['obsesiones', 'pensamientos_intrusivos', 'rituales_mentales'], 'then': 'toc_puro'},
    {'if': ['obsesiones', 'temor_a_la_contaminacion', 'lavado_excesivo'], 'then': 'toc_de_contaminacion'},
    {'if': ['obsesiones', 'dudas_excesivas', 'conductas_de_verificacion'], 'then': 'toc_de_verificacion'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
