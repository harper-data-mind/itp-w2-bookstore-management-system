def create_bookstore(name):
    return {
        'name': name,
        'authors': [],
        'books' : []
    }


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality' : nationality,
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    res = {}
    for author in bookstore['authors']:
        if author['name'] == name:
            res= author
    return res


def add_book(bookstore, title, isbn, author):
    book = {
        'title' : title,
        'isbn' : isbn,
        'author' : author
    }
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    res = {}
    for book in bookstore['books']:
        if book['title'] == title:
            res = book
    return res


def get_books_by_author(bookstore, author):
    res = []
    for book in bookstore['books']:
        if book['author'] == author:
            res.append(book)
    return res