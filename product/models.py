from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True, help_text="foo")


    def __repr__(self):
        return "%s ($%s)" % (self.name, self.price/100.0)
