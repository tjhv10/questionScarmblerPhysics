import random

def read_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    questions = []
    question = None
    answers = []
    i = 0
    for line in lines:
        line = line.strip()
        if not line:
            i += 1
            continue
        if line.startswith('[q'):
            if question is not None:
                questions.append((question_num, question, answers))
            question_num = line.split(']', 1)[0][2:]  # Extract the question number
            question = lines[i + 1].strip()
            answers = []
        elif line.startswith('[a]'):
            i += 1
            continue
        else:
            if '?' not in line:
                answers.append(line)
        i += 1
    
    if question is not None and answers:
        questions.append((question_num, question, answers))
    
    return questions

def scramble_questions(questions, num_questions=20):
    selected_questions = random.sample(questions, num_questions)
    scrambled_questions = []
    
    for question_num, question, answers in selected_questions:
        scrambled_answers = random.sample(answers, len(answers))
        scrambled_questions.append((question_num, question, scrambled_answers))
    
    return scrambled_questions

def write_scrambled_questions(filename, scrambled_questions):    
    with open(filename, 'w', encoding='utf-8') as file:
        for question_num, question, answers in scrambled_questions:
            file.write(f"{question_num}. {question}\n")
            for j, answer in enumerate(answers):
                file.write(f"{answer} ({j+1}\n")
            file.write("\n")

            
write_scrambled_questions('scrambled_questions.txt', scramble_questions(read_questions('questions.txt')))
