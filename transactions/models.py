from django.db import models
from django.contrib.auth.models import ( #od Adamsa
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth import get_user_model

"""
class Account(models.Model):
    login = models.CharField(max_length=100)
    password = models.TextField()
    email = models.EmailField()

    USERNAME_FIELD = 'login'
"""
User = get_user_model()

############################################################
#od Adamsa

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, email, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        if not username:
            raise ValueError('Superuser must have a username')
        if not email:
            raise ValueError('Superuser must have an email address')

        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        null = False,
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] # Only username & password are required by default.

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    def is_superuser(self):
        return self.admin

#do Adamsa
##########################################################################

class ExpenseOrProceeds(models.Model): #wydatek lub przychód
    pass

class Category(models.Model): #kategorie wydatku lub przychodu
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model): #transakcje

    EXPENSE = 'EXP'
    PROCEEDS = 'PRO'
    ExpenseOrProceedsChoices = [
        (EXPENSE, 'Expense'),
        (PROCEEDS, 'Proceeds')
    ]
    expense_or_proceeds = models.CharField(
        max_length=3,
        choices=ExpenseOrProceedsChoices,
        default=EXPENSE,
    )

    transaction = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_of_transaction = models.DateField()

    #Index(Lower("id").asc())

    def __str__(self):
        return self.transaction
