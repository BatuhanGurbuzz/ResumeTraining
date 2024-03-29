from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, SocialMedia, Document


# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj

def layout(request):
    # General Settings Start #

    # Site Settings Start #
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')

    # Site Settings End #

    # Home Settings Start #
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')

    # Home Settings End #

    # About Settings Start #
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')
    # about settings End #

    # Nav Setting Start # 
    nav_logo = get_general_setting('nav_logo')
    # Nav Setting End #

    # General Settings End #

    # Image Settings Start #
    home_banner_image = get_image_setting('home_banner_image')
    site_favicon = get_image_setting('site_favicon')

    # Image Settings End #

    # Skill Starts #

    skills = Skill.objects.all()

    # Skill Ends #

    # Social Media Starts #

    social_medias = SocialMedia.objects.all()

    # Social Media Ends #

    # Document Starts #

    documents = Document.objects.all()

    # Document Ends #

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'nav_logo': nav_logo,
        'skills': skills,
        'social_medias': social_medias,
        'documents': documents,
    }
    return context


def index(request):
    return render(request, 'index.html')


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)

    return redirect(doc.file.url)
