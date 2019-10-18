# stepik-3-6
Мы хотим, чтобы разрабатываемый нами интернет-магазин работал одинаково хорошо для пользователей из любой страны. Чтобы убедиться в работоспособности решения с поддержкой разных языков, мы планируем запускать набор автотестов для каждого языка. Вам как разработчику автотестов нужно реализовать решение, которое позволит запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.

Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.
Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.