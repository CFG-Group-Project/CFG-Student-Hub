from django.test import TestCase
from .models import *

class MaterialTestCase(TestCase):
    def setUp(self):
        Material.objects.create(lesson='good', week=2, slides='<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQsjjAoDSvnZHB7PeUeq2KN8MbGPof812NuvTA157NiGAR7tZpzxU_UT6cSGsDnIeCoe4SNB5NYClAT/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>')
        Material.objects.create(lesson='bad',week=2)

    def test_material_model(self):
        """testing if the models are being filled corrextly and auto-filling defaults correctly"""
        good = Material.objects.get(lesson='good')
        bad = Material.objects.get(lesson='bad')
        self.assertFalse(good.show)
        self.assertEqual(good.lesson,'good')
        self.assertEqual(good.week,2)
        self.assertRaises(TypeError,bad.week,'www')
        self.assertRaises(TypeError,bad.program,'www')