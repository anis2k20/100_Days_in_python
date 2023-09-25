with open("all_chap_question.txt","r",encoding='utf-8') as file:
    all_chap_ques = file.readlines()

ques_dict = {}

for ques in all_chap_ques:
    key=ques[:3]
    val=ques[3:]
    ques_dict[key]=val

print(ques_dict)