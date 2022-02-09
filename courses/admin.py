from atexit import register
from django.contrib import admin
from courses.models import Course,Tag,Learing,Prerequisite,Video
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearingAdmin(admin.TabularInline):
    model = Learing

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearingAdmin,PrerequisiteAdmin,VideoAdmin]

admin.site.register(Course , CourseAdmin)
admin.site.register(Video)
