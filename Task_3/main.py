with open('Task_3/file1.txt', encoding='utf-8') as file1:
    file1_content = file1.readlines()
    file1_name = 'Файл 1'
    file1_number = 1
    file1_info ={"len": len(file1_content), "name": file1_name, "number": file1_number, "content": file1_content}
    
with open('Task_3/file2.txt', encoding='utf-8') as file2:
    file2_content = file2.readlines()
    file2_name = 'Файл 2'
    file2_number = 2
    file2_info ={"len": len(file2_content), "name": file2_name, "number": file2_number, "content": file2_content}

with open('Task_3/file3.txt', encoding='utf-8') as file3:
    file3_content = file3.readlines() 
    file3_name = 'Файл 3'
    file3_number = 3
    file3_info ={"len": len(file3_content), "name": file3_name, "number": file3_number, "content": file3_content}

result_info = [file1_info, file2_info, file3_info]

sorted_info = sorted(result_info, key=lambda x:x["len"])


with open('Task_3/summary.txt', 'w', encoding='utf-8') as summary:
    for fragment in sorted_info:
        summary.writelines(fragment.get("name"))
        summary.writelines("\n")
        summary.writelines(str(fragment.get("len")))
        summary.writelines("\n")
        id = fragment.get("number")
        for index, string in enumerate(fragment.get("content")):
            x = str(f'Строка {index + 1} файла номер {id} {string}')
            summary.writelines(x)  
        summary.writelines("\n")


with open('Task_3/summary.txt', 'r', encoding='utf-8') as summary:
     full_text = summary.read()
     print(full_text)


