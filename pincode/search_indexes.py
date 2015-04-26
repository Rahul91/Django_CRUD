from haystack import indexes
from pincode.models import Pincode 

class PincodeIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	content_auto = indexes.EdgeNgramField(model_attr='pincode')

	def get_model(self):
		return Pincode

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
	