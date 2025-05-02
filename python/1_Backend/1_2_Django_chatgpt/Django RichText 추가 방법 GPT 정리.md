### CKEditor 설정 및 이미지 루트 설정

1. **설치**
   ```sh
   pip install django-ckeditor
   ```

2. **Django 설정 (`settings.py`)**
   ```python
   INSTALLED_APPS += ['ckeditor', 'ckeditor_uploader']
   CKEDITOR_UPLOAD_PATH = "uploads/"
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **모델 설정 (`models.py`)**
   ```python
   from ckeditor_uploader.fields import RichTextUploadingField
   class Notice(models.Model):
       title = models.CharField(max_length=255)
       content = RichTextUploadingField()
   ```

4. **URL 설정 (`urls.py`)**
   ```python
   from django.conf import settings
   from django.conf.urls.static import static
   from django.urls import path, include
   urlpatterns = [
       path('ckeditor/', include('ckeditor_uploader.urls')),
   ]
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

---

### Quill.js 설정 및 이미지 루트 설정

1. **설치**
   ```sh
   pip install django-quill-editor
   ```

2. **Django 설정 (`settings.py`)**
   ```python
   INSTALLED_APPS += ['django_quill']
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **모델 설정 (`models.py`)**
   ```python
   from django_quill.fields import QuillField
   class Notice(models.Model):
       title = models.CharField(max_length=255)
       content = QuillField()
   ```

4. **템플릿에서 사용**
   ```html
   {{ form.media }}
   ```

---

### TinyMCE 설정 및 이미지 루트 설정

1. **설치**
   ```sh
   pip install django-tinymce
   ```

2. **Django 설정 (`settings.py`)**
   ```python
   INSTALLED_APPS += ['tinymce']
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **모델 설정 (`models.py`)**
   ```python
   from tinymce.models import HTMLField
   class Notice(models.Model):
       title = models.CharField(max_length=255)
       content = HTMLField()
   ```

4. **URL 설정 (`urls.py`)**
   ```python
   urlpatterns += [path('tinymce/', include('tinymce.urls'))]
   ```

---

### Summernote 설정 및 이미지 루트 설정

1. **설치**
   ```sh
   pip install django-summernote
   ```

2. **Django 설정 (`settings.py`)**
   ```python
   INSTALLED_APPS += ['django_summernote']
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

3. **모델 설정 (`models.py`)**
   ```python
   from django_summernote.fields import SummernoteTextField
   class Notice(models.Model):
       title = models.CharField(max_length=255)
       content = SummernoteTextField()
   ```

4. **URL 설정 (`urls.py`)**
   ```python
   urlpatterns += [path('summernote/', include('django_summernote.urls'))]
   ```

---
## 기본 코드 정리
```python
# models.py
from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    is_deleted = models.BooleanField(default=False, verbose_name="삭제 여부")
    is_pinned = models.BooleanField(default=False, verbose_name="고정 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "공지"
        verbose_name_plural = "공지사항"

    def __str__(self):
        return self.title
```


```python
# serializers.py
from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
	class Meta:
	model = Notice
	fields = 
	\\\\







\
```