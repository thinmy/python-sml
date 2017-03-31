from haystack import indexes
from tours.models import Tour


class TourIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    active = indexes.CharField(model_attr='active')
    category = indexes.CharField(model_attr='category')
    owner = indexes.CharField(model_attr='owner')
    location = indexes.LocationField()

    def get_model(self):
        return Tour

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active=1)

    def prepare_location(self, obj):
        # If you're just storing the floats...
        return "%s,%s" % (obj.latitude, obj.longitude)
