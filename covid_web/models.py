from django.db import models
from django.urls import reverse


class UserInfo(models.Model):
    username = models.CharField(max_length=15, help_text='Enter username (max 15)')
    email = models.EmailField(max_length=25, help_text='Enter you email')
    password = models.CharField(max_length=20, help_text='Enter password (max 20)')
    reg_date = models.DateField(auto_now_add=True)

    # Metadata
    class Meta:
        ordering = ['-reg_date', 'username']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.username


class Favourite(models.Model):
    place = models.CharField(max_length=15, help_text='Enter username (max 15)')

    def __str__(self):
        return self.place
