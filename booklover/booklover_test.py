import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover1 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover1.add_book('Diary of the Wimpy Kid', 4.)
        expected = pd.DataFrame({'book_name': ['Diary of the Wimpy Kid'], 'book_rating': [4.0]})
        self.assertEqual(list(booklover1.book_list.all()), list(expected.all()))


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover2 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover2.add_book('Diary of the Wimpy Kid', 4.)
        booklover2.add_book('Diary of the Wimpy Kid', 2.)
        self.assertEqual(booklover2.num_books, 1.)      
        
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover3 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover3.add_book('Diary of the Wimpy Kid', 4.)
        self.assertTrue(booklover3.has_read('Diary of the Wimpy Kid'))

        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover4 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover4.add_book('Diary of the Wimpy Kid', 4.)
        self.assertFalse(booklover4.has_read('The Big Short'))

        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklover5 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover5.add_book('Diary of the Wimpy Kid', 4.)
        booklover5.add_book('The Big Short', 3.)
        booklover5.add_book('Death Note', 5.)
        booklover5.add_book('The Man From Beijing', 5.)
        self.assertEqual(booklover5.num_books_read(),4.)


    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover6 = BookLover('Kristian', 'kno5cac@virginia.edu', 'Thriller')
        booklover6.add_book('Diary of the Wimpy Kid', 1)
        booklover6.add_book('The Big Short', 3)
        booklover6.add_book('Death Note', 4)
        booklover6.add_book('The Man From Beijing', 5)
        booklover6_fav_books = booklover6.fav_books()
        expected = pd.DataFrame({'book_name': ['Death Note', 'The Man From Beijing'], 'book_rating': [4,5]})
        self.assertEqual(list(booklover6_fav_books['book_name']),['Death Note', 'The Man From Beijing'])
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)