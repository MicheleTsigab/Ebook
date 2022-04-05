from django.contrib import admin

from .models import author, genre, ebook, authored_ebook,bought_ebook,review,discount,customer

admin.site.register(ebook)
admin.site.register(author)
admin.site.register(customer)
admin.site.register(authored_ebook)
admin.site.register(bought_ebook)
admin.site.register(review)
admin.site.register(discount)
admin.site.register(genre)