class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__len_password()

    def __len_password(self):
        if len(self.password) < 8:
            raise ValueError('Weak password! Need more stronger password')

    def save(self):
        with open('user.txt', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')
