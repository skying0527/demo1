from rest_framework import serializers
from .models import UserPersonalInfo

class UserPersonalInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)  # 昵称
    sex_choices = (
        (u'M', u'男'),
        (u'F', u'女'),
    )
    sex = serializers.ChoiceField(choices=sex_choices
                            )
    age = serializers.IntegerField(default="")
    mail = serializers.EmailField(max_length=30, default="")
    create_time = serializers.DateField(read_only=True)


    def create(self,validated_data):
        return UserPersonalInfo.objects.create(**validated_data)


    def update(self,instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.age = validated_data.get('age', instance.age)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.save()
        return instance
