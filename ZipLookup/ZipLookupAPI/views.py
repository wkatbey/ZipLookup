from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ZipLookupSerializer
import requests



class ZipLookup(APIView):
    base_url = "https://secure.shippingapis.com/ShippingAPI.dll?API=ZipCodeLookup&XML="


    def post(self, request, format=None):
        request_xml = request.requestXml
        full_url = base_url + request_xml

        response = requests.post(baseUrl, full_url)

        serializer = ZipLookupSerializer(response.content)

        return serializer.data








