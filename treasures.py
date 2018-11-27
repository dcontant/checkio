'''
 As input you'll receive the information about the vault contents in the following format: 
 {'golden coin': {'price': 100, 'weight': 50, 'amount': 200}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 1000} , 
 'ruby': {'price': 1000, 'weight': 200, 'amount': 2}}, where price is measured in the standard units of your country's 
 currency, weight is measured in grams, and amount is measured in pieces.
In addition, you'll also have a weight limit (in kilograms), over which you won't be able to carry.

Your task is to collect such a set of treasures so that their total weight doesn't exceed the limit, and their total cost 
was as high as possible. The answer must be returned as the list of strings, for example: ['golden coin: 150', 
'silver coin: 700', 'ruby: 2']. There always be 3 types of the treasures (golden coin, silver coin and ruby) and it should 
be represent in the answer in the same order. If some type of the treasures are out of limit (so you 'can' take it 0) - 
just don't include it into answer.

Input: Dictionary with information about treasures and weight limit.

Output: All treasures, which you take (a list of strings).

Precondition:
3 types of treasures 
'''

def treasures(info, limit):
    
    def value_density(token):
        return info[token]['price'] / info[token]['weight']
    
    limit = limit * 1000
    contents = sorted([token for token in info], key = value_density, reverse = True)
    temp_answer = dict()
    for token in contents:
        token_total_weight = info[token]['weight'] * info[token]['amount']
        if token_total_weight <= limit :
            temp_answer[token] = str(info[token]['amount'])
            limit -= token_total_weight
        elif limit > 0:
            temp_answer[token] =  str(int(limit // info[token]['weight']))
            break
    final_answer = []
    for token in ['golden coin', 'silver coin', 'ruby']:
        if token in temp_answer:
            final_answer.append(token + ': ' + temp_answer[token])
    return final_answer
        
            
    
    
if __name__ == '__main__':
    
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 200}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 1000}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin': 
                         {'price': 100, 'weight': 50, 'amount': 100}, 
                      'silver coin': 
                         {'price': 10, 'weight': 20, 'amount': 100}, 
                      'ruby': 
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    assert treasures({"silver coin":
                          {"price":10,"amount":100,"weight":20},
                      "ruby":
                          {"price":1000,"amount":3,"weight":200},
                      "golden coin":
                          {"price":100,"amount":100,"weight":50}},0.6) == ["ruby: 3"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
