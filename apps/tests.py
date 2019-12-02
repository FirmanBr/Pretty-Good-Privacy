from django.test import TestCase
from django.contrib.auth.models import User
from apps.models import PairKeyReq

class ModelTest(TestCase):

    @classmethod
    def setUpClass(cls):

        super(ModelTest, cls).setUpClass()

        dept = PairKeyReq(fullname='Firman Brilian', email='firmanbriliant@gmail.com')
        dept.save()

        dept = PairKeyReq.objects.get(fullname='Firman Brilian')
        print('Added key data : ')
        print(dept)
        print('')

    def test_key_models(self):
        dept = PairKeyReq.objects.get(fullname='Firman Brilian')
        self.assertEqual(dept.email,'firmanbrilian@gmail.com')

#tes