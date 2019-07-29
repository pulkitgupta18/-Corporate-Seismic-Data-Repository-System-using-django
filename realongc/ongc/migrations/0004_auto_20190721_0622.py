# Generated by Django 2.1.2 on 2019-07-21 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ongc', '0003_acquisition'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Block',
            new_name='Acquisition_add',
        ),
        migrations.RenameModel(
            old_name='Acquisition',
            new_name='Block_add',
        ),
        migrations.RenameModel(
            old_name='Survey',
            new_name='Survey_add',
        ),
        migrations.RenameField(
            model_name='acquisition_add',
            old_name='blockname',
            new_name='acquisitionname',
        ),
        migrations.RenameField(
            model_name='acquisition_add',
            old_name='blocknumber',
            new_name='acquisitionnumber',
        ),
        migrations.RenameField(
            model_name='block_add',
            old_name='acquisitionname',
            new_name='blockname',
        ),
        migrations.RenameField(
            model_name='block_add',
            old_name='acquisitionnumber',
            new_name='blocknumber',
        ),
    ]
