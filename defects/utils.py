from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_mail_view(email):
    subject = 'You have assigned a defect complete ASAP'
    message = 'The given High Priority Defect need to complete'
    from_email = 'pramodr2101@gmail.com' # Must mathch DEFAULT_FROM_EMAIL
    recipient_list = [email] # Email address of the recipient

    #Render HTML email from template

    html_message = render_to_string('defects/task_email_template.html')
    #Create plain text version by stripping HTML tags
    plain_message = strip_tags(html_message)

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error while sending enaim: {str(e)}")