# # from django.contrib.auth.models import User
# from django.apps import AppConfig
# from django.db.models.signals import post_save
# from django.utils.translation import ugettext_lazy as _

# class ProfilesConfig(AppConfig):
#     name = 'accounts'
#     verbose_name = _('accounts')

#     def ready(self):
#         import accounts.signals  # noqa


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ProfilesConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('accounts')

    def ready(self):
        import accounts.signals