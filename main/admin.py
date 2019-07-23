from django.contrib import admin
from django.db import models
from .models import Tutorial
from datetime import datetime
from tinymce.widgets import TinyMCE 


class TutorialAdmin(admin.ModelAdmin):
	"""
	fields = [ "tutorial_title", 
				#"tutorial_published", 
				"tutorial_content" ] 
"""
	fieldsets = [
		("Title/date" , {"fields" : ["tutorial_title", "tutorial_published"] } ), 
		("Content" , {"fields": ["tutorial_content"]} )
	]

formfield_overrides = {
	models.TextField: {'widget': TinyMCE()}, 
}

#tutorial_published = models.DateTimeField('date published', default=datetime.now)
admin.site.register(Tutorial, TutorialAdmin)

