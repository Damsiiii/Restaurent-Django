from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    table_number = models.IntegerField()
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Table {self.table_number}"