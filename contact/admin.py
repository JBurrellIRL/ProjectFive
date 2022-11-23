from django.contrib import admin
from .models import Contact, ContactNotes
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'replied_to',
    )


class ContactNotesAdmin(SummernoteModelAdmin):
    summernote_fields = ('reply_sent')
    list_display = (
        'related_message',
        'date',
        'replied_to',
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactNotes, ContactNotesAdmin)
