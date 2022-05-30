# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pessoa(models.Model):
    pessoa_id = models.BigIntegerField(primary_key=True)
    pessoa_nome = models.CharField(max_length=255, blank=True, null=True)
    pessoa_data_nasc = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa'


class InfoTable(models.Model):
    info_table_x_id = models.BigIntegerField(primary_key=True)
    info_table_y_id = models.BigIntegerField()
    info_table_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info_table'
        unique_together = (('info_table_x_id', 'info_table_y_id'),)
