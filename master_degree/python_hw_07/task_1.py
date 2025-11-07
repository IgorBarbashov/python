import requests

url = "https://jsonplaceholder.typicode.com/posts"
post_number = 5


def get_posts(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Failed to retrieve posts. Status code: {response.status_code}")


def print_posts(posts, post_number):
    for post in posts[:post_number]:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")


if __name__ == "__main__":
    posts = get_posts(url)
    print_posts(posts, post_number)
