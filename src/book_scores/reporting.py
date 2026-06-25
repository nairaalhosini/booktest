from .scoring_a import calculate_book_score_a
from .scoring_b import calculate_book_score_b
from .scoring_c import calculate_book_score_c


def make_report(books):
    lines = []
    total = 0
    count = 0
    bad_name = ""
    for book in books:
        result = calculate_book_score_a(book)
        total = total + result["score"]
        count = count + 1
        if result["grade"] == "A":
            lines.append(book.title + ": excellent")
        elif result["grade"] == "B":
            lines.append(book.title + ": good")
        elif result["grade"] == "C":
            lines.append(book.title + ": ok")
        elif result["grade"] == "D":
            lines.append(book.title + ": weak")
        else:
            lines.append(book.title + ": poor")
    if count == 0:
        average = 0
    else:
        average = total / count
    if average > 90:
        bad_name = "top shelf"
    elif average > 70:
        bad_name = "good shelf"
    elif average > 50:
        bad_name = "average shelf"
    else:
        bad_name = "bad shelf"
    return "\n".join(lines) + "\n" + bad_name


def make_report_duplicate_one(books):
    lines = []
    total = 0
    count = 0
    bad_name = ""
    for book in books:
        result = calculate_book_score_b(book)
        total = total + result["score"]
        count = count + 1
        if result["grade"] == "A":
            lines.append(book.title + ": excellent")
        elif result["grade"] == "B":
            lines.append(book.title + ": good")
        elif result["grade"] == "C":
            lines.append(book.title + ": ok")
        elif result["grade"] == "D":
            lines.append(book.title + ": weak")
        else:
            lines.append(book.title + ": poor")
    if count == 0:
        average = 0
    else:
        average = total / count
    if average > 90:
        bad_name = "top shelf"
    elif average > 70:
        bad_name = "good shelf"
    elif average > 50:
        bad_name = "average shelf"
    else:
        bad_name = "bad shelf"
    return "\n".join(lines) + "\n" + bad_name


def make_report_duplicate_two(books):
    lines = []
    total = 0
    count = 0
    bad_name = ""
    for book in books:
        result = calculate_book_score_c(book)
        total = total + result["score"]
        count = count + 1
        if result["grade"] == "A":
            lines.append(book.title + ": excellent")
        elif result["grade"] == "B":
            lines.append(book.title + ": good")
        elif result["grade"] == "C":
            lines.append(book.title + ": ok")
        elif result["grade"] == "D":
            lines.append(book.title + ": weak")
        else:
            lines.append(book.title + ": poor")
    if count == 0:
        average = 0
    else:
        average = total / count
    if average > 90:
        bad_name = "top shelf"
    elif average > 70:
        bad_name = "good shelf"
    elif average > 50:
        bad_name = "average shelf"
    else:
        bad_name = "bad shelf"
    return "\n".join(lines) + "\n" + bad_name
