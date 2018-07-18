# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoachRecords(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=255)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    lg = models.CharField(db_column='Lg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=255)  # Field name made lowercase.
    regular_g = models.IntegerField(db_column='regular_G', blank=True, null=True)  # Field name made lowercase.
    regular_w = models.IntegerField(db_column='regular_W', blank=True, null=True)  # Field name made lowercase.
    regular_l = models.IntegerField(db_column='regular_L', blank=True, null=True)  # Field name made lowercase.
    regular_wl_ratio = models.FloatField(blank=True, null=True)
    w_minus_l_over_2 = models.FloatField(blank=True, null=True)
    finish = models.IntegerField(db_column='Finish', blank=True, null=True)  # Field name made lowercase.
    playoff_g = models.IntegerField(db_column='playoff_G', blank=True, null=True)  # Field name made lowercase.
    playoff_w = models.IntegerField(db_column='playoff_W', blank=True, null=True)  # Field name made lowercase.
    playoff_l = models.IntegerField(db_column='playoff_L', blank=True, null=True)  # Field name made lowercase.
    playoff_wl_ratio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach_records'
        unique_together = (('id', 'season', 'tm'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MatchRecords(models.Model):
    playoff_regular = models.CharField(primary_key=True, max_length=120)
    team = models.CharField(max_length=120)
    year = models.IntegerField()
    g = models.IntegerField(db_column='G')  # Field name made lowercase.
    opponent = models.CharField(db_column='Opponent', max_length=120, blank=True, null=True)  # Field name made lowercase.
    home_away = models.IntegerField(db_column='Home_away', blank=True, null=True)  # Field name made lowercase.
    tm = models.IntegerField(db_column='Tm', blank=True, null=True)  # Field name made lowercase.
    opp = models.IntegerField(db_column='Opp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'match_records'
        unique_together = (('playoff_regular', 'team', 'year', 'g'),)


class PlayerAvgPerformance(models.Model):
    number_2p = models.IntegerField(db_column='2P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2p_percent = models.FloatField(db_column='2P_percent', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2pa = models.FloatField(db_column='2PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3p = models.IntegerField(db_column='3P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3p_percent = models.FloatField(db_column='3P_percent', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pa = models.FloatField(db_column='3PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ast = models.FloatField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    blk = models.FloatField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    drb = models.FloatField(db_column='DRB', blank=True, null=True)  # Field name made lowercase.
    fg = models.FloatField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fg_percent = models.FloatField(db_column='FG_percent', blank=True, null=True)  # Field name made lowercase.
    fga = models.FloatField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    ft = models.FloatField(db_column='FT', blank=True, null=True)  # Field name made lowercase.
    ft_percent = models.FloatField(db_column='FT_percent', blank=True, null=True)  # Field name made lowercase.
    fta = models.FloatField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    lg = models.CharField(db_column='Lg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mp = models.FloatField(db_column='MP')  # Field name made lowercase.
    orb = models.FloatField(db_column='ORB', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.FloatField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stl = models.FloatField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=255)  # Field name made lowercase.
    tov = models.FloatField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    trb = models.FloatField(db_column='TRB', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=255)  # Field name made lowercase.
    efg_percent = models.FloatField(db_column='eFG_percent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'player_avg_performance'
        unique_together = (('id', 'mp', 'season', 'tm'),)


class PlayerBasic(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    player = models.CharField(db_column='Player', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    until = models.IntegerField(db_column='Until', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='Pos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ht = models.CharField(db_column='Ht', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wt = models.CharField(db_column='Wt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=255, blank=True, null=True)  # Field name made lowercase.
    colleges = models.CharField(db_column='Colleges', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'player_basic'


class PlayerRegPerformance(models.Model):
    number_3p = models.IntegerField(db_column='3P', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3p_percent = models.FloatField(db_column='3P_percent', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3pa = models.IntegerField(db_column='3PA', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ast = models.IntegerField(db_column='AST', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', primary_key=True, max_length=120)  # Field name made lowercase.
    blk = models.IntegerField(db_column='BLK', blank=True, null=True)  # Field name made lowercase.
    drb = models.IntegerField(db_column='DRB', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fg = models.IntegerField(db_column='FG', blank=True, null=True)  # Field name made lowercase.
    fg_percent = models.FloatField(db_column='FG_percent', blank=True, null=True)  # Field name made lowercase.
    fga = models.IntegerField(db_column='FGA', blank=True, null=True)  # Field name made lowercase.
    ft = models.IntegerField(db_column='FT', blank=True, null=True)  # Field name made lowercase.
    ft_percent = models.FloatField(db_column='FT_percent', blank=True, null=True)  # Field name made lowercase.
    fta = models.IntegerField(db_column='FTA', blank=True, null=True)  # Field name made lowercase.
    g = models.IntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.CharField(db_column='GS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gmsc = models.FloatField(db_column='GmSc', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='Id', max_length=120)  # Field name made lowercase.
    mp = models.CharField(db_column='MP', max_length=255)  # Field name made lowercase.
    orb = models.IntegerField(db_column='ORB', blank=True, null=True)  # Field name made lowercase.
    opp = models.CharField(db_column='Opp', max_length=120)  # Field name made lowercase.
    pf = models.IntegerField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pts = models.IntegerField(db_column='PTS', blank=True, null=True)  # Field name made lowercase.
    rk = models.IntegerField(db_column='Rk', blank=True, null=True)  # Field name made lowercase.
    stl = models.IntegerField(db_column='STL', blank=True, null=True)  # Field name made lowercase.
    tov = models.IntegerField(db_column='TOV', blank=True, null=True)  # Field name made lowercase.
    trb = models.IntegerField(db_column='TRB', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='Tm', max_length=120)  # Field name made lowercase.
    home_or_awar = models.CharField(db_column='Home_or_Awar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wl = models.CharField(db_column='WL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'player_reg_performance'
        unique_together = (('age', 'id', 'mp', 'opp', 'tm'),)
