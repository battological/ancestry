from django.db import models


class Immigration(models.Model):
        ship_name = models.CharField(max_length=100, blank=True)
        ship_embarkation_location = models.CharField(max_length=500, blank=True)
        ship_embarkation_date = models.DateField(blank=True, null=True)
        arrival_location = models.CharField(max_length=500, blank=True)
        arrival_date = models.DateField(blank=True, null=True)

        def __str__(self):
                return '<Immigration trip: {}>'.format(self.ship_name)


class Person(models.Model):
        first_name = models.CharField(max_length=50, blank=True)
        middle_name = models.CharField(max_length=200, blank=True)
        last_name = models.CharField(max_length=50, blank=True)
        maiden_name = models.CharField(max_length=50, blank=True)
        gender = models.CharField(max_length=1)
        birthdate = models.DateField(blank=True, null=True)
        deathdate = models.DateField(blank=True, null=True)
        father = models.ForeignKey('self', related_name='fathers_child', on_delete=models.SET_NULL, blank=True, null=True)
        mother = models.ForeignKey('self', related_name='mothers_child', on_delete=models.SET_NULL, blank=True, null=True)
        burial_location = models.TextField(blank=True)
        military_service = models.TextField(blank=True)
        career = models.TextField(blank=True)
        immigration = models.ForeignKey(Immigration, related_name='immigrant', on_delete=models.SET_NULL, blank=True, null=True)
        other_notes = models.TextField(blank=True)

        def __str__(self):
                return '{} {}'.format(self.first_name, self.last_name)

class Marriage(models.Model):
        spouse_a = models.ForeignKey(Person, related_name='spouse1', on_delete=models.PROTECT)
        spouse_b = models.ForeignKey(Person, verbose_name='Spouse', related_name='spouse2', on_delete=models.PROTECT)
        marriage_start_date = models.DateField(blank=True, null=True)
        marriage_end_date = models.DateField(blank=True, null=True)
        location = models.CharField(max_length=250, blank=True)

        def __str__(self):
                return '<Marriage: {} + {}>'.format(self.spouse_a.first_name, self.spouse_b.first_name)


class SchoolAttendance(models.Model):
        person = models.ForeignKey(Person, related_name='student', on_delete=models.PROTECT)
        school_level = models.CharField(max_length=50)
        school_name = models.CharField(max_length=250, blank=True)
        school_location = models.CharField(max_length=250, blank=True)
        degree_earned = models.CharField(max_length=50, blank=True)
        degree_earned_year = models.DateField(blank=True, null=True)

        def __str__(self):
                return '<School: {}, {} {}>'.format(self.school_name, self.person.first_name, self.person.last_name)


class Residence(models.Model):
        person = models.ForeignKey(Person, related_name='lived_in', on_delete=models.SET_NULL, blank=True, null=True)
        where = models.CharField(max_length=500)
        beginning = models.DateField(blank=True, null=True)
        ending = models.DateField(blank=True, null=True)

        def __str__(self):
                return '<Residence: {}, {} {}>'.format(self.where, self.person.first_name, self.person.last_name)
