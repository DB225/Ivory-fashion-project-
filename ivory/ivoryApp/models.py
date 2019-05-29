from django.db import models
from django.contrib.auth.models import User

# Model for user
class UserLoginModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    userForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


# MODELS FOR MEN
# Model for t-shirt
class Tshirt(models.Model):
    ts_title = models.CharField(max_length=200)
    ts_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    ts_size = models.CharField(max_length=20)
    ts_price = models.IntegerField
    ts_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.ts_title


# Model for shirt
class Shirt(models.Model):
    s_title = models.CharField(max_length=200)
    s_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    s_size = models.CharField(max_length=20)
    s_price = models.IntegerField
    s_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.s_title


# Model for pants
class Pants(models.Model):
    pant_title = models.CharField(max_length=200)
    pant_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    pant_size = models.CharField(max_length=20)
    pant_price = models.IntegerField
    pant_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.pant_title


# Model for men's shoes
class ShoesMen(models.Model):
    sm_title = models.CharField(max_length=200)
    sm_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    sm_size = models.CharField(max_length=20)
    sm_price = models.IntegerField
    sm_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.sm_title

###############################################
# MODELS FOR WOMEN
# Model for dress
class Dress(models.Model):
    dress_title = models.CharField(max_length=200)
    dress_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    dress_size = models.CharField(max_length=20)
    dress_price = models.IntegerField
    dress_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.dress_title


# Model for bag&Jewelry
class BagJewel(models.Model):
    bj_title = models.CharField(max_length=200)
    bj_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    bj_size = models.CharField(max_length=20)
    bj_price = models.IntegerField
    bj_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.bj_title


# Model for women's shoes
class ShoesWomen(models.Model):
    sw_title = models.CharField(max_length=200)
    sw_picture = models.ImageField(upload_to="media/images/", null=True, blank=True)
    sw_size = models.CharField(max_length=20)
    sw_price = models.IntegerField
    sw_ForeignKey = models.ForeignKey(UserLoginModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.sw_title
