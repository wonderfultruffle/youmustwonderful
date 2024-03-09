from django.urls import path

from .views import list

app_label = "board"

# Resource 선별
# 1. Top level page: 게시판 목록
# 2. Topics - html로 각 글에 달린 댓글과 답글을 함께 표현
# 3. 

# 규칙1: 각 Topic의 URL은 'board/<topic_id>' 로 한다.
# 규칙2: 

urlpatterns = [
    path("", list, name="topic_list"),
    # path("board/<tp_id:int>", name="topic_detail"),
]
