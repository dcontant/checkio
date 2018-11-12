class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.current = self.channels[0]
    
    def first_channel(self):
        self.current = self.channels[0]
        return self.current
    
    def last_channel(self):
        self.current = self.channels[-1]
        return self.current
    
    def turn_channel(self, n):
        self.current =  self.channels[n-1]
        return self.current
    
    def next_channel(self):
        current_index = self.channels.index(self.current)
        self.current = self.channels[(current_index +1) % len(self.channels)]
        return self.current
        
    
    def previous_channel(self):
        current_index = self.channels[::-1].index(self.current)
        self.current = self.channels[::-1][(current_index +1) % len(self.channels)]
        return self.current
    
    def current_channel(self):
        return self.current
    
    def is_exist(self, n):
        if type(n) == int:
            try:
                if self.channels[n-1]:
                    return 'Yes'
            except IndexError:
                return "No"
        else:
            yes = self.channels.count(n)
            return yes * 'Yes' + (not yes) * 'No'
                
            

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)
    
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
