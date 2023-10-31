# Generated by Django 4.2.3 on 2023-10-31 06:47

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="نام دسته بندی"),
                ),
                (
                    "return_condition",
                    models.TextField(
                        default="برای کالاهای گروه موبایل، امکان برگشت کالا به دلیل انصراف از خرید تنها در صورتی مورد قبول است که کالا بدون هیچگونه استفاده و با تمامی قطعات، متعلقات و بسته\u200cبندی\u200cهای اولیه خود بازگردانده شود. لازم به ذکر است که برای هر کالای موبایل، ضمانت رجیستری صادر می\u200cشود. در صورت بروز اشکال در ضمانت رجیستری، پس از انقضای مدت ۳۰ روزه، کالا می\u200cتواند بازگردانده شود."
                    ),
                ),
                ("is_special", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Mobile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=450, verbose_name="نام محصول")),
                ("image", models.ImageField(upload_to="", verbose_name="عکس محصول")),
                (
                    "alt",
                    models.CharField(
                        blank=True,
                        default="image",
                        max_length=100,
                        null=True,
                        verbose_name="توضیح عکس",
                    ),
                ),
                ("dimensions", models.CharField(max_length=150)),
                ("weight", models.CharField(max_length=150)),
                ("count", models.PositiveIntegerField()),
                ("price", models.PositiveIntegerField()),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=18, samples=None
                    ),
                ),
                (
                    "discount",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="درصد تخفیف",
                    ),
                ),
                ("sales_number", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("is_special", models.BooleanField(default=False)),
                ("is_show", models.BooleanField(default=True)),
                ("ram", models.CharField(max_length=10)),
                ("cpu", models.CharField(max_length=150)),
                ("front_camera", models.CharField(max_length=150)),
                ("back_camera", models.CharField(max_length=150)),
                ("sim_cart", models.CharField(max_length=150)),
                ("os", models.CharField(default="", max_length=150)),
                ("included_items", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Laptop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=450, verbose_name="نام محصول")),
                ("image", models.ImageField(upload_to="", verbose_name="عکس محصول")),
                (
                    "alt",
                    models.CharField(
                        blank=True,
                        default="image",
                        max_length=100,
                        null=True,
                        verbose_name="توضیح عکس",
                    ),
                ),
                ("dimensions", models.CharField(max_length=150)),
                ("weight", models.CharField(max_length=150)),
                ("count", models.PositiveIntegerField()),
                ("price", models.PositiveIntegerField()),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF", image_field=None, max_length=18, samples=None
                    ),
                ),
                (
                    "discount",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[django.core.validators.MaxValueValidator(100)],
                        verbose_name="درصد تخفیف",
                    ),
                ),
                ("sales_number", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("is_special", models.BooleanField(default=False)),
                ("is_show", models.BooleanField(default=True)),
                ("ram", models.CharField(max_length=10)),
                ("cpu", models.CharField(max_length=150)),
                ("webcam", models.CharField(max_length=150)),
                ("graphic_card", models.CharField(max_length=150)),
                ("os", models.CharField(default="", max_length=150)),
                ("included_items", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
