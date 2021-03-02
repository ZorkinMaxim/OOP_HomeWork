class User:
    def __init__(self, nickname, rating=5, friends=0, posts=0, comments=0):
        self.nickname = nickname
        self.rating = rating
        self.friends = friends
        self.posts = posts
        self.comments = comments
        if self.reglament_rating():
            self.rating = 0
        if self.reglament_friends():
            self.friends = 0
        if self.reglament_posts():
            self.posts = 0
        if self.reglament_comments():
            self.comments = 0

    def __str__(self):
        return f"{self.nickname:>12} {self.rating:4} {self.friends:3} {self.posts:3} {self.comments:3}"

    def like(self):
        if self.like_ratingOK():
            self.rating += 0.5

    def dislike(self):
        if self.dislike_ratingOK():
            self.rating -= 0.5

    def like_ratingOK(self):
        return self.rating <= 4.5

    def dislike_ratingOK(self):
        return self.rating >= 0.5

    def reglament_rating(self):
        return self.rating < 0

    def reglament_friends(self):
        return self.friends < 0

    def reglament_posts(self):
        return self.posts < 0

    def reglament_comments(self):
        return self.comments < 0


###############################################################
users = []
users.append(User("Mary", 3))
users.append(User("Jonh", 5))
users.append(User("Kate", 4.5))

users[0].like()
users[2].dislike()

# for i in range(len(users)):
#     print(users[i])
for u in users:
    print(u)
