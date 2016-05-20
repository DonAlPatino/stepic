from django.conf.urls import url
from qa.views import test, question_list, question_detail, popular

urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', test, name='signup'),
    url(r'^login/', test, name='login'),
    url(r'^logout/', test, name='logout'),
    url(r'^new/', test, name='new'),
]
