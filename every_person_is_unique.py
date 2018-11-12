from datetime import date

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = date(*[int(data) for data in birth_date.split('.')[::-1]])
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender
        
    def name(self):
        return self.first_name + ' ' + self.last_name
    
    def age(self):
        return (date(2018,1,1) - self.birth_date).days // 365
    
    def work(self):
        prefix = {'male': 'He is ', 'female': 'She is ', 'unknown': 'Is '}
        return '{gender}a {job}'.format(gender=prefix[self.gender], job=self.job)
    
    def money(self):
        total_money = self.salary * 12 * self.working_years
        millions = (str(total_money // 10**6)+' ') * bool(total_money // 10**6)
        thousands = (str(total_money%10**6 // 1000)+' ') * bool(total_money // 1000)
        hundreds = str(total_money%1000)
        return '{0}{1}{2:0<3}'.format(millions, thousands, hundreds)
    
    def home(self):
        return 'Lives in {self.city}, {self.country}'.format(self=self)
        
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
