from csv import reader

#Task 1
count_long_titles = 0
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[2]) > 30: 
            count_long_titles += 1

print(f'Количество записей с названием длиннее 30 символов: {count_long_titles}')

#Task 2
while True:
    flag = 0
    search = input('Введите автора для поиска: ')
    if search == '0':
        break
    
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            lower_case = row[1].lower()
            index = lower_case.find(search.lower())
            if index != -1:
                print(row[2])  
                flag += 1
                if flag >= 5:
                    print('Достигнуто ограничение на выдачу (5 результатов)')
                    break
        
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')

# task 3
bibliography = []
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for i, row in enumerate(table):
        if i >= 20:  
            break
        reference = f"{row[1]}. {row[2]} - {row[3]}"
        bibliography.append(reference)

with open('result.txt', 'w', encoding='utf-8') as output:
    for i, ref in enumerate(bibliography, 1):
        output.write(f"{i}. {ref}\n")

print("Библиографические ссылки сохранены в файл 'result.txt'")
