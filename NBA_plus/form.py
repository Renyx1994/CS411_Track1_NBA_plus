from django.forms import ModelForm
from NBA_plus.models import PlayerBasic, TeamBasic, MatchRecords

class PlayerForm(ModelForm):
     class Meta:
         model = PlayerBasic
         fields = '__all__'

class TeamForm(ModelForm):
    class Meta:
        model = TeamBasic
        fields = '__all__'

class GameForm(ModelForm):
    class Meta:
        model = MatchRecords
        fields = '__all__'