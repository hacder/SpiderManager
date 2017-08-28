from rest_framework import serializers
from backend import models


class ScrapydSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Scrapyd
        fields = ('id', 'name', 'ip', 'port', 'comment')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'scrapyd', 'comment')


class SpiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Spider
        fields = ('id', 'name', 'project', 'comment')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = ('id', 'name', 'spider', 'comment')