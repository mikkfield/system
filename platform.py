class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)

    def view_posts(self):
        if not self.posts:
            print(f"{self.username} has no posts yet.")
        else:
            print(f"Posts by {self.username}:")
            for post in self.posts:
                print(f"{post.content} ({post.timestamp})")

class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.timestamp = datetime.datetime.now()

class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        user = next((u for u in self.users if u.username == username), None)
        if user and user.password == password
