

# tests.py

# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from .models import SignUp
# from .forms import CreatUserForm
# from django.test import TestCase
# from django.urls import reverse
# from .forms import CreatUserForm
# from django.test import TestCase
# from .models import Apartments
# from django.test import TestCase
# from .forms import CreatUserForm
# from django.test import TestCase
# from .models import SignUp
# from .forms import addApartmentForm
# from django.contrib.auth.models import User, Group
# from .views import SignUpUser

# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls import reverse


# from django.urls import reverse


# class UserTestCase(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password1': 'testpassword',
#             'password2': 'testpassword'
#         }

#     def test_signup_user(self):
#         response = self.client.post(reverse('SignUpUser'), self.user_data)
#         self.assertEqual(response.status_code, 302)  # Check if redirecting after successful signup

#     def test_login_user(self):
#         user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
#         login_data = {'username': 'testuser', 'password': 'testpassword'}
#         response = self.client.post(reverse('Loginuser'), login_data)
#         self.assertEqual(response.status_code, 302)  # Check if redirecting after successful login

#     def test_invalid_login_user(self):
#         login_data = {'username': 'wronguser', 'password': 'wrongpassword'}
#         response = self.client.post(reverse('Loginuser'), login_data)
#         self.assertEqual(response.status_code, 200)  # Check if staying on login page after unsuccessful login

#     def test_create_user_form_valid(self):
#         form = CreatUserForm(data=self.user_data)
#         self.assertTrue(form.is_valid())  # Check if form with valid data is considered valid

#     def test_create_user_form_invalid(self):
#         # Intentionally pass invalid data to the form
#         invalid_data = self.user_data.copy()
#         invalid_data['password2'] = 'differentpassword'
#         form = CreatUserForm(data=invalid_data)
#         self.assertFalse(form.is_valid())  # Check if form with invalid data is considered invalid

        

#     def test_login_view(self):
#         # יבדוק כי הנתיב להתחברות מחזיר קוד תקין
#         url = reverse('Loginuser')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_logout_view(self):
#         # יבדוק כי הנתיב להתנתקות מחזיר קוד תקין
#         url = reverse('Logoutuser')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)




# class SignUpUserViewTest(TestCase):
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/signupuser/')
#         self.assertEqual(response.status_code, 200)

#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('signupuser'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'pages/SignUpUser.html')

#     def test_signup_form(self):
#         response = self.client.get(reverse('signupuser'))
#         self.assertIsInstance(response.context['form'], CreatUserForm)
#         self.assertTrue('form' in response.context)

#     def test_form_submission(self):
#         form_data = {'username': 'testuser', 'password': '12345'}
#         response = self.client.post(reverse('signupuser'), form_data)
#         # Check the response code or redirection after form submission


# class ApartmentsModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Apartments.objects.create(name='Test Apartment', price=1000)

#     def test_name_label(self):
#         apartment = Apartments.objects.get(id=1)
#         field_label = apartment._meta.get_field('name').verbose_name
#         self.assertEquals(field_label, 'name')

#     def test_price_label(self):
#         apartment = Apartments.objects.get(id=1)
#         field_label = apartment._meta.get_field('price').verbose_name
#         self.assertEquals(field_label, 'price')



# class CreatUserFormTest(TestCase):
#     def test_form_validity(self):
#         form_data = {'username': 'testuser', 'password': 'fakepassword'}
#         form = CreatUserForm(data=form_data)
#         self.assertTrue(form.is_valid())


# class LoginTestCase(TestCase):
#     def setUp(self):
#         self.credentials = {
#             'username': 'testuser',
#             'password': 'secret'}
#         User.objects.create_user(**self.credentials)




# class UserGroupTest(TestCase):
#     def setUp(self):
#         # Create a group named 'Users'
#         self.group = Group.objects.create(name='Users')

#     def test_user_group_assignment(self):
#         # Simulate form submission with user data
#         self.client.post('/signupuser/', {'username': 'testuser', 'password1': 'pass1234', 'password2': 'pass1234'})
#         user = User.objects.get(username='testuser')
#         # Check if user is assigned to 'Users' group
#         self.assertTrue(user.groups.filter(name='Users').exists())


# class LogoutRedirectTest(TestCase):
#     def test_logout_redirect(self):
#         # Assuming you have a logout view that redirects to home page after logout
#         response = self.client.get('/logout/')
#         self.assertRedirects(response, '/home/', status_code=302, target_status_code=200)




