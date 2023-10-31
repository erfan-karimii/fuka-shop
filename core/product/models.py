from django.db import models
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام دسته بندی')
    return_condition = models.TextField(default='برای کالاهای گروه موبایل، امکان برگشت کالا به دلیل انصراف از خرید تنها در صورتی مورد قبول است که کالا بدون هیچگونه استفاده و با تمامی قطعات، متعلقات و بسته‌بندی‌های اولیه خود بازگردانده شود. لازم به ذکر است که برای هر کالای موبایل، ضمانت رجیستری صادر می‌شود. در صورت بروز اشکال در ضمانت رجیستری، پس از انقضای مدت ۳۰ روزه، کالا می‌تواند بازگردانده شود.')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BaseProduct(models.Model):
    name = models.CharField(max_length=450,verbose_name='نام محصول')
    image = models.ImageField(verbose_name="عکس محصول")
    alt = models.CharField(max_length=100,verbose_name='توضیح عکس',null=True,blank=True,default='image')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    dimensions = models.CharField(max_length=150)
    weight = models.CharField(max_length=150)
    count = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    color = ColorField()
    discount = models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(100)],verbose_name='درصد تخفیف')
    sales_number = models.IntegerField(default=0)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False)
    is_show = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    # def main_discount_call(self):
    #     return self.price - (self.price * (self.discount/100))
    
    # def calculate_price(self,count):
    #     return self.main_discount_call() * count
    
    def in_stock(self):
        return bool(self.count)


class Mobile(BaseProduct):
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=150)
    front_camera = models.CharField(max_length=150)
    back_camera = models.CharField(max_length=150)
    sim_cart = models.CharField(max_length=150)
    os = models.CharField(max_length=150,default='')
    included_items = models.TextField()


class Laptop(BaseProduct):
    ram = models.CharField(max_length=10)
    cpu = models.CharField(max_length=150)
    webcam = models.CharField(max_length=150)
    graphic_card = models.CharField(max_length=150)
    os = models.CharField(max_length=150,default='')
    included_items = models.TextField()

