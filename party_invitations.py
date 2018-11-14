class Friend:
    def __init__(self, name):
        self.name = name
        self.party = None
        
    def show_invite(self):
        if self.party:
            return self.party
        else:
            return 'No party...'
        
        
    

class Party:
    def __init__(self, name):
        self.name = name
        self.friends = []
        
    def add_friend(self, name):
        self.friends.append(name)
    
    def del_friend(self, name):
        self.friends.remove(name)

    def send_invites(self, date):
        for friend in self.friends:
            friend.party = '{party_name}: {date}'.format(party_name = self.name, date = date)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
