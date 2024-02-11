# Generated by Django 5.0.2 on 2024-02-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_loandetail_end_date_loandetail_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetail',
            name='tenure',
            field=models.CharField(choices=[('1', 'One Year'), ('2', 'Two Years'), ('3', 'Three Years'), ('4', 'Four Years'), ('5', 'Five Years')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]