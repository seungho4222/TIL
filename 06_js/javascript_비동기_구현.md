# :whale2: 자바스크립트 axios

[🧸 팔로우 구현](#-팔로우-구현)

[💕 좋아요 구현](#-좋아요-구현)

---

## 🧸 팔로우 구현
```py
# view.py
from django.http import JsonResponse

@login_required
def follow(request, user_pk):
  User = get_user_model()
  you = User.objects.get(pk=user_pk)
  me = request.user

  if me != you:
    if me in you.followers.all():
      you.followers.remove(me)
      is_followed = False
    else:
      you.followers.add(me)
      is_followed = True
    context = {
      'is_followed': is_followed,
      'followings_count': you.followings.count(),
      'followers_count': you.followers.count(),
    }
    return JsonResponse(context)
  return redirect('accounts:profile', you.username)
```

```html
<!-- profile.html -->
<div>
  <div>
    팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span> / 
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
  </div>
  {% if request.user != person and request.user.is_authenticated %}
    <div>
      <form id="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <input type="submit" value="Unfollow">
        {% else %}
          <input type="submit" value="Follow">
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>

<!-- javascript -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  // 1. form 요소 선택
  const formTag = document.querySelector('#follow-form')
  // 6. csrftoken value 값 선택
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  // 2. form 요소에 이벤트 리스터 부착
  formTag.addEventListener('submit', function (event) {
    // 3. submit 이벤트 기본 동작 취소
    event.preventDefault()
    // 5. form 요소에 지정한 data 속성 접근하기
    const userId = formTag.dataset.userId
    // 4. axios 사용하여 비동기적으로 팔로우/언팔로우 요청
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then((response) => {
        // 7. Django에서 보낸 follow 여부를 알 수 있는 변수를 저장
        const isFollowed = response.data.is_followed
        // 8. 팔로우 버튼 조작
        const followBtn = document.querySelector('input[type=submit]')
        // 9. 팔로우 버튼 토글
        if (isFollowed === true) {
        followBtn.value = 'Unfollow'
        } else {
        followBtn.value = 'Follow'
        }

        // 10. 팔로워 / 팔로잉 수 처리
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')

        followingsCountTag.textContent = response.data.followings_count
        followersCountTag.textContent = response.data.followers_count
      })
      .catch((error) => {
        console.log(error)
      })
  })
</script>
```

## 💕 좋아요 구현
```py
# view.py
from django.http import JsonResponse

@login_required
def likes(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.user in article.like_users.all():
    article.like_users.remove(request.user)
    is_liked = False
  else:
    article.like_users.add(request.user)
    is_liked = True
  context = {
    'is_liked': is_liked,
  }
  return JsonResponse(context)
```

```html
<!-- index.html -->
<form class="like-forms" data-article-id="{{ article.pk }}">
  {% csrf_token %}
  {% if request.user in article.like_users.all %}
    <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
  {% else %}
    <input type="submit" value="좋아요" id="like-{{ article.pk }}">
  {% endif %}
</form>

<!-- javascript -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const formTags = document.querySelectorAll('.like-forms')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  formTags.forEach((formTag) => {
    formTag.addEventListener('submit', function (event) {
      event.preventDefault()

      const articleId = formTag.dataset.articleId

      axios({
        method: 'post',
        url: `/articles/${articleId}/likes/`,
        headers: {'X-CSRFToken': csrftoken,},
      })
        .then((response) => {
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          if (isLiked === true) {
            likeBtn.value = '좋아요 취소'
          } else {
            likeBtn.value = '좋아요'
          }
        })
        .catch((error) => {
          console.log(error)
        })
    })
  })
</script>
```