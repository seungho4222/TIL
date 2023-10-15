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