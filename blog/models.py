from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class Post(models.Model):
    class TypeOfPicture(models.TextChoices):
        OPENING = 'OP', _('Portes et Fenêtres')
        BOOKSHELF = 'BS', _('Bibliothèques')
        DRESSING = 'DR', _('Dressings')
        OTHERS = 'OT', _('Autres')

    type_of_picture = models.CharField(
        max_length = 2,
        choices = TypeOfPicture.choices,
        default = TypeOfPicture.OPENING,
        name = "type_image",
    )

    titre = models.CharField(max_length=200)
    description = models.CharField(max_length = 10000)
    image = models.ImageField(upload_to = 'images/', blank = True)
    pub_date = models.DateTimeField('date de publication')

    def __str__(self):
        return self.titre
