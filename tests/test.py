try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.contrib.auth.models import User
from django.test import LiveServerTestCase, override_settings


class AdminEnvironmentTestCase(LiveServerTestCase):

    def login_user(self):
        """ Login to admin part """
        self.superuser = User.objects.create_superuser(username='root', email='root@e.co', password='123123')
        self.client.post('/admin/login/', dict(username=self.superuser.username, password='123123'))

    def setUp(self):
        super(AdminEnvironmentTestCase, self).setUp()
        self.login_user()

    def test_show_nothing_if_no_settings(self):
        """ Should not display anything if there is no settings """
        response = self.client.get("/admin/")
        self.assertNotContains(response, "<!-- Environment notice -->")

    @override_settings(ENVIRONMENT_NAME="Production server", ENVIRONMENT_COLOR="#FF2222")
    def test_add_css_code_on_correct_settings(self):
        """ Should add correct css code if settings was provided """
        response = self.client.get("/admin/")
        self.assertContains(response, "<!-- Environment notice -->")
        self.assertContains(response, 'content: "Production server"')
        self.assertContains(response, "background-color: #FF2222")

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222"
    )
    def test_use_body_as_admin_selector_if_no_setting(self):
        """ Should use body as selector if settings was not provided """
        response = self.client.get('/admin/')
        self.assertContains(response, 'body:before {')

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
        ENVIRONMENT_ADMIN_SELECTOR='.container'
    )
    def test_add_admin_selector_code_on_correct_settings(self):
        """ Should use the selector if settings was provided """
        response = self.client.get('/admin/')
        self.assertContains(response, '.container:before {')

    @override_settings(ENVIRONMENT_NAME="Production server", ENVIRONMENT_COLOR="#FF2222")
    def test_should_work_on_other_admin_pages(self):
        """ Should include css code to other admin pages as well """
        urls = [
            reverse("admin:auth_user_change", args=(self.superuser.pk,)),
            reverse("admin:auth_user_delete", args=(self.superuser.pk,)),
            reverse("admin:auth_user_changelist"),
            reverse("admin:auth_user_add"),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertContains(response, "<!-- Environment notice -->")
