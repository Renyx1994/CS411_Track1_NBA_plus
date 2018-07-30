from django.forms import Form,ModelForm,CharField
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

class SimilarplayerForm(Form):
    player_name = CharField(label='Player name', max_length=100)

class PredictForm(Form):
    team_name = CharField(label='Team name', max_length=100)