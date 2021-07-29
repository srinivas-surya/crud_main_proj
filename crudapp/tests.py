from django.test import TestCase
from .models import ProfileData

# models test


class ProfileModelTestCase(TestCase):
    ''' writing test case for model '''

    def create_profile_data(self):
        ''' creating model object using custom data'''
        return ProfileData.objects.create(name="srini",
                                        past_address="visakhapatnam",
                                        present_address="chennai",
                                        phone_number="9908944927")

    def test_whatever_creation(self):
        w = self.create_profile_data()
        self.assertTrue(isinstance(w, ProfileData))
        ''' test the model object whatever we created earlier'''
        self.assertEqual(w.__unicode__(), w.name)

