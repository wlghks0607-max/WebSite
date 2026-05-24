from django.db import models

class Gacha(models.Model):
    winning_nums = models.JSONField(null=True, blank=True)
    bonus_num = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}회차"

class Ticket(models.Model):
    draw = models.ForeignKey(Gacha, on_delete=models.CASCADE)
    nums = models.JSONField()
    is_auto = models.BooleanField(default=True)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.draw.id}회차 티켓 - {self.nums}"

