## 📍 forms.py

##### 🔻 폼 출력형식 (Choic, Float)

```py
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