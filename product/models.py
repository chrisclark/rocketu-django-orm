from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=128)


class Product(models.Model):

    name = models.CharField(max_length=128)
    price = models.IntegerField()
    desription = models.TextField(blank=True, null=True, help_text="hey there")
    category = models.ForeignKey(Category, null=True)


    def __repr__(self):
        return "%s - $%s" % (self.name, self.price/100)

