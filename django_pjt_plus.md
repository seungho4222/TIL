# :whale: 장고 프로젝트 응용

[✨ 폼 출력형식 (Choic, Float)](#-폼-출력형식-choic-float)

[🧑‍🤝‍🧑 Many To Many Field (M : N 관계)](#-many-to-many-field-m--n-관계)

[❤️ 좋아요 구현](#-좋아요-구현)

[#️⃣ 해쉬태그 구현](#️-해쉬태그-구현)

---

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


## 🧑‍🤝‍🧑 Many To Many Field (M : N 관계)
```py
class Patient(models.Model):  # 역참조 시 사용하는 manager name 변경
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
# doctor.patient_set.all() -> doctor.patients.all()

class Person(models.Model):  # 대칭 참조(기본값: True)
    friends = models.ManyToManyField('self')
    # friends = models.ManyToManyField('self', symmetrical=False)
# 내가 네 친구면 너도 내 친구 !

class Article(models.Model):  # 유저필드와 역참조 매니저 충돌 방지
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')  # 역참조 이름 변경
    title = models.CharField(max_length=10)
    content = models.TextField()
```


## ❤️ 좋아요 구현
```py
# models.py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


# urls.py
    path('<int:article_pk>/likes/', views.likes, name='likes'),


# views.py
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
    # if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article)
    else:
        article.like_users.add(request.user)
        # request.user.like_articles.add(article)
    return redirect('articles:index')


# index.html
<p>{{ article.like_users.all|length }}</p>  # DTL 함수 : 개수 카운트
<form action="{% url "articles:likes" article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소">
    {% else %}
        <input type="submit" value="좋아요">
    {% endif %}
</form>
```


## #️⃣ 해쉬태그 구현
```py
# models.py
class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Article(models.Model):
    hashtags = models.ManyToManyField(Hashtag, blank=True)


# urls.py
    path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),


# views.py
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    # pk 역순 조회
    articles = hashtag.article_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)

def create(request):
    if form.is_valid():
        ... # 해쉬태그 생성
        for word in article.content.split():
            if word.startswith("#"):
                # 조건을 만족하면 가져오고 없으면 생성
                hashtag, created = Hashtag.objects.get_or_create(content=word)
                article.hashtags.add(hashtag)


# pjt/templatetags/make_link.py (__init__.py 도 생성)
from django import template

register = template.Library()

@register.filter
def hashtag_link(article):
    content = article.content
    hashtags = article.hashtags.all()
    # '#'으로 시작하는 단어가 존재 => 링크로 만들어 주기
    for hashtag in hashtags:
        content = content.replace(hashtag.content,
            f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a>')
    return content


# detail.html
<p>내용 : {{ article|hashtag_link|safe }}</p> 과 같이 사용
```