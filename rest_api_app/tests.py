from django.test import TestCase
from .models import BucketList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse 
from django.contrib.auth.models import User
# Create your tests here.

class ModelTestCase(TestCase):

    def setUp(self):
        self.bucket_list_name = "my bucket list"
        user = User.objects.create(username="ashok")
        self.bucket_list = BucketList(name=self.bucket_list_name,owner=user)

    def testModelCreateBucket(self):
        oldCount = BucketList.objects.count()
        self.bucket_list.save()
        newCount = BucketList.objects.count()
        self.assertNotEqual(oldCount,newCount)

class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="ashok")
        self.client = APIClient()
        self.bucket_list_data = {'name':'ashok', 'owner': user.id}       
        self.response = self.client.post(
            reverse('home'),
            self.bucket_list_data,
            format = "json"
        ) 

    def testApiCreateBucketList(self):

        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def testAuthorizationIsEnforced(self):
       
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def testApiGetDetails(self):

        get_bucketlist = BucketList.objects.get(id=1)
        response = self.client.get(
           '/bucketlists/',
           kwargs={"pk":get_bucketlist.id},
           format="json"
        )

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertContains(response,get_bucketlist)

    def testApiUpdateDetails(self):
        bucketlist = BucketList.objects.get()
        change_bucketlist = {'name': 'Something'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testApiDeleteDetails(self):
        delete_bucketlist= BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': delete_bucketlist.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)