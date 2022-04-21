from datetime import datetime
from .user import User
from .city import City

class Booking: 

    def __init__(self, start_date, end_date, city, user):
        self.num_guests = 1
        self.start_date = start_date
        self.end_date = end_date
        self.city = city
        self.user = user

    def __repr__(self):
        s = 'Number of Guests: {0}\nStart Date: {1}\nEnd Date: {2}\nCity: {3}\nUser: {4}'
        s = s.format(self.num_guests, 
                        self.start_date, 
                        self.end_date, 
                        self.city, 
                        self.user)
        return s