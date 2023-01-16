import re

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.contrib.auth.models import User
from django.test import LiveServerTestCase, override_settings


NONCE_RE = re.compile(r"nonce-([^']+)")


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

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
    )
    def test_show_to_unauthenticated_with_default_value(self):
        """
        Since the default value of `ENVIRONMENT_SHOW_TO_UNAUTHENTICATED` is `True`, notice should be displayed
        """
        self.client.logout()  # make sure the user is not authenticated
        response = self.client.get("/admin/login/")
        self.assertContains(response, "<!-- Environment notice -->")

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
        ENVIRONMENT_SHOW_TO_UNAUTHENTICATED=True
    )
    def test_show_to_unauthenticated_set_to_true(self):
        """
        Since the value of `ENVIRONMENT_SHOW_TO_UNAUTHENTICATED` is `True`, notice should be displayed
        """
        self.client.logout()  # make sure the user is not authenticated
        response = self.client.get("/admin/login/")
        self.assertContains(response, "<!-- Environment notice -->")

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
        ENVIRONMENT_SHOW_TO_UNAUTHENTICATED=False
    )
    def test_show_to_unauthenticated_set_to_false(self):
        """
        Since the value of `ENVIRONMENT_SHOW_TO_UNAUTHENTICATED` is `False`, notice should not be displayed
        """
        self.client.logout()  # make sure the user is not authenticated
        response = self.client.get("/admin/login/")
        self.assertNotContains(response, "<!-- Environment notice -->")

    @override_settings(ENVIRONMENT_NAME="Production server", ENVIRONMENT_COLOR="#FF2222")
    def test_add_css_code_on_correct_settings(self):
        """ Should add correct css code if settings was provided """
        response = self.client.get("/admin/")
        self.assertContains(response, "<!-- Environment notice -->")
        self.assertContains(response, 'content: "Production server"')
        self.assertContains(response, "background-color: #FF2222")
        self.assertContains(response, "color: white")

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
        ENVIRONMENT_TEXT_COLOR="#00FF00",
    )
    def test_set_text_color(self):
        """ Should set correct text color if the setting was provided """
        response = self.client.get("/admin/")
        self.assertContains(response, "color: #00FF00")

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

    @override_settings(
        ENVIRONMENT_NAME="Production server",
        ENVIRONMENT_COLOR="#FF2222",
        CSP_INCLUDE_NONCE_IN=["style-src"],
    )
    def test_add_nonce_code_on_correct_settings(self):
        """ Should add correct css code if settings was provided """
        response = self.client.get("/admin/")
        csp_header = response["content-security-policy"]

        match = NONCE_RE.search(csp_header)
        if not match:
            raise AssertionError("CSP header does not contain a nonce")

        nonce = match.group(1)
        self.assertContains(response, 'nonce="%s"' % (nonce,))
