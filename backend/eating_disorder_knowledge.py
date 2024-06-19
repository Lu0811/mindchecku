# backend/eating_disorder_knowledge.py

questions = {
    'restriccion_alimentaria': '¿Restringe su alimentación para controlar su peso?',
    'atracones': '¿Come grandes cantidades de comida en un corto periodo de tiempo?',
    'conductas_de_purga': '¿Utiliza métodos como vomitar para controlar su peso?',
    'miedo_intenso_a_subir_de_peso': '¿Tiene un miedo intenso a subir de peso?',
    'percepcion_distorsionada_del_cuerpo': '¿Tiene una percepción distorsionada de su cuerpo?',
    'ejercicio_excesivo': '¿Realiza ejercicio excesivo para controlar su peso?',
    'sentimientos_de_culpa': '¿Siente culpa o vergüenza después de comer?',
    'aislamiento_social': '¿Se aísla socialmente debido a su alimentación?',
    'fluctuaciones_de_peso': '¿Experimenta fluctuaciones significativas de peso?',
    'uso_de_laxantes': '¿Utiliza laxantes para controlar su peso?',
    'preocupacion_excesiva_por_la_comida': '¿Está excesivamente preocupado por la comida y el peso?',
    'comer_en_secreto': '¿Come en secreto para evitar que otros lo vean?',
    'malestar_digestivo': '¿Experimenta malestar digestivo frecuentemente?',
    'problemas_menstruales': '¿Tiene problemas menstruales debido a su alimentación?',
    'deshidratacion': '¿Sufre de deshidratación frecuentemente?'
}

diseases = {
    'anorexia_nerviosa': ['restriccion_alimentaria', 'miedo_intenso_a_subir_de_peso', 'percepcion_distorsionada_del_cuerpo', 'ejercicio_excesivo', 'problemas_menstruales', 'deshidratacion'],
    'bulimia_nerviosa': ['atracones', 'conductas_de_purga', 'sentimientos_de_culpa', 'aislamiento_social', 'fluctuaciones_de_peso', 'uso_de_laxantes', 'preocupacion_excesiva_por_la_comida'],
    'trastorno_por_atracon': ['atracones', 'sentimientos_de_culpa', 'comer_en_secreto', 'malestar_digestivo', 'fluctuaciones_de_peso'],
    'ortorexia': ['preocupacion_excesiva_por_la_comida', 'restriccion_alimentaria', 'ejercicio_excesivo', 'aislamiento_social', 'deshidratacion']
}

rules = [
    {'if': ['restriccion_alimentaria', 'miedo_intenso_a_subir_de_peso', 'percepcion_distorsionada_del_cuerpo'], 'then': 'anorexia_nerviosa'},
    {'if': ['atracones', 'conductas_de_purga', 'sentimientos_de_culpa'], 'then': 'bulimia_nerviosa'},
    {'if': ['atracones', 'sentimientos_de_culpa', 'comer_en_secreto'], 'then': 'trastorno_por_atracon'},
    {'if': ['preocupacion_excesiva_por_la_comida', 'restriccion_alimentaria', 'ejercicio_excesivo'], 'then': 'ortorexia'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
