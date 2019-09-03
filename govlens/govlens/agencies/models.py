from django.db import models
from django.utils import timezone


def logo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/agency_logos/<id>/<filename>
    return 'agency_logos/{0}/{1}'.format(instance.id, filename)


# Create your models here.
class Agency(models.Model):
    id = models.IntegerField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    facebook = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    last_successful_scrape = models.DateTimeField(blank=True, null=True)
    scrape_counter = models.IntegerField(default=0)
    logo = models.ImageField(upload_to=logo_path, blank=True)

    # Geolocation
    latitude = models.DecimalField(max_digits=8, decimal_places=3,default=0)
    longitude = models.DecimalField(max_digits=8, decimal_places=3,default=0)

    def __str__(self):
        return self.name
