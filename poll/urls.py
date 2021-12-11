from django.urls import path
from .views import home, create, vote, result

app_name = 'poll'

urlpatterns = [
    path( '', home, name='home' ),
    path( 'create', create, name='create' ),
    path( 'vote/<int:poll_id>', vote, name='vote' ),
    path( 'result/<int:poll_id>', result, name='result' ),
]
