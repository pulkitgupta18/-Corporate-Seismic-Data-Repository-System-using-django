from django.db import models

class Survey_add(models.Model):
    surveyname = models.CharField(max_length=200)
    surveynumber=models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)

class Block_add(models.Model):
    blockname=models.CharField(max_length=200)
    blocknumber=models.CharField(max_length=20)
    cpf=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)

class Acquisition_add(models.Model):
    acquisitionname=models.CharField(max_length=200)
    acquisitionnumber=models.CharField(max_length=20)
    cpf=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)    

class Media_add(models.Model):
    medianame=models.CharField(max_length=200)
    medianumber=models.CharField(max_length=20)
    cpf=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20)

class Meta:
    db_table='survey_add',
    db_table='block_add',
    db_table='acquisition_add',
    db_table='media_add'