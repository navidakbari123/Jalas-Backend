from django.contrib import admin

# Register your models here.
from poll.models import MeetingParticipant, Poll, Select, SelectUser, Comment

admin.site.register(MeetingParticipant)
admin.site.register(Poll)
admin.site.register(Select)
admin.site.register(SelectUser)
admin.site.register(Comment)
