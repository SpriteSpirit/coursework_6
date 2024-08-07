from django.urls import path
from django.views.decorators.cache import cache_page

from mailing_service.views import dashboard, ClientListView, MailingListView, MailingCreateView, MailingUpdateView, \
    MessageCreateView, MessageListView, ClientCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingDetailView, MailingDeleteView, ClientDetailView, ClientUpdateView, ClientDeleteView, MailingLogListView, \
    toggle_mailing, moderator_dashboard
from mailing_service.apps import MailingServiceConfig


app_name = MailingServiceConfig.name


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # кеширование убрала потому что можно снова попасть в ЛК
    path('moderator_dashboard/', moderator_dashboard, name='moderator_dashboard'),

    path('client_list/', cache_page(5)(ClientListView.as_view()), name='client_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('view_client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('mailing_list/', cache_page(5)(MailingListView.as_view()), name='mailing_list'),
    path('create_mail/', MailingCreateView.as_view(), name='create_mail'),
    path('view_mail/<int:pk>', MailingDetailView.as_view(), name='view_mail'),
    path('update_mail/<int:pk>/', MailingUpdateView.as_view(), name='update_mail'),
    path('delete_mail/<int:pk>/', MailingDeleteView.as_view(), name='delete_mail'),

    path('message_list/', cache_page(5)(MessageListView.as_view()), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('log_list/', cache_page(5)(MailingLogListView.as_view()), name='log_list'),
    path('toggle_mailing/<int:pk>', toggle_mailing, name='toggle_mailing'),
]
