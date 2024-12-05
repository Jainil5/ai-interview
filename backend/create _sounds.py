import os
from gtts import gTTS

# List of text inputs (questions in this case)
questions = [
    "In which university do you want to study?",
    "Why do you want to study in this university?",
    "What course do you want to do in this university?",
    "What benefits will you get by doing this course?",
    "What do you know more about your university?",
    "Where exactly do you want to go in the US?",
    "Apart from this, in which other universities have you applied?",
    "How many admits and rejections?",
    "From where did you get the rejection?",
    "What are the reasons for rejection?",
    "Why have you not given GRE, GMAT, or SAT?",
    "Why do you want to study in the US?",
    "Why only US, not any other country?",
    "Why do you want to do a master's?",
    "Why do you want to do a bachelor's?",
    "Why do you want to do a master's from the USA?",
    "Why do you want to pursue this course?",
    "What is your course curriculum?",
    "What is the difference between course curriculums in India and the US?",
    "What is the scope of your field in India?",
    "What kind of job will you find after the completion of the course?",
    "What salary are you expecting after the completion of the course?",
    "Have you connected with any professor of this university?",
    "What is your future plan after a master's?",
    "Will you work in the USA if you get an opportunity - part-time or full-time?",
    "What is the guarantee that you will come back?",
    "What is the tuition fee for your course?",
    "What is your expected living expense?",
    "What is the total expense?",
    "Who is sponsoring you?",
    "What exactly is your father doing?",
    "How many people work under your father?",
    "How is your sponsor going to fund you?",
    "Which consultancy helped you in filing your visa?",
    "Who helped you in filling your DS-160 form?",
    "Why is your IELTS score low?",
    "What subjects did you study in your bachelor's?",
    "Normally students prefer fall intake. Why do you want to go in spring intake?",
    "Which research facilities are available in your university?",
    "How can your job help you in your studies?",
    "Why do you want to leave your job?",
    "Do you know anybody there?",
    "Will you work on CPT in any good company?",
    "What if I dont give you a visa?",
    "Who said the US is the best?",
    "How did you learn about this university?",
    "Have you done any case study?"
]

# Folder to save audio files
output_folder = "backend/audio_files"
os.makedirs(output_folder, exist_ok=True)

# Generate audio files for each question
for i, question in enumerate(questions, 1):
    filename = os.path.join(output_folder, f"question_{i}.mp3")
    tts = gTTS(text=question, lang='en')
    tts.save(filename)
    print(f"Saved: {filename}")

print(f"All audio files are saved in the '{output_folder}' folder.")