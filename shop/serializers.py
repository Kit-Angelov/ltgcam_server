from . import models
from rest_framework import serializers


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mark
        fields = ['id', 'name']


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Photo
        fields = ['photo']


class VideoExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VideoExample
        fields = ['link']


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Options
        fields = ['text']


class MainOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainOptions
        fields = ['text']


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Description
        fields = ['text']


class AutoModelSerializer(serializers.HyperlinkedModelSerializer):

    main_photo = PhotoSerializer(many=False)
    galery_photo = PhotoSerializer(many=True)
    options = OptionsSerializer(many=True)
    main_options = MainOptionsSerializer(many=True)
    video = VideoExampleSerializer(many=False)
    mark = MarkSerializer(many=False)
    description = DescriptionSerializer(many=False)

    class Meta:
        model = models.AutoModel
        fields = ['url',
                  'id',
                  'name',
                  'main_photo',
                  'galery_photo',
                  'options',
                  'main_options',
                  'video',
                  'mark',
                  'price',
                  'description']
