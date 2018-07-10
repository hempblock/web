# Generated by Django 2.0.7 on 2018-07-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('dashboard', '0090_auto_20180709_1525'), ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='status',
            field=models.CharField(
                choices=[('review', 'Needs Review'), ('warned', 'Hunter Warned'), ('okay', 'Okay'),
                         ('snoozed', 'Snoozed'), ('pending', 'Pending')],
                default='okay',
                help_text='Whether or not the interest requires review',
                max_length=7,
                verbose_name='Needs Review'
            ),
        ),
        migrations.AlterField(
            model_name='interest',
            name='acceptance_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Accepted'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='issue_message',
            field=models.TextField(blank=True, default='', verbose_name='Issue Comment'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='pending',
            field=models.BooleanField(
                default=False,
                help_text='If this option is chosen, this interest is pending and not yet active',
                verbose_name='Pending'
            ),
        ),
    ]
