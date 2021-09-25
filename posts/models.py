from django.db import models

class Memo(models.Model):
    memo = models.CharField(max_length=100,verbose_name="メモ")

    def __str__(self):
        return self.memo