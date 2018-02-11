from django.contrib import admin

from .models import Immigration, Marriage, Person, Residence, SchoolAttendance


class ResidenceInline(admin.StackedInline):
        model = Residence
        extra = 1


class SchoolInline(admin.StackedInline):
        model = SchoolAttendance
        extra = 1


class MarriageInline(admin.StackedInline):
        model = Marriage
        fk_name = 'spouse_a'
        extra = 1


class PersonAdmin(admin.ModelAdmin):
        inlines = [MarriageInline, ResidenceInline, SchoolInline]


admin.site.register(Immigration)
admin.site.register(Marriage)
admin.site.register(Person, PersonAdmin)
admin.site.register(Residence)
admin.site.register(SchoolAttendance)
