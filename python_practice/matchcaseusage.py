def http_status(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not found"
        case _:
            return "Other error"

print(http_status(400))
print(http_status(401))
print(http_status(403))
print(http_status(404))
print(http_status(405))


def http_status1(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Authentication error"
        case 404:
            return "Not found"
        case _:
            return "Other error"

print("Second Set: "+ http_status1(401))
print(http_status1(403))    

def alarm(item):
    match item:
        case [('morning' | 'afternoon' | 'evening') as time, action]:
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')

print(alarm(['afternoon', 'work']))

def alarm1(item):
    match item:
        case ['evening', action] if action not in ['work', 'study']:
            print(f'You almost finished the day! Now {action}!')
        case ['evening', _]:
            print('Come on, you deserve some rest!')
        case [time, action]:
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')

print (alarm1(['evening', 'study']))
print (alarm1(['morning', 'study']))

class Direction:
    def __init__(self, horizontal=None, vertical=None):
        self.horizontal = horizontal
        self.vertical = vertical


def direction(loc):
    match loc:
        case Direction(horizontal='east', vertical='north'):
            print('You towards northeast')
        case Direction(horizontal='east', vertical='south'):
            print('You towards southeast')
        case Direction(horizontal='west', vertical='north'):
            print('You towards northwest')
        case Direction(horizontal='west', vertical='south'):
            print('You towards southwest')
        case Direction(horizontal=None):
            print(f'You towards {loc.vertical}')
        case Direction(vertical=None):
            print(f'You towards {loc.horizontal}')
        case _:
            print('Invalid Direction')

d1=Direction('east','south')
d2 = Direction(vertical='north')
d3 = Direction('centre', 'centre')

print(direction(d1))
print(direction(d2))
print(direction(d3))




