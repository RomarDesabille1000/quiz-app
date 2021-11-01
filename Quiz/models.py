from django.template.defaultfilters import slugify
from django.db import models
from Account.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField()

    def __str__(self):
        return self.name

class Quizzes(models.Model):
    title = models.CharField(max_length=200, verbose_name='Quiz Title')
    slug = models.SlugField(unique=True, null=True)
    time_limit = models.IntegerField(verbose_name='Time Limit (minutes): ')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Lists'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title

    def save(self):
        super(Quizzes, self).save()
        if not self.slug:
            slug = slugify(self.title)
            try:
                post_obj = Quizzes.objects.get(slug=slug)
                slug += "-" + str(self.id)
            except Quizzes.DoesNotExist:
                pass
            self.slug = slug
            self.save()

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name='Last updated', auto_now_add=True)

    class Meta:
        abstract = True

class Questions(Updated):

    class Meta:
        ordering = ['id']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    TYPE = (
        (0, 'Multiple Choice'),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name='Type of Question')
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Title')

    def __str__(self):
        return self.title

class Answer(Updated):
    class Meta:
        ordering = ['id']
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Results(models.Model):
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    date_taken = models.DateTimeField(null=True, blank=True)
    quiz_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.quiz.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Results'
        verbose_name_plural = 'Results'

class Crud(models.Model):
    class Meta:
        verbose_name_plural = 'Crud'

    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)


