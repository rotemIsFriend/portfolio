from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Project, Skill
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    for project in projects:
        if isinstance(project.technologies, str):
            project.technologies_list = project.technologies.split(",")
        else:
            project.technologies_list = project.technologies

    # Contact form handling
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email to yourself
            send_mail(
                f"New contact message from {name}",
                message,
                email,
                ['rotman1999@gmail.com'],
                fail_silently=False,
            )

            # Send a confirmation email to the user
            send_mail(
                'Thank you for contacting me!',
                f"Hi {name},\n\nThank you for reaching out! I'll get back to you soon.\n\nBest regards,\nRotem Haver",
                'rotman1999@gmail.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'success': True})

        # Form errors handling
        return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'myPortfolio/home.html', {'projects': projects, 'skills': skills, 'form': ContactForm()})