### Задания на программирование

- **Задание 1**

    Напишите функцию `double_print`, которая принимает строку и выводит ее на экран дважды.

    При передачи пустой строки, функция должна возбудить исключение `ValueError` с сообщением `empty string is not allowed`

    Пример работы программы:
    ```
    >>> double_print('Hello')
    Hello
    Hello
    ```
    
    ```
    >>> double_print('')
    Traceback (most recent call last):
    ...
    ValueError: empty string is not allowed
    ```

- **Задание 2**

    Напишите класс исключения `ParseError`, который будет являться наследником класса `Exception`.

    Снабдите созданный класс документ-строкой: `""" Error while parsing file """`.

    Конструктор класса `ParseError` должен принимать необязательные именованные аргументы `line_no` (номер строки) и `text` (текст, который вызвал ошибку).

    Опишите метод `__str__`, создающий сообщение об ошибке по следующей логике:
    - если не переданы ни номер строки, ни текст, вызывается стандартный метод `Exception`
    - если передан только номер строки, метод выдает `cannot parse text on line ...`
    - если передан только текст, метод выдает `cannot parse text: '...'"` (текст должен выглядеть так, как его выдает функция `repr`)
    - если переданы и номер строки, и текст, метод выдает: `cannot parse text on line ...: '...'`

    Пример работы программы:
    ```
    >>> raise ParseError('some standard message')
    Traceback (most recent call last):
    ...
    __main__.ParseError: some standard message
    
    >>> raise ParseError(line_no=10)
    Traceback (most recent call last):
    ...
    __main__.ParseError: cannot parse text on line 10
    
    >>> raise ParseError(text='abc')
    Traceback (most recent call last):
    __main__.ParseError: cannot parse text: 'abc'
    
    >>> raise ParseError(line_no=10, text='...')
    Traceback (most recent call last):
    ...
    __main__.ParseError: cannot parse text on line 10: '...'
    ```    

    **Пояснение**: любой класс исключения принимает произвольное число аргументов (в сигнатуре функции это выглядит как `*args`). Класс-наследник должен поддерживать весь интерфейс родителя, поэтому в вашем классе также должны быть `*args`, которые нужно передать выше по иерархии наследования с помощью функции super. Любые аргументы, указанные после аргумента со «звездочкой», можно передать только по имени, поэтому они называются именованными. Чтобы сделать их необязательными, нужно дать им значение по умолчанию.
