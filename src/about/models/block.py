from django.db import models
from common.models.base import BaseModel


class Block(BaseModel):
    """
    Block on the website
    """
    BLOCKTYPES = (
        ('About us', 'About us'),
        ('Our vision', 'Our vision'),
        ('Our mission', 'Our mission'),
        ('Res. & Dev.', 'Res. & Dev'),
    )

    LANGUAGES = (
        ('Eng', 'English'),
        ('Tur', 'Turkish'),
    )

    title = models.CharField(
        max_length=1000000,
        unique=True,
        verbose_name='Post title'
    )
    blocktype = models.CharField(
        max_length=20,
        choices=BLOCKTYPES,
        verbose_name='Block type'
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGES,
        default='Eng',
        verbose_name='Language'
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'


class BlockPhoto(BaseModel):
    """
    Block photo
    """
    post = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Block'
    )
    photo = models.ImageField(
        upload_to='blocks/photos/',
        verbose_name='Photo'
    )

    class Meta:
        verbose_name = 'Block photo'
        verbose_name_plural = 'Block photos'


class BlockVideo(BaseModel):
    """
    Block video
    """
    post = models.ForeignKey(
        Block,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Block'
    )
    video = models.FileField(
        upload_to='blocks/videos/',
        verbose_name='Video'
    )

    class Meta:
        verbose_name = 'Block video'
        verbose_name_plural = 'Block videos'
