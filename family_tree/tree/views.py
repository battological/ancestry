from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .models import Immigration, Marriage, Person, Residence, SchoolAttendance

class Children(generic.DetailView):
        model = Person

        def get_context_data(self, **kwargs):
                context = super(Children, self).get_context_data(**kwargs)

                context['children'] = Person.objects.filter(
                        Q(father=self.get_object()) | Q(mother=self.get_object())
                )

                marriages = Marriage.objects.filter(
                        Q(spouse_a=self.get_object()) | Q(spouse_b=self.get_object())
                )
                for marriage in marriages:
                        if marriage.spouse_a == self.get_object():
                                marriage.spouse = marriage.spouse_b
                        else:
                                marriage.spouse = marriage.spouse_a
                context['marriages'] = marriages

                context['schools'] = SchoolAttendance.objects.filter(person=self.get_object())
                context['residences'] = Residence.objects.filter(person=self.get_object())

                return context


class FamilyTree(generic.ListView):
        model = Person

        def get_context_data(self):
                context = super(FamilyTree, self).get_context_data(**kwargs)

                # magic!
                # ...

                return context
