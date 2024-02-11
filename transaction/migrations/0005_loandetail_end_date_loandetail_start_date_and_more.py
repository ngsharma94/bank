# Generated by Django 5.0.2 on 2024-02-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_loandetail_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetail',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loandetail',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fixeddeposit',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fixeddeposit',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
