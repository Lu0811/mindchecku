# backend/bipolar_disorder_knowledge.py

questions = {
    'episodios_maniacos': '¿Experimenta períodos de energía o actividad inusualmente alta?',
    'episodios_depresivos': '¿Experimenta períodos de energía o actividad inusualmente baja?',
    'cambios_rapidos_de_humor': '¿Experimenta cambios rápidos en el estado de ánimo?',
    'problemas_para_dormir': '¿Tiene problemas para dormir?',
    'hablar_rapidamente': '¿Habla más rápido de lo normal?',
    'pensamientos_acelerados': '¿Tiene pensamientos acelerados?',
    'baja_autoestima': '¿Siente baja autoestima o falta de confianza en sí mismo?',
    'dificultad_para_concentrarse': '¿Tiene dificultad para concentrarse?',
    'irritabilidad': '¿Se siente irritable o de mal humor?',
    'aumento_de_actividad': '¿Ha notado un aumento significativo en su actividad?',
    'ideas_de_grandeza': '¿Tiene ideas de grandeza o pensamientos exagerados sobre sus habilidades?',
    'pérdida_de_interés': '¿Ha perdido interés en actividades que antes disfrutaba?',
    'cambios_en_el_apetito': '¿Ha notado cambios en su apetito?',
    'pensamientos_suicidas': '¿Ha tenido pensamientos de suicidio o autolesiones?',
    'impulsividad': '¿Actúa de manera impulsiva sin considerar las consecuencias?',
    'hipersensibilidad': '¿Es muy sensible a las críticas o el rechazo?',
    'aumento_del_deseo_sexual': '¿Ha notado un aumento inusual en su deseo sexual?',
    'gasto_excesivo': '¿Ha realizado gastos excesivos o irresponsables?',
    'aumento_en_el_consumo_de_sustancias': '¿Ha aumentado el consumo de alcohol u otras sustancias?'
}

diseases = {
    'trastorno_bipolar_I': ['episodios_maniacos', 'episodios_depresivos', 'cambios_rapidos_de_humor', 'problemas_para_dormir', 'hablar_rapidamente', 'pensamientos_acelerados', 'ideas_de_grandeza', 'impulsividad', 'gasto_excesivo'],
    'trastorno_bipolar_II': ['episodios_hipomaniacos', 'episodios_depresivos', 'cambios_rapidos_de_humor', 'problemas_para_dormir', 'pensamientos_acelerados', 'baja_autoestima', 'dificultad_para_concentrarse'],
    'trastorno_ciclotímico': ['cambios_rapidos_de_humor', 'baja_autoestima', 'dificultad_para_concentrarse', 'irritabilidad', 'aumento_de_actividad', 'pérdida_de_interés', 'hipersensibilidad'],
    'depresion_bipolar': ['episodios_depresivos', 'baja_autoestima', 'dificultad_para_concentrarse', 'pérdida_de_interés', 'cambios_en_el_apetito', 'pensamientos_suicidas']
}

rules = [
    {'if': ['episodios_maniacos', 'episodios_depresivos', 'cambios_rapidos_de_humor'], 'then': 'trastorno_bipolar_I'},
    {'if': ['episodios_hipomaniacos', 'episodios_depresivos', 'cambios_rapidos_de_humor'], 'then': 'trastorno_bipolar_II'},
    {'if': ['cambios_rapidos_de_humor', 'baja_autoestima', 'dificultad_para_concentrarse', 'irritabilidad', 'aumento_de_actividad', 'hipersensibilidad'], 'then': 'trastorno_ciclotímico'},
    {'if': ['episodios_depresivos', 'baja_autoestima', 'dificultad_para_concentrarse', 'pérdida_de_interés', 'cambios_en_el_apetito', 'pensamientos_suicidas'], 'then': 'depresion_bipolar'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
