from django.test import TestCase
from .models import BucketList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self):
        self.bucket_list_name = "my bucket list"
        self.bucket_list = BucketList(name=self.bucket_list_name)

    def testModelCreateBucket(self):
        oldCount = BucketList.objects.count()
        self.bucket_list.save()
        newCount = BucketList.objects.count()
        self.assertNotEqual(oldCount,newCount)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.bucket_list_data = {'name':'TEST'}
        self.response = self.client.post(
            reverse('create'),
            self.bucket_list_data,
            format = "json"
        ) 

    def testApiCreateBucketList(self):
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)