# class SessionTest(TestCase):
#     def test_login_session(self):
#         user = User.objects.create_user(username='testuser', password='12345')
#         self.client.login(username='testuser', password='12345')
#         # Check if user_id is stored in session
#         self.assertEqual(self.client.session['_auth_user_id'], str(user.pk))














from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CreatUserForm
from .views import SignUpUser, Loginuser, logoutAdmin, SignUpStudent, logoutstudent, Loginstudent, Logiadmin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from .models import PrivateClasses, PrivateMechanicalClasses, PrivateCivilClasses, PrivateChemicalClasses, PrivateElectricClasses, Apartments, scholarship


class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }

    def test_signup_user_success(self):
        response = self.client.post(reverse('SignUpUser'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())  # Check if user exists

    def test_signup_user_invalid_form(self):
        invalid_user_data = {'username': 'testuser'}
        response = self.client.post(reverse('SignUpUser'), invalid_user_data)
        self.assertEqual(response.status_code, 200)  # Reloads signup page
        self.assertFalse(User.objects.filter(username=invalid_user_data['username']).exists())  # User should not exist

    def test_login_user_success(self):
        # Create a user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        response = self.client.post(reverse('Loginuser'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # User should be logged in

    def test_login_user_invalid_credentials(self):
        response = self.client.post(reverse('Loginuser'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Stay on login page after unsuccessful login
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should not be logged in

    def test_logout_user(self):
        # Log in a user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logoutuser'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should be logged out

    def test_signup_form_valid(self):
        form = CreatUserForm(data=self.user_data)
        self.assertTrue(form.is_valid())  # Form should be valid with valid data

    def test_signup_form_invalid(self):
        invalid_user_data = {'username': 'testuser'}
        form = CreatUserForm(data=invalid_user_data)
        self.assertFalse(form.is_valid())  # Form should be invalid with incomplete data

    def test_logout_admin(self):
        response = self.client.get(reverse('logoutAdmin'))
        self.assertEqual(response.status_code, 200)  # Log out without being logged in, should return 200

    def test_signup_student_success(self):
        response = self.client.post(reverse('SignUpStudent'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())  # Check if user exists

    def test_logout_student(self):
        response = self.client.get(reverse('logoutstudent'))
        self.assertEqual(response.status_code, 200)  # Log out without being logged in, should return 200

    def test_login_student_success(self):
        # Create a student user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        student_group = Group.objects.create(name='Students')
        student_group.user_set.add(user)
        response = self.client.post(reverse('Loginstudent'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # User should be logged in

    def test_login_admin_success(self):
        # Create an admin user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        admin_group = Group.objects.create(name='Admin')
        admin_group.user_set.add(user)
        response = self.client.post(reverse('Logiadmin'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # User should be logged in


class ViewsTestCase(TestCase):
    def test_masterpage_view(self):
        response = self.client.get(reverse('masterpage'))
        self.assertEqual(response.status_code, 200)  # Check if page loads successfully

    # Add tests for other views similarly


class ModelsTestCase(TestCase):
    def setUp(self):
        # Set up objects as needed for testing
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_creation(self):
        self.assertTrue(User.objects.filter(username='testuser').exists())

    # Add tests for other models similarly


class FormsTestCase(TestCase):
    def test_CreatUserForm(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CreatUserForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid with valid data

    # Add tests for other forms similarly


class OtherTests(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)  # Example test, remove it when adding real tests





class UserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }

    def test_signup_user(self):
        response = self.client.post(reverse('SignUpUser'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Check if redirecting after successful signup

    def test_login_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        login_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('Loginuser'), login_data)
        self.assertEqual(response.status_code, 302)  # Check if redirecting after successful login

    def test_invalid_login_user(self):
        login_data = {'username': 'wronguser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('Loginuser'), login_data)
        self.assertEqual(response.status_code, 200)  # Check if staying on login page after unsuccessful login

    def test_create_user_form_valid(self):
        form = CreatUserForm(data=self.user_data)
        self.assertTrue(form.is_valid())  # Check if form with valid data is considered valid

    def test_create_user_form_invalid(self):
        # Intentionally pass invalid data to the form
        invalid_data = self.user_data.copy()
        invalid_data['password2'] = 'differentpassword'
        form = CreatUserForm(data=invalid_data)
        self.assertFalse(form.is_valid())  # Check if form with invalid data is considered invalid

        

    def test_login_view(self):
        # יבדוק כי הנתיב להתחברות מחזיר קוד תקין
        url = reverse('Loginuser')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        # יבדוק כי הנתיב להתנתקות מחזיר קוד תקין
        url = reverse('Logoutuser')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)








