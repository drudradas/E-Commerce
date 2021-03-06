# Generated by Django 3.1 on 2022-03-29 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20220329_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='category_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctions',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
