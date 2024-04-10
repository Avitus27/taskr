from datetime import timedelta, datetime
from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_next = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # This should show/hide the repeat days field
    repeats = models.BooleanField(default=True)
    repeat_days = models.SmallIntegerField(
        default=1, verbose_name="Repeat every _ days", validators=[MinValueValidator(1)])
    complete = models.BooleanField(default=False)

    def is_overdue(self) -> bool:
        return self.due_next < timezone.now()

    def __str__(self) -> str:
        return self.title

    def clean(self, *args, **kwargs):
        # HT: https://stackoverflow.com/a/12188214
        # run the base validation
        super(Task, self).clean(*args, **kwargs)

        # Don't allow dates older than now.
        if self.due_next < timezone.now():
            raise ValidationError(
                'Tasks can only be planned for a future time.')

    # TODO: Use timezone type built into django
    def mark_done(self):
        try:
            if (self.repeats):
                # don't mark as complete, just update the next due date
                self.due_next = datetime.combine(timezone.now().date(), self.due_next.time()) + \
                    timedelta(self.repeat_days)
                return (True, False)
            else:
                # mark as complete
                self.complete = True
                return (True, True)
        except:
            return (False, False)
