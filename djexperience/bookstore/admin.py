from django.contrib import admin
from .models import Author, Book, People, PF, PJ, Customer, Provider

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(People)
admin.site.register(PF)
admin.site.register(PJ)
admin.site.register(Customer)
admin.site.register(Provider)