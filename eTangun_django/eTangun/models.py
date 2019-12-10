from django.db import models
import datetime


class LevelDict(models.Model):
    belt_level = models.CharField(max_length=10, blank=True)


class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=datetime.datetime.now, blank=True)
    belt_level = models.ForeignKey(
        LevelDict, on_delete=models.CASCADE, blank=True
    )
    group = models.IntegerField()
    is_active = models.BooleanField(default=True)
    comment = models.TextField(blank=True)
    gender = models.CharField(max_length=1, blank=True)  # M or K
    login = models.CharField(max_length=5, blank=True)


class Addresses(models.Model):
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    descr = models.CharField(max_length=150)
    country = models.CharField(max_length=2, default='pl')


class CompetitionDict(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)


class CompetitionResult(models.Model):
    place = models.IntegerField()
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    competition_date = models.DateField(default=datetime.datetime.now,
                                        blank=True)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    competition_active = models.ForeignKey(CompetitionDict,
                                           on_delete=models.CASCADE)


class PaymentsList(models.Model):
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    payment = models.IntegerField()