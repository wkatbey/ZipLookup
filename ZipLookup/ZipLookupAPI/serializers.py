from rest_framework import serializers

class ZipLookupSerializer(serializers.Serializer):
    requestXml = serializers.CharField()