from rest_framework.serializers import ModelSerializer

from ..models import Professional, Cuidador


class ProfessionalSerializer(ModelSerializer):
    class Meta:
        model = Professional
        fields = "__all__"
        read_only_fields = ["id"]
        write_only_fields = ["password"]
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def create(self, validated_data: dict):
        return Professional.objects.create_user(**validated_data)


class CuidadorSerializer(ModelSerializer):
    class Meta:
        model = Cuidador
        fields = "__all__"
        read_only_fields = ["id"]
        extra_kwargs = {"id": {"read_only": True}}
