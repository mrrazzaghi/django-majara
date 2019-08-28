from django.db import models
from ckeditor.fields import RichTextField
from enumfields import EnumField
from enum import Enum
from django.core.files.storage import FileSystemStorage


def dir_media(file):
    return FileSystemStorage(location=f'H:/Programming/Django/django-majara/uploads/{file}/')


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

    title = models.CharField(blank=False, max_length=255, verbose_name='عنوان')
    slug = models.SlugField(blank=False, max_length=255, verbose_name='شناسه وب')
    image = models.ImageField(storage=dir_media('Category'), blank=False, verbose_name='عکس')
    description = models.TextField(blank=False, verbose_name='توضیحات')

    def __str__(self):
        return self.title


class Author(models.Model):
    class Meta:
        verbose_name_plural = 'نویسندگان'
        verbose_name = 'نویسنده'

    FirstName = models.CharField(blank=False, max_length=255, verbose_name='نام')
    LastName = models.CharField(blank=False, max_length=255, verbose_name='نام خانوادگی')
    Email = models.CharField(blank=False, max_length=70, verbose_name='ایمیل')
    mobile = models.CharField(blank=False, max_length=11, verbose_name='موبایل')
    avatar = models.ImageField(storage=dir_media('AuthorAvatar'), blank=False, verbose_name='آواتار')
    description = RichTextField(blank=True, verbose_name='توضیحات')


class StoryType(Enum):
    Text = 0
    Audio = 1
    Dialog = 2
    Image = 3
    labels = {
        Text: 'متنی',
        Audio: 'صوتی',
        Dialog: 'دیالوگ',
        Image: 'تصویری',
    }


class Story(models.Model):
    class Meta:
        verbose_name_plural = 'داستان ها'
        verbose_name = 'داستان'

    title = models.CharField(blank=False, max_length=255, verbose_name='عنوان')
    slug = models.CharField(blank=False, max_length=255, verbose_name='شناسه وب')
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='دسته بندی داستان')
    thumbNailImage = models.ImageField(storage=dir_media('Story-thumbNailImage'), blank=False, verbose_name='عکس کوچک')
    CoverImage = models.ImageField(storage=dir_media('Story-CoverImage'), blank=False, verbose_name='عکس کاور')
    headline = models.CharField(blank=False, max_length=255, verbose_name='سر تیتر')
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, verbose_name='نویسنده')
    hasAudio = models.BooleanField(default=True, verbose_name='فایل صوتی دارد؟')
    audioFile = models.FileField(blank=True, verbose_name='فایل صوتی')
    StoryType = EnumField(StoryType, blank=False, default=StoryType.Text)

    def __str__(self):
        return self.title


class TextStory(models.Model):
    class Meta:
        verbose_name_plural = 'محتوای داستان ها'
        verbose_name = 'محتوای داستان'

    storyId = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True, verbose_name='داستان')
    PageNumber = models.IntegerField(blank=False, default=0, verbose_name='شماره صفحه')
    PageContent = models.TextField(blank=False, verbose_name='محتوای صفحه')


class DialogTextType(Enum):
    Description = 0
    Dialog = 1
    labels = {
        Description: 'توضیحات',
        Dialog: 'دیالوگ',
    }


class DialogStory(models.Model):
    class Meta:
        verbose_name_plural = 'دیالوگ ها'
        verbose_name = 'دیالوگ'

    storyId = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True, verbose_name='داستان')
    dialogTextType = EnumField(DialogTextType, blank=False, default=DialogTextType.Description,
                               verbose_name='نوع متن دیالوگ')
    SayFrom = models.CharField(blank=False, max_length=50, verbose_name='شخص گوینده')
    SayTime = models.CharField(blank=False, max_length=10, verbose_name='زمان دیالوگ')
    SayText = models.TextField(blank=False, verbose_name='متن دیالوگ')
