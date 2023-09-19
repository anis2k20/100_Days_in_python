from whatsapp_number import num_list,name_list
with open("WhatsAppChat.txt", encoding="utf8") as messages:
    all_message = messages.read()
sum=0
for name in name_list:
    num_of_msg = all_message.count(name)
    sum +=num_of_msg
    if num_of_msg > 100:
        print(f"Total msg: {num_of_msg} Owner: {name}")

for num in num_list:
    num_of_msg = all_message.count(num)
    sum += num_of_msg
    if num_of_msg > 100:
        print(f"Total msg: {num_of_msg} Owner: {num}")

total_msg = all_message.count(" - ")
print(f"Total group message: {total_msg}")






