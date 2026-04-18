import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self) -> None:
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', [ 'A', 'Б' * 40 ])
    def test_add_new_book_name_one_and_forty_length_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [ '', 'В' * 41 ])
    def test_add_new_book_name_zero_and_forty_one_length_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_no_genre_initially(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    def test_set_book_genre_existing_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Зелёная миля')
        collector.set_book_genre('Зелёная миля', 'Фэнтези')
        assert collector.get_book_genre('Зелёная миля') == ''

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_excludes_age_rating(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Запретная книга')
        collector.set_book_genre('Запретная книга', genre)
        assert 'Взрослая книга' not in collector.get_books_for_children()

    def test_get_books_with_specific_genre_returns_correct_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_add_book_in_favorites_added_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_collection(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Лучшая книга')
        assert 'Лучшая книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_return_correct_list(self):
        collector = BooksCollector()
    
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        favorites = collector.get_list_of_favorites_books()
    
        assert len(favorites) == 1
        assert 'Дюна' in favorites

   
