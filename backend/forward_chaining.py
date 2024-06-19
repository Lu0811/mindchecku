# backend/forward_chaining.py

def forward_chaining(facts, rules):
    inferred = []
    while True:
        new_inference = False
        for rule in rules:
            if all(fact in facts for fact in rule['if']) and rule['then'] not in inferred:
                inferred.append(rule['then'])
                facts.append(rule['then'])
                new_inference = True
        if not new_inference:
            break
    return inferred
