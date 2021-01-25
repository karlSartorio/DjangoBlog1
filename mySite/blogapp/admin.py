from django.contrib import admin
from blogapp.models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

#create a super user.
# Username:     karl
# email:       k@rl.com
#password: testPassword
