from rest_framework import serializers
from .models import Product
from .validator import product_name
from accounts.serializer import UserSerializers


class ProductSerializers(serializers.Serializer):
    owner = UserSerializers(source='user', read_only=True)
    name = serializers.CharField(max_length=100, validators=[product_name])
    description = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    due_date = serializers.DateTimeField()
    image = serializers.ImageField()

    url = serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='pk')

    class Meta:
        fields = ['name', 'url']

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        price = validated_data.get('price')
        due_date = validated_data.get('due_date')
        image = validated_data.get('image')
        return Product.objects.create(name=name, description=description, price=price, due_date=due_date, image=image)
