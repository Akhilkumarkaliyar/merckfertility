from django.db import models

# Create your models here.
class f_users(models.Model):
    name  = models.CharField(max_length=50, null=False)
    nurseid=models.CharField(max_length=100,null=False)
    accesscode=models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=255, null=False)
    hospital = models.CharField(max_length=50, null=False)
    speciality = models.CharField(max_length=15, null=False)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, null=False)
    created_date= models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)
    password  = models.CharField(max_length=50, null=False)
    # ifLogged    = models.BooleanField(default=False)
    # token       = models.CharField(max_length=500, null=True, default="")

    
    class Meta:
        db_table = 'f_users'

    def __str__(self):
        return "Nurse name is {} -and email is {}".format(self.name, self.email)


# class auth_user(models.Model):
#     password  = models.CharField(max_length=50, null=False)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_superuser = models.CharField(max_length=50, null=False)
#     username  = models.CharField(max_length=50, null=False)
#     first_name = models.EmailField(max_length=255, null=False)
#     last_name = models.CharField(max_length=15, null=False)
#     email = models.EmailField(max_length=255, null=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.CharField(max_length=500, null=True, default="")
#     date_joined =models.DateTimeField(auto_now_add=True)
  
#     class Meta:
#         db_table = 'auth_user'
#         managed = False

#############Country city stateModel by akhil #################
class countries(models.Model):
    sortname = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    phonecode = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'countries'

class states(models.Model):
    name = models.CharField(max_length=100, null=False)
    country_id = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'states'

class cities(models.Model):
    name = models.CharField(max_length=100, null=False)
    state_id = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'cities'
#############Country city state Model by akhil #################