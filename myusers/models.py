from django.db import models


class My_user(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.email)





# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
# from django.db import models
#
#
# class User(models.Model):
#     username = models.CharField(max_length=255, blank=False, null=False)
#     email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
#     password = models.CharField(max_length=255, blank=False, null=False)
