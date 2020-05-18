'''
1. Create a MongoDB Atlas Database - Done
2. Connect to the database - Done
3. Define a Book Document Collection
4. Create a new book document and add it to collection
5. Fetch the document
6. Update the document
7. Run queries on the Collection
8. Delete document
'''

import mongoengine as db
from api_constants import mongo_password

database_name = "quickstart"
password = mongo_password
DB_URI = "mongodb+srv://rahularora:{}@pythoncluster-n0fjw.azure.mongodb.net/{}?retryWrites=true&w=majority".format(
    mongo_password, database_name)
db.connect(host=DB_URI)

# Define a Book Document Collection


class Book(db.Document):
    book_id = db.IntField()
    name = db.StringField()
    author = db.StringField()

    def to_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author
        }


print("\nCreate a Book")
book = Book(
    book_id=1,
    name="A Game of Thrones",
    author="George R.R. Martin"
)
book.save()

print("\nFetch a book")
book = Book.objects(book_id=1).first()
# print(book.to_json())

print("\nUpdate a book")
book.update(name="Harry Potter",
            author="J.K. Rowling")
print(book.to_json())

print("\nAdd another Book")
book = Book(book_id=2,
            name="The Alchemist",
            author="Paulo Coelho")
book.save()

print("\nFetch all books")
books = []
for book in Book.objects():
    books.append(book.to_json())
print(books)

print("\nFind books whose name contains The")
books = []
for book in Book.objects(name__contains='The'):
    books.append(book.to_json())
print(books)

print("\nHow many books are in a collection?")
print(Book.objects.count())

print("\nOrder by author field")
books = []
for book in Book.objects().order_by('author'):
    books.append(book.to_json())
print(books)

print("\nDelete a book")
book = Book.objects(book_id=2).first()
book.delete()
print(Book.objects.count())

print("\nDelete all books in a collection")
for book in Book.objects():
    book.delete()
print(Book.objects.count())  # 0
