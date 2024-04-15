from django.contrib import admin
from . models import User,Product,Wishlist,category,Profile
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(category)
admin.site.register(Profile)