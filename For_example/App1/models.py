from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Games(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)

#    buyer = models.ManyToManyField(Buyer, related_name='Games')
#    в данном задании не реализуе

    def __str__(self):
        return self.title
