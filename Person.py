# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user.'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User has been added with id ', person.set_name('Priyanka'))
    print('User associated with id is ', person.get_name(0))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
