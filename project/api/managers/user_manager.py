from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        is_staff = kwargs.pop('is_staff', False)
        is_super_user = kwargs.pop('is_super_user', False)

        user = self.model(
            email = email,
            is_active = True,
            is_staff=is_staff,
            is_super_user=is_super_user,
            ** kwargs
        )

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_user(self,email, password=None, **extra_fields):
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)




