from django.conf.urls import include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy

urlpatterns = [
    # Examples:
    # url(r'^$', 'pycon_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^libadmin/', include(admin.site.urls)),
]

# Change Admin Site Title
admin.site.site_title = ugettext_lazy('PyCon Library Admin')
# Change the <h1> for the Admin
admin.site.site_header = ugettext_lazy('PyCon Library Administration')
# Text to put at the top of the admin index page.
admin.site.index_title = ugettext_lazy('PyCon Library Administration')
