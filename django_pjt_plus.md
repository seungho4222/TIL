# :whale: 장고 프로젝트 응용

## ✨ 폼 출력형식 (Choic, Float)

```py
# apps/forms.py
class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=[
        ('Comdey', 'Comedy'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
        ],
    )

    score = forms.FloatField(
        required=False,
        min_value=0,
        max_value=5,
        widget=forms.NumberInput(
            attrs={'step': '0.5'}
        ),
    )
```


## Many To Many Field (M : N 관계)
```py
class Patient(models.Model):  # 역참조 시 사용하는 manager name 변경
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
# doctor.patient_set.all() -> doctor.patients.all()

class Person(models.Model):  # 대칭 참조(기본값: True)
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)
# 내가 네 친구면 너도 내 친구 !

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')  # 유저필드와 역참조 매니저 충돌 방지
    content = models.CharField(max_length=200)

```