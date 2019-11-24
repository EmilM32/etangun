"""
Function generate random login for every club member (length 5)
get member object as json:
    member = {
        "firstName": "zawodnik",
        "lastName": "nowy",
        "birthDate": "2019-01-12",
        "gender": "M"
    }
if return code == 0 return unique login for member
else No free login
"""
from random import randint
from eTangun.models import Members


class LoginGenerator:
    def __init__(self, member):
        self.member = member
        self.alphabet = [
            'A', 'Ą', 'B', 'C', 'Ć', 'D', 'E',
            'Ę', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó',
            'P', 'R', 'S', 'Ś', 'T', 'U', 'W',
            'Y', 'Z', 'Ź', 'Ż'
        ]
        self.current_logins = Members.objects.all().values('login')

    def create(self):
        first_name = self.member['firstName']
        last_name = self.member['lastName']
        birth_date = self.member['birthDate']
        gender = self.member['gender']
        alphabet = self.alphabet
        current_logins = self.current_logins

        def _length_check(number):
            len_name = number
            while True:
                if len_name > 9:
                    _name = str(len_name)
                    len_name = int(_name[0]) + int(_name[1])
                else:
                    break
            return len_name

        length_name = len(first_name) + len(last_name)
        _el_one = _length_check(length_name)
        alpDict = {}
        for i, el in enumerate(alphabet):
            alpDict[el] = i

        _index = int(len(first_name)/2)
        _dict_key = alpDict[first_name[_index].upper()]
        _el_two = _length_check(_dict_key)

        _date_arr = birth_date.split('-')
        _date_sum = int(_date_arr[0]) + int(_date_arr[1]) + int(_date_arr[2])
        _date_check = _length_check(_date_sum)
        _el_three = _length_check(ord(str(_date_check)))

        _logins = []
        for login in current_logins:
            _logins.append(login['login'])

        member_login = ''
        while True:
            rand_int = randint(0, 9)
            i = 0
            member_login = f"{gender}{_el_one}{_el_two}{_el_three}{rand_int}"
            if member_login not in _logins:
                break
            else:
                i += 1
                if i > 10:
                    return {'info': 'No free login', 'code': 1}

        return {'login': member_login, 'code': 0}
