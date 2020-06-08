from django.db import models


# Create your models here.

class Services(models.Model):
    service_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.service_name


class Subservices(models.Model):
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    subservice_name = models.CharField(max_length=100)
    subservice_description = models.CharField(max_length=500)

    def __str__(self):
        return self.subservice_name + ' of ' + self.service_name.service_name
