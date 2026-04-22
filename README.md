# qa_python
Удалось реализовать тесты :
1. test_add_new_book_name_one_and_forty_length_added проверяет добавление книг с максимальной и минимальтной длиной названия ( 1 и 40)
2. test_add_new_book_name_zero_and_forty_one_length_not_added проверяет, что в список не добавляются книги с невалидной длиной названия ( 0 и 41)
3. test_add_new_book_no_genre_initially проверяет, что у добавленной книги жанр изначально пустой
4. test_set_book_genre_existing_genre_is_set проверяет, что фильму можно присвоить жанр из списка
5. test_set_book_genre_not_in_list проверяет, что фильму нельзя присвоить жанр, которого нет в списке
6. test_get_books_for_children_excludes_age_rating проверяет, что книг с возрастным рейтингом нет в списке для детей
7. test_get_books_with_specific_genre_returns_correct_book проверяет, что можно получить список книг по конкретному жанру
8. test_add_book_in_favorites_added_successfully проверяет, что книга добавляется в список избранного
9. test_add_book_in_favorites_not_in_collection проверяет, что книгку нельзя добавить в избранное, если ее нет в коллекции
10. test_delete_book_from_favorites проверяет, что книга удаляется из избранного
11. test_get_list_of_favorites_books_return_correct_list проверяет, что при вызове списка Избранного мы получаем список, с ранее добавленными туда книгами
