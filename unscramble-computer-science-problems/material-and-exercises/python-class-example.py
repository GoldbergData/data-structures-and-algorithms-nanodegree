class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month

    def birthday(self):
        self.age += 1


def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects


def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages
    # as values. See the test below for an example expected output.
    keys = []
    ages = []
    for person in people:
        if person.birthday_month == 'April':
            person.birthday()
            keys.append(person.name)
            ages.append(person.age)
    april_birthdays = dict(zip(keys, ages))

    # TODO: Modify the return statement
    return april_birthdays


def get_most_common_month(people):
    # TODO:
    # Use the "months" dictionary to record counts of birthday months
    # for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0,
              'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0,
              'November': 0, 'December': 0}

    for person in people:
        if person.birthday_month == 'January':
            months['January'] += 1
        elif person.birthday_month == 'February':
            months['February'] += 1
        elif person.birthday_month == 'March':
            months['March'] += 1
        elif person.birthday_month == 'April':
            months['April'] += 1
        elif person.birthday_month == 'May':
            months['May'] += 1
        elif person.birthday_month == 'June':
            months['June'] += 1
        elif person.birthday_month == 'August':
            months['August'] += 1
        elif person.birthday_month == 'September':
            months['September'] += 1
        elif person.birthday_month == 'October':
            months['October'] += 1
        elif person.birthday_month == 'November':
            months['November'] += 1
        elif person.birthday_month == 'December':
            months['December'] += 1
    print(months)
    max_value = max(months.values())
    max_month = [k for k, v in months.items() if v == max_value]
    # TODO: Modify the return statement.
    return max_month[0]


def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Suzanne', 'Dorothy', 'Edna', 'Olive', 'Barbara', 'Agnes',
             'Anthony', 'Mildred', 'Stephen', 'Daniel', 'James', 'David',
             'Anna', 'Frank', 'Darlene', 'Chris', 'Micheal', 'James', 'Joseph',
             'George', 'Barry', 'Clarice', 'Maranda', 'Jessica', 'Nicole',
             'Grace', 'Randy', 'Jennifer', 'Richard', 'William', 'Dennis',
             'Peggy', 'James', 'Sarah', 'Nellie', 'Dominique', 'Stewart',
             'Wendy', 'Caroline', 'Barbara', 'Carey', 'Tammy', 'Charles',
             'Brian', 'Amber', 'Paula', 'Troy', 'Laura', 'Dewey', 'Joe', 'Kim',
             'Rosalinda', 'Martin', 'Juan', 'Larry', 'Cherryl', 'Heather',
             'Betty', 'Carol', 'Robert', 'Bruce', 'Carla', 'Delphia', 'Bernice',
             'Sylvia', 'Gavin', 'John', 'Mildred', 'Jamie', 'Javier', 'Carolyn',
             'Armando', 'Joseph', 'Marjorie', 'Ruth', 'Roy', 'Randy', 'Ana',
             'Jerald', 'Wendy', 'Margaret', 'Barbara', 'Donald', 'Lawrence',
             'Hope', 'Mason', 'Jonathan', 'John', 'Evelyn', 'Catherine',
             'Anthony', 'Rita', 'Alan', 'Reginald', 'Christopher', 'Bernice',
             'Trinidad', 'Marna', 'Jasmine', 'Dwight']

    ages = [13, 98, 12, 68, 40, 87, 38, 95, 67, 11, 65, 66, 43, 12, 22, 80, 87,
            52, 48, 31, 8, 100, 54, 81, 84, 80, 80, 48, 54, 84, 75, 98, 64, 10,
            94, 83, 50, 52, 83, 85, 66, 13, 56, 14, 39, 23, 78, 41, 62, 29, 25,
            43, 70, 87, 86, 69, 82, 61, 28, 44, 26, 70, 43, 67, 93, 81, 37, 66,
            46, 86, 97, 31, 85, 65, 3, 34, 54, 97, 54, 92, 96, 71, 73, 63, 4,
            68, 61, 56, 38, 34, 9, 57, 84, 92, 29, 5, 73, 70, 18, 87]

    months = ['December', 'January', 'November', 'October', 'March', 'December',
              'June', 'March', 'December', 'January', 'November', 'June',
              'January', 'December', 'June', 'November', 'November', 'August',
              'December', 'May', 'July', 'June', 'June', 'September', 'June',
              'July', 'December', 'May', 'August', 'June', 'December', 'August',
              'September', 'October', 'August', 'June', 'June', 'March',
              'September', 'October', 'July', 'December', 'May', 'October',
              'June', 'April', 'March', 'March', 'July', 'October', 'December',
              'October', 'June', 'March', 'November', 'April', 'July',
              'September', 'September', 'May', 'August', 'March', 'March',
              'April', 'December', 'November', 'March', 'October', 'October',
              'June', 'June', 'April', 'August', 'March', 'March', 'November',
              'January', 'June', 'October', 'May', 'August', 'January',
              'September', 'January', 'February', 'October', 'January', 'March',
              'April', 'March', 'April', 'April', 'June', 'January', 'November',
              'April', 'August', 'July', 'November', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))


test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August
