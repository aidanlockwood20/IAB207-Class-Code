from travel.city import City
from travel.user import User, FrequentTraveller
from travel.booking import Booking
from datetime import datetime

new_city = City('Brisbane', 'South Eastern Australia')
new_user = User()
another_user = FrequentTraveller()
another_user.register('rick123', 'password1', 'rick123@gmail.com', 'RickRolld')
new_user.register('jerry123', 'password1', 'jerry123@gmail.com')

start_date = datetime(2022, 2, 1)
end_date = datetime(2022, 2, 28)

new_booking = Booking(start_date, end_date, new_city, another_user)

print(new_booking)
