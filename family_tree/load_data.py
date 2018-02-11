from tree.models import Person


if __name__ == '__main__':
Person.objects.all().delete()
ruth = Person(
first_name='Ruth',
        middle_name='Gordon',
        last_name='Sherman',
        maiden_name='Gordon',
        gender='F',
        birthdate='1957-06-27',
        career='Computer programmer',
)
ruth.save()

glen = Person(
        first_name='Glen',
        middle_name='Philip',
        last_name='Sherman',
        gender='M',
        birthdate='1950-05-07',
        career='Computer programmer',
)
glen.save()

garrick = Person(
        first_name='Garrick',
        middle_name='Thomas',
        last_name='Sherman',
        gender='M',
        birthdate='1989-11-12',
        father=glen,
        mother=ruth
)
garrick.save()
