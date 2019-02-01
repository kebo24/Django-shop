# Generated by Django 2.1.3 on 2019-01-27 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20190118_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父类级别', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类'),
        ),
    ]