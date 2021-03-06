from django.test import TestCase
from django.urls import reverse


# All tests pass
# From assignment: We can’t easily test SnackDetailView just yet


class SnacksModelsTest(TestCase):


    def test_snack_list_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    # def test_snack_details_status(self):
    #     url = reverse('snack_details')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
        
    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        
    # def test_snack_details_template(self):
    #     url = reverse('snack_details')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_details.html')
        
    def test_base_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')