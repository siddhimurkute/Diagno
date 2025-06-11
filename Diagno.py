class MedicalChatbot:
    def __init__(self):
        self.diseases = {
            # Respiratory Diseases (15)
            'Common Cold': {'symptoms': ['runny nose', 'sneezing', 'sore throat', 'cough', 'congestion', 'mild fever'], 'category': 'Respiratory'},
            'Influenza (Flu)': {'symptoms': ['fever', 'chills', 'muscle aches', 'fatigue', 'headache', 'dry cough', 'sore throat'], 'category': 'Respiratory'},
            'Pneumonia': {'symptoms': ['fever', 'chills', 'productive cough', 'shortness of breath', 'chest pain', 'fatigue'], 'category': 'Respiratory'},
            'Bronchitis': {'symptoms': ['persistent cough', 'mucus production', 'fatigue', 'shortness of breath', 'mild fever'], 'category': 'Respiratory'},
            'Tuberculosis': {'symptoms': ['chronic cough', 'bloody mucus', 'fever', 'night sweats', 'weight loss'], 'category': 'Respiratory'},
            'Asthma': {'symptoms': ['wheezing', 'shortness of breath', 'chest tightness', 'coughing'], 'category': 'Respiratory'},
            'COPD': {'symptoms': ['chronic cough', 'shortness of breath', 'wheezing', 'chest tightness'], 'category': 'Respiratory'},
            'Sinusitis': {'symptoms': ['facial pain', 'nasal congestion', 'thick nasal discharge', 'reduced smell'], 'category': 'Respiratory'},
            'Laryngitis': {'symptoms': ['hoarseness', 'weak voice', 'tickling throat', 'dry cough'], 'category': 'Respiratory'},
            'Pharyngitis': {'symptoms': ['sore throat', 'painful swallowing', 'swollen tonsils', 'fever'], 'category': 'Respiratory'},
            'Pleurisy': {'symptoms': ['sharp chest pain', 'pain with breathing', 'shortness of breath', 'cough'], 'category': 'Respiratory'},
            'Pulmonary Embolism': {'symptoms': ['sudden shortness of breath', 'chest pain', 'coughing up blood', 'rapid heart rate'], 'category': 'Respiratory'},
            'Lung Cancer': {'symptoms': ['chronic cough', 'coughing up blood', 'chest pain', 'weight loss', 'fatigue'], 'category': 'Respiratory'},
            'Croup': {'symptoms': ['barking cough', 'hoarseness', 'difficulty breathing', 'fever'], 'category': 'Respiratory'},
            'Whooping Cough': {'symptoms': ['severe coughing fits', 'whooping sound', 'vomiting after coughing', 'fatigue'], 'category': 'Respiratory'},

            # Gastrointestinal Diseases (15)
            'Gastroenteritis': {'symptoms': ['diarrhea', 'nausea', 'vomiting', 'stomach pain', 'fever'], 'category': 'Gastrointestinal'},
            'Food Poisoning': {'symptoms': ['nausea', 'vomiting', 'diarrhea', 'stomach cramps', 'fever'], 'category': 'Gastrointestinal'},
            'GERD': {'symptoms': ['heartburn', 'regurgitation', 'chest pain', 'difficulty swallowing'], 'category': 'Gastrointestinal'},
            'Peptic Ulcer': {'symptoms': ['burning stomach pain', 'bloating', 'heartburn', 'nausea'], 'category': 'Gastrointestinal'},
            'Irritable Bowel Syndrome': {'symptoms': ['abdominal pain', 'bloating', 'diarrhea', 'constipation'], 'category': 'Gastrointestinal'},
            'Crohn\'s Disease': {'symptoms': ['diarrhea', 'abdominal pain', 'fatigue', 'weight loss', 'blood in stool'], 'category': 'Gastrointestinal'},
            'Ulcerative Colitis': {'symptoms': ['diarrhea', 'rectal bleeding', 'abdominal pain', 'urgency to defecate'], 'category': 'Gastrointestinal'},
            'Appendicitis': {'symptoms': ['abdominal pain', 'loss of appetite', 'nausea', 'fever'], 'category': 'Gastrointestinal'},
            'Gallstones': {'symptoms': ['sudden abdominal pain', 'back pain', 'nausea', 'vomiting'], 'category': 'Gastrointestinal'},
            'Pancreatitis': {'symptoms': ['upper abdominal pain', 'back pain', 'nausea', 'vomiting', 'fever'], 'category': 'Gastrointestinal'},
            'Celiac Disease': {'symptoms': ['diarrhea', 'weight loss', 'bloating', 'abdominal pain', 'fatigue'], 'category': 'Gastrointestinal'},
            'Diverticulitis': {'symptoms': ['abdominal pain', 'fever', 'nausea', 'constipation or diarrhea'], 'category': 'Gastrointestinal'},
            'Hepatitis A': {'symptoms': ['fatigue', 'nausea', 'abdominal pain', 'jaundice', 'dark urine'], 'category': 'Gastrointestinal'},
            'Hepatitis B': {'symptoms': ['fatigue', 'nausea', 'abdominal pain', 'jaundice', 'joint pain'], 'category': 'Gastrointestinal'},
            'Cirrhosis': {'symptoms': ['fatigue', 'easy bruising', 'jaundice', 'abdominal swelling'], 'category': 'Gastrointestinal'},

            # Neurological Disorders (15)
            'Migraine': {'symptoms': ['severe headache', 'nausea', 'sensitivity to light', 'aura'], 'category': 'Neurological'},
            'Tension Headache': {'symptoms': ['dull head pain', 'tightness around forehead', 'tenderness'], 'category': 'Neurological'},
            'Cluster Headache': {'symptoms': ['severe one-sided pain', 'eye redness', 'nasal congestion', 'restlessness'], 'category': 'Neurological'},
            'Epilepsy': {'symptoms': ['seizures', 'temporary confusion', 'staring spells', 'uncontrollable movements'], 'category': 'Neurological'},
            'Parkinson\'s Disease': {'symptoms': ['tremors', 'stiffness', 'slow movement', 'balance problems'], 'category': 'Neurological'},
            'Multiple Sclerosis': {'symptoms': ['numbness', 'weakness', 'vision problems', 'balance issues'], 'category': 'Neurological'},
            'Alzheimer\'s Disease': {'symptoms': ['memory loss', 'confusion', 'difficulty with tasks', 'personality changes'], 'category': 'Neurological'},
            'Bell\'s Palsy': {'symptoms': ['facial drooping', 'drooling', 'eye problems', 'loss of taste'], 'category': 'Neurological'},
            'Carpal Tunnel Syndrome': {'symptoms': ['hand numbness', 'tingling', 'weakness', 'pain radiating up arm'], 'category': 'Neurological'},
            'Neuropathy': {'symptoms': ['numbness', 'tingling', 'burning pain', 'sensitivity to touch'], 'category': 'Neurological'},
            'Stroke': {'symptoms': ['face drooping', 'arm weakness', 'speech difficulty', 'sudden headache'], 'category': 'Neurological'},
            'Concussion': {'symptoms': ['headache', 'confusion', 'dizziness', 'nausea', 'memory problems'], 'category': 'Neurological'},
            'Meningitis': {'symptoms': ['sudden fever', 'stiff neck', 'severe headache', 'confusion'], 'category': 'Neurological'},
            'Brain Tumor': {'symptoms': ['headaches', 'seizures', 'vision problems', 'personality changes'], 'category': 'Neurological'},
            'ALS': {'symptoms': ['muscle weakness', 'twitching', 'stiffness', 'slurred speech'], 'category': 'Neurological'},

            # Cardiovascular Diseases (15)
            'Hypertension': {'symptoms': ['often asymptomatic', 'headache', 'dizziness', 'blurred vision'], 'category': 'Cardiovascular'},
            'Coronary Artery Disease': {'symptoms': ['chest pain', 'shortness of breath', 'heart attack'], 'category': 'Cardiovascular'},
            'Heart Attack': {'symptoms': ['chest pain', 'shortness of breath', 'nausea', 'cold sweat'], 'category': 'Cardiovascular'},
            'Heart Failure': {'symptoms': ['shortness of breath', 'fatigue', 'swelling in legs', 'rapid heartbeat'], 'category': 'Cardiovascular'},
            'Arrhythmia': {'symptoms': ['palpitations', 'racing heart', 'slow heartbeat', 'chest pain'], 'category': 'Cardiovascular'},
            'Atrial Fibrillation': {'symptoms': ['irregular heartbeat', 'palpitations', 'fatigue', 'dizziness'], 'category': 'Cardiovascular'},
            'Pericarditis': {'symptoms': ['sharp chest pain', 'fever', 'weakness', 'cough'], 'category': 'Cardiovascular'},
            'Endocarditis': {'symptoms': ['fever', 'fatigue', 'muscle aches', 'night sweats'], 'category': 'Cardiovascular'},
            'Cardiomyopathy': {'symptoms': ['breathlessness', 'swelling in legs', 'fatigue', 'irregular heartbeat'], 'category': 'Cardiovascular'},
            'Aortic Aneurysm': {'symptoms': ['often asymptomatic', 'back pain', 'abdominal pain', 'pulsating feeling'], 'category': 'Cardiovascular'},
            'Deep Vein Thrombosis': {'symptoms': ['leg swelling', 'leg pain', 'red skin', 'warmth in area'], 'category': 'Cardiovascular'},
            'Varicose Veins': {'symptoms': ['bulging veins', 'leg pain', 'heaviness', 'itching'], 'category': 'Cardiovascular'},
            'Peripheral Artery Disease': {'symptoms': ['leg pain when walking', 'numbness', 'cold legs'], 'category': 'Cardiovascular'},
            'Hypercholesterolemia': {'symptoms': ['often asymptomatic', 'xanthomas', 'chest pain'], 'category': 'Cardiovascular'},
            'Rheumatic Fever': {'symptoms': ['fever', 'joint pain', 'rash', 'fatigue'], 'category': 'Cardiovascular'},

            # Continue with other categories (Dermatological, Endocrine, etc.)...
        }

        self.all_symptoms = sorted(list({
            symptom 
            for disease in self.diseases.values() 
            for symptom in disease['symptoms']
        }))

    def show_symptom_suggestions(self):
        print("\nCommon Symptoms (you can mention any of these):")
        print("- " + "\n- ".join(self.all_symptoms[:20]))  # Show first 20
        if len(self.all_symptoms) > 20:
            print("\n... and {} more symptoms".format(len(self.all_symptoms)-20))
        print("\nYou can say things like: 'I have fever and headache' or 'nausea, vomiting, diarrhea'")

    def extract_symptoms(self, user_input):
        cleaned = user_input.lower()
        for word in ["i have", "i'm experiencing", "symptoms include", "and"]:
            cleaned = cleaned.replace(word, ",")
        
        potential = [s.strip() for s in cleaned.split(",") if s.strip()]
        
        confirmed = []
        for symptom in potential:
            # Exact match
            if symptom in self.all_symptoms:
                confirmed.append(symptom)
                continue
            
            # Partial match
            for known_symptom in self.all_symptoms:
                if symptom in known_symptom or known_symptom in symptom:
                    confirmed.append(known_symptom)
                    break
        
        return list(set(confirmed))

    def start(self):
        print("\n" + "="*60)
        print("MEDICAL DIAGNOSIS CHATBOT (EDUCATIONAL PURPOSES ONLY)")
        print("="*60)
        print("\nThis chatbot knows about {} diseases across all major categories.".format(len(self.diseases)))
        print("It recognizes {} distinct symptoms.".format(len(self.all_symptoms)))
        
        self.show_symptom_suggestions()
        
        while True:
            user_input = input("\nDescribe your symptoms (or 'quit'): ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nRemember: This is for educational purposes only. Consult a real doctor for medical advice.")
                break
                
            symptoms = self.extract_symptoms(user_input)
            
            if not symptoms:
                print("\nI didn't recognize those symptoms. Try phrases like:")
                print("'headache and fever' or 'nausea, vomiting, diarrhea'")
                self.show_symptom_suggestions()
                continue
                
            print("\nAnalyzing: " + ", ".join(symptoms))
            
            # Find matching conditions
            matches = []
            for name, data in self.diseases.items():
                overlap = set(symptoms) & set(data['symptoms'])
                if overlap:
                    score = len(overlap) / len(data['symptoms'])
                    matches.append((name, data, len(overlap), score))
            
            if not matches:
                print("\nNo matching conditions found. Try describing different symptoms.")
                continue
                
            # Sort by best match
            matches.sort(key=lambda x: (-x[2], -x[3]))
            
            print("\nPossible Conditions (by likelihood):")
            for i, (name, data, count, score) in enumerate(matches[:5], 1):
                matched = set(symptoms) & set(data['symptoms'])
                unmatched = set(data['symptoms']) - matched
                
                print(f"\n{i}. {name} ({data['category']}) - {count}/{len(data['symptoms'])} symptoms")
                print(f"   Matched: {', '.join(matched)}")
                if unmatched:
                    print(f"   Also common: {', '.join(unmatched)}")
                
            print("\nWould you like to check another set of symptoms? (yes/no)")
            if input("> ").lower().strip() in ['no', 'n']:
                print("\nRemember: This is for educational purposes only. Consult a real doctor for medical advice.")
                break

if __name__ == "__main__":
    bot = MedicalChatbot()
    bot.start()
