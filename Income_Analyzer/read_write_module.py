def read_Write_module(value,data):
    if value == 'r':
        db = open(r'.\databank.txt', mode = 'r', encoding = 'utf-8')
        mainMatrix = []
        for item in db:
            mainMatrix.append(item)
        db.close()
        return mainMatrix

    if value == 'a':
        db = open(r'databank.txt', mode = 'a', encoding = 'utf-8')
