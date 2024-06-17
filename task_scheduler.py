import time

tasks = []
print('*' * 10, 'Планировщик задач', '*' * 10)
print('Привет, это планировщик задач!')
task_1 = input('Введите вашу 1 задачу: ')
print('Задача добавлена в список')
task_2 = input('Введите вашу 2 задачу: ')
print('Задача добавлена в список')
task_3 = input('Введите вашу 3 задачу: ')
print('Задача добавлена в список')
tasks.append(task_1)
tasks.append(task_2)
tasks.append(task_3)

while True:
    print()
    q = input('Чем могу помочь(добавить/удалить/показать список/очистить список) ')
    lower_q = q.lower()
    if lower_q == 'добавить':
        q1 = input("Какую зачаду добавить? ")
        tasks.append(q1)
        print('Задача добавлена в список!')
        time.sleep(1)
        print()
    
    elif lower_q == 'удалить':
        q2 = int(input('Какую задачу удалить?(по номеру) '))
        tasks.pop(q2-1)
        print('Задача удалена из списка!')
        print()
        time.sleep(1)
    
    elif lower_q == 'показать список':
        print(f'Задачи: \n{tasks}')
        print()
        time.sleep(1)
    
    elif lower_q == 'очистить список':
        q3 = input('Вы уверены, что хотите очистить список задач? ')
        if q3 == 'да':
            tasks = []
            print('Список задач очищен')
            print()
            time.sleep(1)

        elif q3 == 'нет':
            print('Команда отменена')
            print()
            time.sleep(1)

    else:
        print('Что вы имеете ввиду?\n')  