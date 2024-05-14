# Finding Items in a File

largest = 0
scripture_choice = input('\nWhich volume of scriptures would you like to learn about? ')

with open('Week12/books_and_chapters.txt') as file:
    for line in file:
        parts = line.strip().split(':')

        book = [parts[0]]
        chapter = [int(parts[1])]
        scripture = [parts[2]]

        for i in range(len(scripture)):
            if scripture_choice.lower() == scripture[i].lower():
                for i in range(len(chapter)):
                    large_chapter = chapter[i]
                    large_book = book[i]
                    if largest < large_chapter:
                        largest = large_chapter
                        largest_book = large_book

    print(f'Largest Number of Chapters: {largest} - Book: {largest_book}\n')
        # print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
        