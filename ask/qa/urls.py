from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'test'), 
    url(r'^question/(?P<pk>\d+)/', question_detail),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^login/', user_login, name='login'),
    url(r'^new/', test, name='new'),
]
