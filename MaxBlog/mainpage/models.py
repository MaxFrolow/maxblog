from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

class PostAbstractModel(models.Model):
    created_datetime = models.DateTimeField(_('Creating time'), auto_now_add=True)
    update_datetime = models.DateTimeField(_('Last changing time'), auto_now_add=True)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name=_('Author'))

    class Meta:
        abstract = True



class Post(PostAbstractModel):
    CATEGORY_CHOICES =  (
        ('Web Design', 'Web Design'),
        ('JavaScript','JavaScript'),
        ('CSS', 'CSS'),
        ('Jquery', 'Jquery'),
    )
    title = models.CharField(_("Title"), max_length=200)
    second_title = models.CharField(_("Second Title"), max_length=200)
    text = models.TextField(_("News text"))
    category = models.CharField(_("Category"), max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(_("News image"), upload_to='news_images/', null=True, blank=False)
    likes = GenericRelation('likes.Like', related_name='post_likes')

    def __str__(self):
        return " ".join([str(self.created_datetime), self.title])

    class Meta:
        ordering = ('-created_datetime',)
        verbose_name = _("News")
        verbose_name_plural = _("News")



class Comment(PostAbstractModel):
    text = models.TextField(_('Post comment'))
    post = models.ForeignKey('mainpage.Post', on_delete=models.CASCADE, verbose_name=_('comment_post'))

    def __str__(self):
        return "Comment from {0} to post {1}".format(self.author.id, self.post.id)

    class Meta:
        ordering = ('created_datetime',)
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
