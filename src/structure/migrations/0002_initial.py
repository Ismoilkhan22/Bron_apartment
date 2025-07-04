# Generated by Django 5.0.1 on 2024-09-19 03:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='comforts',
            field=models.ManyToManyField(blank=True, to='structure.comfort'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.product'),
        ),
        migrations.AddField(
            model_name='productlike',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.product'),
        ),
        migrations.AddField(
            model_name='productlike',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productrule',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.product'),
        ),
        migrations.AddField(
            model_name='rent',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='structure.product'),
        ),
        migrations.AddField(
            model_name='rent',
            name='renter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
