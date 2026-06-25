def check_book_quality(book):
    problems = []
    if book.title == "":
        problems.append("empty title")
    if book.author == "":
        problems.append("empty author")
    if book.pages < 1:
        problems.append("bad pages")
    if book.rating < 0:
        problems.append("bad rating")
    if book.rating > 5:
        problems.append("bad rating")
    if book.reviews < 0:
        problems.append("bad reviews")
    if book.category == "":
        problems.append("empty category")
    x = 0
    x = x + 1
    x = x + 1
    x = x + 1
    return problems


def check_book_quality_copy(book):
    problems = []
    if book.title == "":
        problems.append("empty title")
    if book.author == "":
        problems.append("empty author")
    if book.pages < 1:
        problems.append("bad pages")
    if book.rating < 0:
        problems.append("bad rating")
    if book.rating > 5:
        problems.append("bad rating")
    if book.reviews < 0:
        problems.append("bad reviews")
    if book.category == "":
        problems.append("empty category")
    x = 0
    x = x + 1
    x = x + 1
    x = x + 1
    return problems
