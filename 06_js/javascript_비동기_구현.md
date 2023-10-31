# :whale2: 자바스크립트 비동기 : axios

[🧸 팔로우 구현](#-팔로우-구현)

[💕 좋아요 구현](#-좋아요-구현)

---

## 🧸 팔로우 구현
```py
# views.py
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
# views.py
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
    'count': article.like_users.count(),
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
<p>
  <span id="like-count-{{ article.pk }}">{{ article.like_users.all|length }}</span>명이 이 글을 좋아합니다.
</p>


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
          // likeButton.innerText = liked ? '좋아요 취소' : '좋아요'

          const likeCount = document.querySelector(`#like-count-${articleId}`)
          const count = response.data.count

          likeCount.innerText = count

        })
        .catch((error) => {
          console.log(error)
        })
    })
  })
</script>
```

## 💕 댓글 구현
```py
# views.py
import json

@require_POST
def comments_create(request, pk):
  if request.user.is_authenticated:
    article = get_object_or_404(Article, pk=pk)

    # 1. 클라이언트에서 data 속성을 일반 json 객체로 보냈을 경우
    # request.body 안의 json 데이터 뽑아서 처리후 사용
    json_data = json.loads(request.body)
    comment_form = CommentForm(json_data)
    
    # 2. 클라이언트에서 data 속성을 FormData 객체로 보냈을 경우
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            "commentPk": comment.pk 
        }
        return JsonResponse(context, status=200)
    return redirect('articles:detail', article.pk)
  return redirect('accounts:login')
```

```html
<!-- detail.html -->
<ul id="comment-list">  <!-- id 추가 -->
  {% for comment in comments %}
    <!-- 생략 -->
    <p id="no-comment">댓글이 없어요..</p>  <!-- id 추가 -->
  {% endfor %}
</ul>

{% if request.user.is_authenticated %}
  <form id="comment-form" data-article-id="{{ article.pk }}">  <!-- id 추가 -->
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>

<!-- javascript -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const form = document.querySelector('#comment-form')
  const input = document.querySelector('[name=content]')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  // 댓글 달기위한 부모 노드
  const ul = document.querySelector('#comment-list')

  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const content = input.value  // 댓글 입력
    const articleId = event.target.dataset.articleId
    const baseURL = "http://127.0.0.1:8000/"

    // 1. data 속성을 일반 json 객체로 보내주기
    const data = {
      "content": content
    }
    // 2. FormData 객체 사용
    const data = new FormData()
    data.append("content", content)

    axios({
      method: 'post',
      baseURL,
      url: `articles/${ articleId }/comments/`,
      headers: {'X-CSRFToken': csrftoken,},
      data,
    }).then(response => {
      const {commentPk} = response.data
      
      // 댓글 객체 생성
      const li = document.createElement("li")
      li.innerHTML = `
      {{ user.username }} - ${content}
      <form action="/articles/${articleId}/comments/${commentPk}/delete/" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      `

      // 댓글 생성시 노코멘트 문구 삭제
      const nc_p = document.querySelector('#no-comment')
      if (nc_p) {
        ul.removeChild(nc_p)
      }

      // 댓글 추가
      ul.appendChild(li)

      // 인풋 초기화
      input.value = ""
    })
  })
</script>
```
