from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        return user

    def create_user(self, email, password):
        return self._create_user(email, password)

    def create_superuser(self, email, password):
        return self._create_user(email, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилие")
    email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    avatar = models.ImageField(upload_to='user_avatars/', verbose_name="Аватар")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return '%s. %s %s' % (self.id, self.name, self.surname)


class Rating(models.Model):
    from_user = models.ForeignKey(User, related_name="from_people", on_delete=models.CASCADE, verbose_name="Лайк от")
    to_user = models.ForeignKey(User, related_name="to_people", on_delete=models.CASCADE, verbose_name="Лайк для")

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [
            models.CheckConstraint(
                check=~models.Q(from_user=models.F('to_user')),
                name='users_cannot_rate_themselves'
            ),
        ]

    def __str__(self):
        return '%s. %s %s' % (self.id, self.from_user, self.to_user)
