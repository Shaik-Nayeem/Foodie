from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.

class Product(models.Model):

    name=models.CharField(max_length=264)
    description=models.CharField(max_length=264)
    location=models.CharField(max_length=264)
    document = models.FileField(upload_to='documents/')
    cost=models.BigIntegerField()
    cuisines=models.CharField(max_length=264)
    #ratings=models.IntegerField()
    quantity= models.DecimalField(decimal_places=1,max_digits=5)
    #quantity=models.IntegerField()
    
    class Meta:
    
        permissions=(


                  ('is_admin',_('Is Admin  ')),
                   ('is_user',('Is User')),
        )

    def __str__(self):

        return self.name


class Menu(models.Model):

    name=models.CharField(max_length=264)
    price=models.BigIntegerField()
    product=models.ForeignKey(Product)



    class Meta:
    
        permissions=(


                  ('is_teacher',_('Is Teacher')),
                   ('is_student',('Is Student')),
        )

   # menu_id=models.ForeignKey(settings.AUTH_USER_MODEL)


    def __str__(self):

        return self.name




    

    def get_post_url(self):
       return reverse('update', kwargs={'pk': self.pk})

    def get_post_url(self):
        return reverse('delete', kwargs={'pk': self.pk})
