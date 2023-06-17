from django.contrib import admin
from .models import ExpenseOrProceeds, Category, Transaction
from django.contrib.auth import get_user_model #od Adamsa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin #od Adamsa
from .forms import UserCreationForm #od Adamsa

#Kod Adamsa poniżej

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username', 'is_staff']
    list_filter = ['is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = ()

admin.site.unregister(User)
admin.site.register(User, UserAdmin) #wywalono UserAdmin

################################################################################

#admin.site.register(Account) # do wyrzucenia
admin.site.register(ExpenseOrProceeds) # do wyrzucenia
#admin.site.register(Category)
#admin.site.register(Transaction)

#@admin.register(Expense_proceeds)
#class Expense_proceedsAdmin(admin.ModelAdmin):
#        pass #list_display = ['id', 'expense_or_proceeds']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['transaction']
    list_display = ['id', 'expense_or_proceeds', 'transaction', 'category', 'amount', 'date_of_transaction']
    #Transaction.objects.order_by('-id')
    list_filter = ['expense_or_proceeds', 'category', 'date_of_transaction']
    list_editable = ['expense_or_proceeds', 'transaction', 'category', 'amount', 'date_of_transaction']
