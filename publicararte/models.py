from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Tematica(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Tags(models.Model):
    nome = models.CharField(max_length=75)

    def __str__(self):
        return self.nome


def upload_to(instance, filename):
	return 'media/{filename}'.format(filename=filename)

class Arte(models.Model):
    TIPO_DE_ARQUIVO = [
        ('JPEG', 'JPEG'),
        ('JPG', 'JPG'),
        ('SVG', 'SVG'),
        ('PNG', 'PNG'),
        ('BPM', 'BPM'),
        ('TIFF', 'TIFF'),
        ('GIF', 'GIF'),
        ('EPS', 'EPS'),       
    ]

    nome = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=250, verbose_name="Descrição",blank=False)
    formato = models.CharField(max_length=4, choices=TIPO_DE_ARQUIVO,
                               default="Sem detalhes", blank=False)
    owner = models.ForeignKey('auth.user', related_name='artes', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    preco = models.FloatField(verbose_name="Preço",blank=False)
    foto = models.ImageField(_("Image"), height_field='image_width',
                             width_field='image_height', upload_to=upload_to,blank=False)
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    tematica = models.ForeignKey(
        Tematica, on_delete=CASCADE, verbose_name="Temática", blank=False)
    categoria = models.ForeignKey(
        Categoria, on_delete=CASCADE, blank=False)
    slug = models.SlugField(null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome
   

