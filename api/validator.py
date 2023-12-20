from .models import Product
from rest_framework.validators import UniqueValidator

product_name = UniqueValidator(queryset=Product.objects.all())
