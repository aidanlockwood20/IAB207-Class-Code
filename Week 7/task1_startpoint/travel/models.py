class Destination:
    def __init__(self, name, description, img, currency):
        self.name = name
        self.description = description
        self.img = img
        self.currency = currency
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

class Comment:
    def __init__(self, user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at