from flask import Flask, request, jsonify
from utils import load_knowledge
from diagnosis import find_diagnosis

app = Flask(__name__)

@app.route('/api/questions/anxiety', methods=['GET'])
def get_questions_anxiety():
    questions, _, _ = load_knowledge('anxiety_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/questions/depression', methods=['GET'])
def get_questions_depression():
    questions, _, _ = load_knowledge('depression_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/questions/bipolar', methods=['GET'])
def get_questions_bipolar():
    questions, _, _ = load_knowledge('bipolar_disorder_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/questions/eating_disorder', methods=['GET'])
def get_questions_eating_disorder():
    questions, _, _ = load_knowledge('eating_disorder_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/questions/ocd', methods=['GET'])
def get_questions_ocd():
    questions, _, _ = load_knowledge('ocd_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/questions/ptsd', methods=['GET'])
def get_questions_ptsd():
    questions, _, _ = load_knowledge('ptsd_knowledge')
    return jsonify({'questions': questions})

@app.route('/api/diagnose/anxiety', methods=['POST'])
def diagnose_anxiety():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('anxiety_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

@app.route('/api/diagnose/depression', methods=['POST'])
def diagnose_depression():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('depression_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

@app.route('/api/diagnose/bipolar', methods=['POST'])
def diagnose_bipolar():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('bipolar_disorder_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

@app.route('/api/diagnose/eating_disorder', methods=['POST'])
def diagnose_eating_disorder():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('eating_disorder_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

@app.route('/api/diagnose/ocd', methods=['POST'])
def diagnose_ocd():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('ocd_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

@app.route('/api/diagnose/ptsd', methods=['POST'])
def diagnose_ptsd():
    user_responses = request.json.get('responses', {})
    user_symptoms = [symptom for symptom, answer in user_responses.items() if answer == 'yes']
    _, _, rules = load_knowledge('ptsd_knowledge')
    diagnosis = find_diagnosis(user_symptoms, rules)
    return jsonify({'diagnosis': diagnosis})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
