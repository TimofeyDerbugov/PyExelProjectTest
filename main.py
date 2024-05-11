import openpyxl

book = openpyxl.open("Книга (2).xlsx", read_only=True)

sheet = book.active

for row in range(2, sheet.max_row + 1):
    author = sheet[row][0].value
    name = sheet[row][1].value
    year = sheet[row][2].value
    rating = sheet[row][3].value




    if year >= 1720 and rating >= 3.7:
        print("Новая рекомендованная книга: ", author, name)
    elif year < 1720 and rating >= 3.7:
        print("Старая рекомендованная книга: ", author, name)
    elif year >= 1720 and rating < 3.7:
         print("Новая нерекомендованная книга: ", author, name)
    elif year < 1720 and rating < 3.7:
        print("Старая нерекомендованная книга: ", author, name)