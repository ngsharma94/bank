# Generated by Django 5.0.2 on 2024-02-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_alter_loandetail_loan_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetail',
            name='always_yes_because_of_signals',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loandetail',
            name='loan_active',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loandetail',
            name='is_approved',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1),
        ),
    ]
