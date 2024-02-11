# Generated by Django 5.0.2 on 2024-02-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0010_fixeddeposit_interest_fixeddeposit_maturity_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixeddeposit',
            name='tenure',
            field=models.CharField(choices=[('1', 'One Year'), ('2', 'Two Years'), ('3', 'Three Years'), ('4', 'Four Years'), ('5', 'Five Years')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]