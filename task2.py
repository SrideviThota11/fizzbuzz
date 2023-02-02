#task 2 - part1
book = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book1.txt", 'r')
def unique_words(book):
    text = book.read()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    unique_words = []
    for word in words:
        if(word not in unique_words):
         unique_words.append(word)
    print(unique_words)     
    return unique_words       
unique_words(book)

#task 2 - part2
def count_the_article():
    list = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    #print(len(list))
    return len(list)
count_the_article()

#task 2 - part3
book = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\\20k.txt", 'r')
def sorted_words(book):
    text = book.read()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    sorted_words = []
    for word in words:
         word = word.lower()
         sorted_words.append(word)
    sorted_words.sort(key = len, reverse = True) 
    print(sorted_words)
    return sorted_words    
sorted_words(book)

#task 2 - part4
book = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book1.txt", 'r')
dict = dict()
def character_word_count(book):
    text = book.read()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    for word in words:
        dict[word] = len(word) 
    print(dict)  
    return dict     
character_word_count(book)     
       
#task 2 - part5
book1 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book1.txt", 'r', encoding='UTF-8')
book2 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book2.txt", 'r', encoding='UTF-8')
book3 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book3.txt", 'r', encoding='UTF-8')
def starts_with_vow(book):
   tuple =  ("a", "e", "i", "o", "u")     
   text = book.read()
   words = text.split()
   words = [word.strip('.,!;()[]') for word in words]
   count = 0
   for word in words:
       for vowel in tuple :   
            if(word.startswith(vowel)):
              count = count+1
   #print(count)
   return count
starts_with_vow(book1)
starts_with_vow(book2)
starts_with_vow(book3)

#task 2 - part6
book1 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book1.txt", 'r', encoding='UTF-8')
book2 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book2.txt", 'r', encoding='UTF-8')
book3 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book3.txt", 'r', encoding='UTF-8')
reference = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\\20k.txt", 'r')
def formatBookList(reference):
   text = reference.read()
   words = text.split()
   ref_book_list = []
   for word in words:
       ref_book_list.append(word)
   return ref_book_list
def rare_words(book,reference):
    refBooklist = formatBookList(reference)
    text = book.read()
    words = text.split()
    words = [word.strip('.,!;()[]:?"') for word in words]
    rare_words = []
    for word in words :
        word = word.lower()
        if(word not in refBooklist):
            rare_words.append(word)
    print(rare_words)    
    return rare_words    
rare_words(book1,reference)
rare_words(book2,reference)
rare_words(book3,reference)

#task 2 - part7
book1 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book1.txt", 'r', encoding='UTF-8')
book2 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book2.txt", 'r', encoding='UTF-8')
book3 = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\Book3.txt", 'r', encoding='UTF-8')
reference = open("C:\Users\DELL\Desktop\Midterm Exam\openbook1-Sr443603\\20k.txt", 'r')
def formatBookList(book):
   text = book.read()
   words = text.split()
   words = [word.strip('.,!;()[]:?"') for word in words]
   book_list = []
   for word in words:
       word = word.lower()
       book_list.append(word)
   return book_list
def unused_word(book1,book2,book3,reference):
    book_list1 = formatBookList(book1)
    book_list2 = formatBookList(book2)
    book_list3 = formatBookList(book3)
    text = reference.read()
    words = text.split()
    unused_words = []
    word_count = 0
    for word in words:
        if(word not in book_list1):
            if(word not in book_list2):
                if(word not in book_list3):
                    unused_words.append(word)
                    word_count = word_count+1
    print(word_count)
    return unused_words
unused_word(book1,book2,book3,reference)