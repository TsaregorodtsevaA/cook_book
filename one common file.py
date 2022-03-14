with open('Первый файл.txt', encoding='utf-8') as file_1:
    a = file_1.readlines()
    a_len = len(a)
with open('Первый файл.txt', encoding='utf-8') as file_1:
    a_text = file_1.read()
with open('Первый файл.txt', 'w', encoding='utf-8') as file_1:
    file_1.writelines('\nПервый файл.txt\n')
    file_1.write(f'{a_len}\n')
    file_1.write(f'{a_text}')
with open('Первый файл.txt', encoding='utf-8') as file_1:
    a_list = file_1.readlines()

with open('Второй файл.txt', encoding='utf-8') as file_2:
    b = file_2.readlines()
    b_len = len(b)
with open('Второй файл.txt', encoding='utf-8') as file_2:
    b_text = file_2.read()
with open('Второй файл.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines('\nВторой файл.txt\n')
    file_2.write(f'{b_len}\n')
    file_2.write(f'{b_text}')
with open('Второй файл.txt', encoding='utf-8') as file_2:
    b_list = file_2.readlines()

with open('Третий файл.txt', encoding='utf-8') as file_3:
    c = file_3.readlines()
    c_len = len(c)
with open('Третий файл.txt', encoding='utf-8') as file_3:
    c_text = file_3.read()
with open('Третий файл.txt', 'w', encoding='utf-8') as file_3:
    file_3.writelines('\nТретий файл.txt\n')
    file_3.write(f'{c_len}\n')
    file_3.write(f'{c_text}')
with open('Третий файл.txt', encoding='utf-8') as file_3:
    c_list = file_3.readlines()
common_list = []
common_list.append(a_list)
common_list.append(b_list)
common_list.append(c_list)
common_list.sort(key=len)
print(common_list)
for el in common_list:
    for el_1 in el:
        with open('Общий.txt', 'a', encoding='utf-8') as common_file:
            common_file.write(el_1)