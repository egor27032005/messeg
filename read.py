def read_file_to_dict():
    result_dict = {}

    with open("users.txt", 'r') as file:
        for line in file:
            line = line.strip()  # Удаляем лишние пробелы и символы переноса строки
            if line:  # Проверяем, что строка не пустая
                parts = line.split(' ', 1)  # Разделяем только на два элемента по первому пробелу
                if len(parts) == 2:  # Убедимся, что есть и ключ, и значение
                    key, value = parts[0], parts[1]
                    result_dict[key] = value

    return result_dict
def write_users(us):
    with open("users.txt", 'w') as file:
        for key, value in us.items():
            file.write(f'{key} {value}\n')




def read_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if lines and lines[0].strip() == '':
            lines = lines[1:]
    return [line.strip() for line in lines]

def write_file(filename,text):
    file=open(filename, 'a')
    file.write("\n"+text)
    file.close()
