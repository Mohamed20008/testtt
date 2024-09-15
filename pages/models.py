from django.db import models
# علاقه واحد بواحد

# class Female(models.Model):
#     name_female = models.CharField(max_length=50, null=True)
#     def __str__(self):
#         return self.name_female
# class Male(models.Model):
#     name_male = models.CharField(max_length=50, null=True)
#     girl = models.OneToOneField(Female, on_delete=models.CASCADE)
#     # girl = models.OneToOneField(Female, on_delete=models.PROTECT)
#     def __str__(self):
#         return self.name_male
# # علاقه واحد بكثير
# class Product (models.Model):
#     title = models.CharField(max_length=50, null=True)
#     def __str__(self):
#         return self.title

# class User(models.Model):
#     name = models.CharField(max_length=55, null=True)
#     products = models.ForeignKey(Product, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
# # علاقه كثير لكثير
# class Video (models.Model):
#     title = models.CharField(max_length=50, null=True)
#     def __str__(self):
#         return self.title
# class UserName(models.Model):
#     name = models.CharField(max_length=55, null=True)
#     watch = models.ManyToManyField(Video)
#     def __str__(self):
#         return self.name
class Login(models.Model):
    username = models.CharField(max_length=50, default='d', null=True)
    password = models.CharField(max_length=8 , default='d', null=True)