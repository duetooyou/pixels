from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from rest_framework.test import APITestCase, APIRequestFactory
from .views import PixelCountView


class CountBlackWhitePixelsTest(APITestCase):
    def test_counting_black_white_pixels(self):
        filename = 'example.png'
        factory = APIRequestFactory()
        data = File(open('media/picture/example.png', 'rb'))
        upload_file = SimpleUploadedFile(filename, data.read(),
                                         content_type='multipart/form-data')
        request = factory.put('/pixels/',
                              {'file': upload_file},
                              content_type="application/json",
                              content_disposition="attachment; filename=aaa")
        view = PixelCountView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
