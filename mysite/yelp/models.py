# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Attribute(models.Model):
    business = models.ForeignKey('Business', models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Business(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    name = models.CharField(max_length=255, blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        managed = False
        db_table = 'business'


class Category(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Checkin(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    date = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkin'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EliteYears(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elite_years'


class Friend(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    friend_id = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friend'


class Hours(models.Model):
    hours = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(Business, models.DO_NOTHING)

    def __str__(self):
        return self.hours

    class Meta:
        managed = False
        db_table = 'hours'


class Photo(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    caption = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class Review(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    stars = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    useful = models.IntegerField(blank=True, null=True)
    funny = models.IntegerField(blank=True, null=True)
    cool = models.IntegerField(blank=True, null=True)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class Tip(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tip'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    name = models.CharField(max_length=255, blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    yelping_since = models.DateTimeField(blank=True, null=True)
    useful = models.IntegerField(blank=True, null=True)
    funny = models.IntegerField(blank=True, null=True)
    cool = models.IntegerField(blank=True, null=True)
    fans = models.IntegerField(blank=True, null=True)
    average_stars = models.FloatField(blank=True, null=True)
    compliment_hot = models.IntegerField(blank=True, null=True)
    compliment_more = models.IntegerField(blank=True, null=True)
    compliment_profile = models.IntegerField(blank=True, null=True)
    compliment_cute = models.IntegerField(blank=True, null=True)
    compliment_list = models.IntegerField(blank=True, null=True)
    compliment_note = models.IntegerField(blank=True, null=True)
    compliment_plain = models.IntegerField(blank=True, null=True)
    compliment_cool = models.IntegerField(blank=True, null=True)
    compliment_funny = models.IntegerField(blank=True, null=True)
    compliment_writer = models.IntegerField(blank=True, null=True)
    compliment_photos = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name
        
    class Meta:
        managed = False
        db_table = 'user'

#class WebUser(models.Model):


class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True, null=True)
    comm_date = models.DateTimeField()
    user = models.CharField(max_length=255, blank=True, default = 'Anonymous')

    class Meta:
        db_table = 'comment'
