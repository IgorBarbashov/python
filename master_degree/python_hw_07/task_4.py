import requests

url = "https://jsonplaceholder.typicode.com/posts"


def create_post(url, post):
    response = requests.post(url, json=post)

    if response.status_code == 201:
        created_post = response.json()
        return created_post

    elif response.status_code == 400:
        raise Exception(
            f"Ошибка 400 (Bad Request): Некорректные данные запроса."
        )

    elif response.status_code == 404:
        raise Exception(
            f"Ошибка 404 (Not Found): Ресурс не найден."
        )

    else:
        raise Exception(
            f"Ошибка при создании поста. Статус: {response.status_code}"
        )


def print_post(post):
    print(f"\nПост успешно создан!")
    print(f"ID созданного поста: {post['id']}")
    print(f"\nСодержимое поста:")
    print(f"  Заголовок: {post['title']}")
    print(f"  Текст: {post['body']}")
    print(f"  User ID: {post['userId']}\n")


if __name__ == "__main__":
    post = {
        'title': 'Мой первый пост',
        'body': 'Это содержимое моего первого поста через API',
        'userId': 1
    }

    try:
        created_post = create_post(url, post)
        print_post(created_post)

    except Exception as err:
        print(err)
