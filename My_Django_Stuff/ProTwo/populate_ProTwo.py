import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')


import django
django.setup()


##Fake pop SCRIPT
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):

        fake_firstName = fakegen.name().split()[0]
        fake_LastName = fakegen.name().split()[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_firstName, last_name=fake_LastName, email=fake_email)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')
