from question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]

def run_test(questions, result_list):
    score = 0
    ques_no = 1
    for ques in questions:
        print(ques.prompt)
        ans = input("Enter your answer: ")
        if ans == ques.ans:
            score += 1
            result_list.append('Ques ' + str(ques_no) + '--> correct ans: ' + ques.ans + ' ✓')
        else:
            result_list.append('Ques ' + str(ques_no) + '--> correct ans: ' + ques.ans + ' ✕')
        ques_no += 1
    return score

def show_result(result_list):
    for result in result_list:
        print(result)

result_list = []

score = run_test(questions, result_list)
print('Your Total score is:', score)
show_result(result_list)
