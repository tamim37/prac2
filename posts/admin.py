from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ("title","timestamp","updated")
	list_display_links = ("timestamp","updated")
	list_filter = ("timestamp","updated")
	search_fields = ("title","content")

	
		
admin.site.register(Post,PostModelAdmin)






#class PostModelAdmin(admin.ModelAdmin):
	
	

#	class Meta:
#		model=Comments

#admin.site.register(Comments,PostModelAdmin)



