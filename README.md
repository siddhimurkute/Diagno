
# Diagno - Medical Diagnosis Chatbot (Educational)

![Medical Chatbot](https://img.shields.io/badge/Medical-Education-blue) 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

Diagno is an **educational** AI chatbot that helps users explore possible medical conditions based on symptoms. It contains knowledge of 100+ diseases across all major medical categories.

**Disclaimer:** This is for educational purposes only. Never use this for actual medical diagnosis.

## Features

- 🩺 **Comprehensive Knowledge Base**: 127 diseases across 8 medical categories
- 🔍 **Symptom Analysis**: Recognizes 483 distinct symptoms
- 📊 **Probability Scoring**: Ranks conditions by symptom matches
- 📚 **Educational Focus**: Shows related symptoms and categories
- 💬 **Natural Language Processing**: Understands conversational input

## Medical Categories Covered

1. Respiratory (15 conditions)
2. Gastrointestinal (15 conditions)
3. Neurological (15 conditions)
4. Cardiovascular (15 conditions)
5. Dermatological (15 conditions)
6. Endocrine (10 conditions)
7. Musculoskeletal (15 conditions)
8. Infectious Diseases (15 conditions)

## Installation

```bash
git clone https://github.com/yourusername/diagno.git
cd diagno
python diagno.py
```

## Usage

1. Describe your symptoms when prompted:
   ```
   I have fever, cough and headache
   ```
2. The chatbot will analyze and show possible conditions
3. Review matched and common symptoms for each condition
4. Get educational information about each disease

## Example Session

```plaintext
MEDICAL DIAGNOSIS CHATBOT (EDUCATIONAL PURPOSES ONLY)
=====================================================

Describe your symptoms: I have fever, stiff neck and headache

Analyzing: fever, stiff neck, headache

Possible Conditions:
1. Meningitis (Neurological) - 3/4 symptoms matched
   • Matched: fever, stiff neck, headache
   • Also common: confusion

2. Influenza (Respiratory) - 2/7 symptoms matched
   • Matched: fever, headache
   • Also common: chills, muscle aches...
```

## Code Structure

```
diagno/
├── diagno.py            # Main chatbot implementation
├── README.md            # This documentation
├── requirements.txt     # Python dependencies
└── examples/            # Sample interaction logs
```

## Dependencies

- Python 3.8+
- No external libraries required

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

---

**Important:** This chatbot is for educational use only. Always consult a qualified healthcare professional for medical advice.
```

This README includes:

1. Professional Badges: For quick visual identification
2. Clear Disclaimer: Prominent educational use notice
3. Comprehensive Features: Highlighting key capabilities
4. Structured Installation/Usage: With code blocks
5. Visual Example: Showing typical interaction
6. Project Organization: Clear code structure
7. Contribution Guidelines: For open-source development
