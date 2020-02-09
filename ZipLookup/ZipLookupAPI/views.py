from rest_framework.views import APIView
from rest_framework.response import Response
import requests

base_url = "https://secure.shippingapis.com/ShippingAPI.dll?API=ZipCodeLookup&XML="

class ZipLookupView(APIView):


    def post(self, request, format=None):
        request_xml = request.data['requestXml']
        full_url = base_url + request_xml

        response = requests.post(base_url, full_url)

        response_wrapper = {
            "requestXml": response.content
        }

        return Response(response_wrapper)








