class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        

    def corners(self):
        sw = [self.south, self.west]
        se = [self.south, self.west + self.width_WE]
        nw = [self.south + self.width_NS, self.west]
        ne = [self.south + self.width_NS, self.west + self.width_WE]
        return {'north-west': nw,'north-east': ne,
                'south-west': sw ,'south-east': se}

    def area(self):
        corners = self.corners()
        width = corners['south-east'][1]-corners['south-west'][1]
        length = corners['north-east'][0]-corners['south-east'][0]
        return width * length

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4}, {5})'.format(type(self).__qualname__, self.south, self.west, self.width_WE, 
                                                self.width_NS, self.height)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
    print('tests all good')
