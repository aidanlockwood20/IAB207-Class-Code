class City:

    def __init__(self, city_name, description):
        self.city_name = city_name
        self.description = description

    def getCityDetails(self, city_name, description):
        return str(self)
    
    def __repr__(self):
        s = '{0}\nDescription: {1}'
        s = s.format(self.city_name, self.description)
        return s