from django.db import models


class TestModel(models.Model):

    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'test_model'
