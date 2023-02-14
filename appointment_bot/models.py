from django.db import models

class data_model(models.Model):
    #primary fields
    province = models.CharField(max_length=200, null=True)
    procedure = models.TextField( null=True)
    nie = models.CharField(max_length=200, null=True)
    dni = models.CharField(max_length=200, null=True)
    passport = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    birth_year = models.CharField(max_length=200, null=True)
    origin_country = models.CharField(max_length=200, null=True)
    expiration_date = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    # additional fields
    appointment_approved = models.BooleanField(default=False, null=True)
    appointment = models.CharField(max_length=200, null=True, default="NotApproved")
    
    reason = models.TextField(null=True)
    class Meta:
        verbose_name = "Appointment List"





