from core import NoteService

def getKey():
    year = input('Введите год заметки: ')
    month = input('Введите месяц заметки: ')
    day = input('Введите день заметки: ')
    return year + '-' + month + '-' + day

if __name__ == '__main__':
    run = True
    ns = NoteService()
    while run:
        choose = input('Выберите действие:\n'
                       '\t1 - Создать заметку\n'
                       '\t2 - Просмотреть заметку\n'
                       '\t3 - Изменить заметку\n'
                       '\t4 - Удалить заметку\n'
                       '\t0 - Выход\n'
                       '>>> ')
        if choose == '1':
            ns.addNote()
        elif choose == '2':
            key = getKey()
            ns.getNote(key)
        elif choose == '3':
            key = getKey()
            ns.editNote(key)
        elif choose == '4':
            key = getKey()
            ns.delNote(key)
        elif key == '0':
            print('До свидания')
            run = False
        else:
            print('Неизвестная команда')
