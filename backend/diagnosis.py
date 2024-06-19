# backend/diagnosis.py

from forward_chaining import forward_chaining

def find_diagnosis(user_symptoms, rules):
    inferred_diseases = forward_chaining(user_symptoms, rules)
    if inferred_diseases:
        return inferred_diseases[0]  # Return the first inferred disease
    return "Diagnostico no encontrado"

