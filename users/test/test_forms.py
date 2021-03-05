
from django.test import TestCase

from ..forms import NewUserForm, UserLoginForm

class TestNewUserForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = NewUserForm(auto_id="id_register_%s")

    def test_username_field(self):
        self.assertEqual(
            self.form['username'].auto_id, 'id_register_username'
        )
        self.assertEqual(
            self.form['username'].field.widget.attrs['placeholder'],
            'Username'
        )

    def test_password1_field(self):
        self.assertEqual(
            self.form['password1'].auto_id, 'id_register_password1'
        )
        self.assertEqual(
            self.form['password1'].field.widget.attrs['placeholder'],
            'Password'
        )

    def test_password2_field(self):
        self.assertEqual(
            self.form['password2'].auto_id, 'id_register_password2'
        )
        self.assertEqual(
            self.form['password2'].field.widget.attrs['placeholder'],
            'Password Confirmation'
        )

class TestUserLoginForm(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = UserLoginForm(auto_id="id_login_%s")
        cls.username_field = cls.form['username']
        cls.password_field = cls.form['password']

    def test_username_field(self):
        self.assertEqual(self.username_field.auto_id, 'id_login_username')
        self.assertEqual(
            self.username_field.field.widget.attrs['placeholder'], 'Username'
        )


    def test_password_field(self):
        self.assertEqual(self.password_field.auto_id, 'id_login_password')
        self.assertEqual(
            self.password_field.field.widget.attrs['placeholder'], 'Password'
        )
