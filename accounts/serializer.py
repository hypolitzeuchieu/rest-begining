from rest_framework import serializers
from .validator import validate_username, validate_email
from api.models import Product
from .models import UserAccount


class ProductInlineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='pk')
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('url', 'email', 'name')


class UserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=100, validators=[validate_username])
    name = serializers.CharField(max_length=40)
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)

    def save(self, **kwargs):
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        name = self.validated_data.get('name')

        return UserAccount.objects.create(username=username, email=email, password=password, name=name)

    def get_user_product(self, obj):
        request = self.context.get('request')
        user = obj
        product = user.product_set.all()
        return ProductInlineSerializer(product, many=True, context={'request': request}).data
