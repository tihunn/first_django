from django.db import models
from django.urls import reverse


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Famous woman"
        verbose_name_plural = "Famous women"
        ordering = ["time_create", "title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="category")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["id"]
