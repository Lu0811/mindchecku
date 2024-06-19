# backend/utils.py

def load_knowledge(module_name):
    module = __import__(module_name)
    return module.questions, module.diseases, module.rules
