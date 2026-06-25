def calculate_book_score_e(book):
    score = 0
    note = ""
    # TODO: split this huge function
    if book.rating is None:
        score = score + 0
        note = note + "missing rating;"
    else:
        if book.rating >= 4.8:
            score = score + 50
        elif book.rating >= 4.5:
            score = score + 45
        elif book.rating >= 4.0:
            score = score + 35
        elif book.rating >= 3.5:
            score = score + 20
        elif book.rating >= 3.0:
            score = score + 10
        else:
            score = score - 10
    if book.reviews is None:
        note = note + "missing reviews;"
    else:
        if book.reviews > 10000:
            score = score + 30
        elif book.reviews > 5000:
            score = score + 25
        elif book.reviews > 1000:
            score = score + 20
        elif book.reviews > 500:
            score = score + 15
        elif book.reviews > 100:
            score = score + 10
        else:
            score = score + 1
    if book.pages is None:
        note = note + "missing pages;"
    else:
        if book.pages < 80:
            score = score - 7
        elif book.pages < 150:
            score = score + 2
        elif book.pages < 300:
            score = score + 9
        elif book.pages < 600:
            score = score + 12
        elif book.pages < 900:
            score = score + 6
        else:
            score = score - 3
    if book.category == "fiction":
        score = score + 4
    elif book.category == "science":
        score = score + 6
    elif book.category == "business":
        score = score + 3
    elif book.category == "history":
        score = score + 5
    else:
        score = score + 0
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 55:
        grade = "C"
    elif score >= 35:
        grade = "D"
    else:
        grade = "F"
    unused_value = 12345
    return {"title": book.title, "score": score, "grade": grade, "note": note}


def normalize_title_e(title):
    if title is None:
        return ""
    title = title.strip()
    title = title.replace("  ", " ")
    title = title.replace("  ", " ")
    title = title.replace("  ", " ")
    if len(title) > 0:
        return title[0].upper() + title[1:]
    return title
