from book_scores.models import Book
from book_scores.scoring_a import calculate_book_score_a


def test_score_basic():
    book = Book("Clean Code", "Author", 350, 4.7, 6000, "business")
    result = calculate_book_score_a(book)
    assert result["grade"] in ["A", "B", "C", "D", "F"]
