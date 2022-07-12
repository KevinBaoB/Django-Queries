from turtle import color
from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)
    
    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, product_rating):
        return Product.objects.filter(rating=product_rating)
    
    @classmethod
    def by_rating_range(cls, start, finish):
        return Product.objects.filter(rating__gte=start, rating__lte=finish)

    @classmethod
    def by_rating_and_color(cls, product_rating, color):
        return Product.objects.filter(rating=product_rating, color=color)

    @classmethod
    def by_rating_or_color(cls, product_rating, color):
        # import Q from django.db.models to use OR |
        return Product.objects.filter(Q(rating=product_rating) | Q(color=color))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()

    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(Q(price_cents__lte=price)|Q(rating__gte=rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        #Negative is shorthand for descending
        return Product.objects.order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer):
        # __icontains is case INSENSITIVE 
        return Product.objects.filter(manufacturer__icontains=manufacturer)

    @classmethod
    def manufacturer_names_for_query(cls, name):
        # values_list return the values of the object placement
        # flat=True return a list and not a tuple or nested list
        return Product.objects.filter(manufacturer__icontains=name).values_list('manufacturer', flat=True)

    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.exclude(category=category)

    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        # [:limit] slices the query set up to the limit
        return Product.objects.exclude(category=category)[:limit]

    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(category=category).values_list('manufacturer', flat=True)

    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category=category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.order_by(Length('model').desc()).values_list('id', flat=True)[0]

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model'))

[
  {
    "model": "cars_and_brands.brand",
    "pk": 1,
    "fields": {
      "name": "Toyota"
    }
  },
  {
    "model": "cars_and_brands.brand",
    "pk": 2,
    "fields": {
      "name": "Tesla"
    }
  },
  {
    "model": "cars_and_brands.brand",
    "pk": 3,
    "fields": {
      "name": "Honda"
    }
  }
]