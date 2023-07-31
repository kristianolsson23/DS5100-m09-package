import pandas as pd

class BookLover:
    
    # constructor
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list

    #method 1
    def add_book(self, book_name, rating):
        if self.book_list['book_name'].isin([book_name]).any():
        #if book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the booklist.")
        
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]})
        
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    
    #method 2
    def has_read(self, book_name):
        if not self.book_list[self.book_list['book_name'] == book_name].empty:
            print(f"You have already read {book_name}.")
            return True
        else:
            print(f"You have not read {book_name} yet.")
            return False
        
      
    #method 3
    def num_books_read(self):
        print(f"The length of your booklist is {len(self.book_list)}.")
        return len(self.book_list)

    
    #method 4
    def fav_books(self):
        print(f"Your favorite books with >3 ratings are {list(self.book_list['book_name'][self.book_list['book_rating'] > 3])}.")
        return self.book_list[self.book_list['book_rating'] > 3]