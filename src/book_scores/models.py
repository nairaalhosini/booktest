class Book:
    def __init__(self, title, author, pages, rating, reviews, category):
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = rating
        self.reviews = reviews
        self.category = category


class ScoreResult:
    def __init__(self, name, score, grade, note):
        self.name = name
        self.score = score
        self.grade = grade
        self.note = note
