from django.forms import Form,ModelForm,CharField,IntegerField
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
    p = IntegerField(label='Parameter for learning')

class yearForm(Form):
    year = IntegerField(label='Years in the team')

class SeasonForm(Form):
    season = CharField(label='Specify the Season', max_length=100)

class WLForm(Form):
    team1 = CharField(label='First team name', max_length=100)
    team2 = CharField(label='Second team name', max_length=100)

class pForm(Form):
    p = IntegerField(label='Parameter for learning')