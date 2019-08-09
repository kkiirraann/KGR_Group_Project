from django.db import models

class Category(models.Model):
  cat_name = models.CharField(max_length = 150)


  def __str__(self):
    return self.cat_name

class Product(models.Model):
  category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE )
  product_name = models.CharField(max_length = 100,default='')
  author = models.CharField(max_length = 100,default='')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  available = models.BooleanField(default=True)
  stock = models.PositiveIntegerField()
  image = models.ImageField(upload_to='shop/images/products',default ='')


  def __str__(self):
    return self.product_name

class Contact(models.Model):
  msg_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=70, default="")
  phone = models.IntegerField()
  message = models.TextField()


  def __str__(self):
    return self.name