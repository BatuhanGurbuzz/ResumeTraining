from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, SocialMedia, Document
# Create your views here.

def index(request):
    # General Settings Start #
    
    # Site Settings Start #
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter   
   
    # Site Settings End #
    
    # Home Settings Start #
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter   
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter   
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    
    # Home Settings End #
    
    # About Settings Start #
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    # about settings End #
    
    # Nav Setting Start # 
    nav_logo = GeneralSetting.objects.get(name='nav_logo').parameter
    # Nav Setting End #
    
    # General Settings End #
    
    # Image Settings Start #
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file
    
    # Image Settings End #
    
    # Skill Starts #
    
    skills = Skill.objects.all().order_by('order')
    
    
    # Skill Ends #
    
    # Social Media Starts #
    
    social_medias = SocialMedia.objects.all()
    
    # Social Media Ends #
    
    # Documents Starts #
    documents = Document.objects.all()
    # Documents Ends #
        
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name ,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome' : about_myself_welcome,
        'about_myself_footer':about_myself_footer,
        'home_banner_image':home_banner_image,
        'site_favicon':site_favicon,
        'nav_logo':nav_logo,
        'skills':skills,
        'social_medias':social_medias,
        'documents':documents,
    }
    
    
    return render(request, 'index.html', context = context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    
    return redirect(doc.file.url)
        

