# backend/depression_knowledge.py

questions = {
    'depresion': '¿Siente tristeza persistente o pérdida de interés?',
    'insomnio': '¿Tiene problemas para dormir?',
    'cambios_en_el_apetito': '¿Tiene cambios significativos en el apetito o el peso?',
    'pensamientos_suicidas': '¿Tiene pensamientos de muerte o suicidio?',
    'fatiga': '¿Siente fatiga o falta de energía?',
    'dificultad_para_concentrarse': '¿Tiene dificultad para concentrarse?',
    'culpa': '¿Siente culpa o inutilidad excesiva?',
    'agitación': '¿Se siente agitado o inquieto?',
    'llanto_incontrolable': '¿Llora sin razón aparente?',
    'dolores_fisicos': '¿Tiene dolores físicos sin causa aparente?',
    'perdida_de_interes': '¿Ha perdido interés en actividades que antes disfrutaba?',
    'pensamientos_negativos': '¿Tiene pensamientos negativos persistentes?',
    'aislamiento_social': '¿Se ha aislado socialmente?',
    'falta_de_motivacion': '¿Le falta motivación para realizar tareas diarias?',
    'cambios_en_el_peso': '¿Ha notado cambios en su peso sin razón aparente?'
}

diseases = {
    'trastorno_depresivo_mayor': ['depresion', 'insomnio', 'fatiga', 'dificultad_para_concentrarse', 'cambios_en_el_apetito', 'pensamientos_suicidas'],
    'trastorno_distimico': ['depresion', 'fatiga', 'dificultad_para_concentrarse', 'baja_autoestima', 'falta_de_motivacion', 'pensamientos_negativos'],
    'trastorno_afectivo_estacional': ['depresion', 'fatiga', 'cambios_en_el_apetito', 'dificultad_para_concentrarse', 'aislamiento_social'],
    'depresion_psicotica': ['depresion', 'pensamientos_suicidas', 'alucinaciones', 'delirios', 'agitación', 'insomnio'],
    'depresion_postparto': ['depresion', 'fatiga', 'cambios_en_el_apetito', 'insomnio', 'llanto_incontrolable', 'culpa']
}

rules = [
    {'if': ['depresion', 'insomnio', 'fatiga', 'dificultad_para_concentrarse', 'cambios_en_el_apetito', 'pensamientos_suicidas'], 'then': 'trastorno_depresivo_mayor'},
    {'if': ['depresion', 'fatiga', 'dificultad_para_concentrarse', 'baja_autoestima', 'falta_de_motivacion', 'pensamientos_negativos'], 'then': 'trastorno_distimico'},
    {'if': ['depresion', 'fatiga', 'cambios_en_el_apetito', 'dificultad_para_concentrarse', 'aislamiento_social'], 'then': 'trastorno_afectivo_estacional'},
    {'if': ['depresion', 'pensamientos_suicidas', 'alucinaciones', 'delirios', 'agitación', 'insomnio'], 'then': 'depresion_psicotica'},
    {'if': ['depresion', 'fatiga', 'cambios_en_el_apetito', 'insomnio', 'llanto_incontrolable', 'culpa'], 'then': 'depresion_postparto'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
