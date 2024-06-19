def add_symptom(symptom):
    if symptom not in symptoms:
        symptoms.append(symptom)

def add_disease(disease, symptoms_list):
    if disease not in diseases:
        diseases[disease] = symptoms_list
