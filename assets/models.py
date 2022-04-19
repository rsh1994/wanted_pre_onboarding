from django.db import models

# Create your models here.
class Server(models.Model):
    status_choice = (
        ('online', '  '),
        ('offline', '  '),
        ('normal', '  '),
        ('abnormal', '  ')
    )

    server_name = models.CharField(verbose_name=u'     ', max_length=128, blank=False, null=False)
    server_num = models.CharField(verbose_name=u'     ', max_length=128, blank=True, null=True)
    brand = models.CharField(verbose_name=u'  ', max_length=64, blank=True, null=True)
    model = models.CharField(verbose_name=u'  ', max_length=64, blank=True, null=True)
    cpus = models.IntegerField(verbose_name=u'cpu  ', default=0)
    ram = models.IntegerField(verbose_name=u'    ', default=0)
    disk = models.IntegerField(verbose_name=u'    ', default=0)
    product_date = models.DateTimeField(verbose_name=u'    ', auto_now_add=True)
    status = models.CharField(verbose_name=u'  ', max_length=16, choices=status_choice)

    created_time = models.DateTimeField(verbose_name=u'    ', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=u'    ', auto_now_add=True)

    class Meta:
        verbose_name = u'   '
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.server_name