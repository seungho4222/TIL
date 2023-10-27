from django.db import models


class Weather(models.Model):
    temp = models.FloatField()          # 온도(기본값: 캘빈)
    feels_like = models.FloatField()    # 체감온도(기본값: 캘빈)
    dt_txt = models.DateTimeField()     # 데이터 측정 시간
    