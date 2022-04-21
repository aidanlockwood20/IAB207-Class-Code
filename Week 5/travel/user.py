class User:
    def __init__(self):
        self.user_type = 'guest'

    def register(self, username, password, emailID):
        self.username = username
        self.password = password
        self.emailID = emailID

    def __repr__(self):
        s = '{0}\nEmail: {1}\nUser Type: {2}'
        s = s.format(self.username, self.emailID, self.user_type)
        return s

class FrequentTraveller(User):
    def __init__(self):
        self.user_type = 'Frequent Traveller'
        super().__init__()

    def register(self, username, password, emailID, travellerID):
        super().register(username, password, emailID)
        self.travellerID = travellerID

    def __repr__(self):
        s = '{0}\nEmail: {1}\nUser Type: {2}\nTravellerID: {3}'
        s = s.format(self.username, self.emailID, self.user_type, self.travellerID)
        return s