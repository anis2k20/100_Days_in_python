with open("all_chap_question.txt","r",encoding='utf-8') as file:
    all_ques = file.readlines()

# ques_dict = {
#     "chap_01":{
#         "1":"question 1",
#         "2": "question 2".
#         ..................
#         ..................
#     },
#     "chap_02":{
#         "1":"question 1",
#         "2": "question 2".
#         ..................
#         ..................
#     }
# }
ques_dict = {}
k=0
for ques in all_ques:
    ques_dict[k]=ques[3:].strip()
    k += 1

for q in ques_dict.items():
