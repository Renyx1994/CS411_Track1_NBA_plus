from django.forms import ModelForm
from NBA_plus.models import PlayerBasic

class PlayerForm(ModelForm):
     class Meta:
         model = PlayerBasic
         fields = '__all__'