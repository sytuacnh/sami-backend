from rest_framework import serializers
from .models import ContactMessageInfo
from django.core.mail import send_mail
from sami.settings import SEND_TO_EMAILS

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessageInfo
        fields = "__all__"

    def create(self, validate_data):
        instance = super(ContactMessageSerializer, self).create(validate_data)

        # print("before send email")
        sender_name = validate_data.get('name')
        content = validate_data.get('content')
        email = validate_data.get('email')
        
        send_mail(
            subject='{} Sent a Message from SaMi website'.format(sender_name),
            message='{0} said: \n\n{1}'.format(sender_name, content),
            from_email=email,
            recipient_list=SEND_TO_EMAILS,
            fail_silently=False,
        ) 

        return instance