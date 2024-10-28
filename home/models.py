from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
