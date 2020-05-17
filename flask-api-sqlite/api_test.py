import unittest
import requests

# def addTwoNumbers(a, b):
#     return a + b
# class AddTest(unittest.TestCase):
#     def test1(self):
#         c = addTwoNumbers(5, 10)  # 15
#         self.assertEqual(c, 15)

#     def test2(self):
#         c = addTwoNumbers(5, 10)
#         self.assertNotEqual(c, 10)

# if __name__ == '__main__':
#     unittest.main()


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    BOOKS_URL = "{}/books".format(API_URL)
    BOOK_OBJ = {
        "book_id": 3,
        "name": "Harry Potter and Philosopher Stone",
        "author": "J. K. Rowling"
    }

    NEW_BOOK_OBJ = {
        "book_id": 3,
        "name": "The Alchemist",
        "author": "Paulo Coelho"
    }

    def _get_each_book_url(self, book_id):
        return "{}/{}".format(ApiTest.BOOKS_URL, book_id)

    # GET request to /api/books returns the details of all books
    def test_1_get_all_books(self):
        r = requests.get(ApiTest.BOOKS_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 2)

    # POST request to /api/books to create a new book
    def test_2_add_new_book(self):
        r = requests.post(ApiTest.BOOKS_URL, json=ApiTest.BOOK_OBJ)
        self.assertEqual(r.status_code, 201)

    def test_3_get_new_book(self):
        book_id = 3
        r = requests.get(self._get_each_book_url(book_id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.BOOK_OBJ)

    # PUT request to /api/books/book_id
    def test_4_update_existing_book(self):
        book_id = 3
        r = requests.put(self._get_each_book_url(book_id),
                         json=ApiTest.NEW_BOOK_OBJ)
        self.assertEqual(r.status_code, 204)

    # GET request to /api/books/book_id
    def test_5_get_new_book_after_update(self):
        book_id = 3
        r = requests.get(self._get_each_book_url(book_id))
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), ApiTest.NEW_BOOK_OBJ)

    # DELETE request to /api/books/book_id
    def test_6_delete_book(self):
        book_id = 3
        r = requests.delete(self._get_each_book_url(book_id))
        self.assertEqual(r.status_code, 204)

    @unittest.expectedFailure
    def test_7_get_new_book_after_delete(self):
        book_id = 3
        r = requests.get(self._get_each_book_url(book_id))
        self.assertEqual(r.status_code, 200)
