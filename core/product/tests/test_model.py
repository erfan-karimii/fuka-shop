from django.test import TestCase
from ..models import Mobile
from model_bakery import baker

class TestProductModel(TestCase):
    def setUp(self):
        self.product_sample = baker.make(Mobile,name='test_name')

    def test_def_str(self):
        self.assertEqual(str(self.product_sample),'test_name')

