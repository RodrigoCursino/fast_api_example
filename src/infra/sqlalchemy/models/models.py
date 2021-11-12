from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

class User(Base):
    __tablename__ = "users"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(100))
    picture    = Column(String(800))
    stars      = Column(Integer)
    type       = Column(String(10))
    cellphone  = Column(String(20), unique=True)
    password   = Column(String(255))
    activate   = Column(Boolean, default=True)
    #roles      = relationship('RoleUser', back_populates="roles_users")

    def __init__(self, username, picture, stars, type, cellphone, password, activate=True):
        self.username  = username
        self.picture   = picture
        self.stars     = stars
        self.type      = type
        self.cellphone = cellphone
        self.activate  = activate
        self.password  = password

class Role(Base):
    __tablename__ = "roles"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(100))
    activate   = Column(Boolean, default=True)

    def __init__(self, name, activate=True):
        self.name     = name
        self.activate = activate

class Team(Base):
    __tablename__ = "teams"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(100))
    color      = Column(String(50))
    picture    = Column(String(800))
    activate   = Column(Boolean, default=True)

    def __init__(self, name, color, picture, activate=True):
        self.name     = name
        self.color    = color
        self.picture  = picture
        self.activate = activate

class TeamPlayer(Base):
    __tablename__     = "teams_players"
    id                = Column(Integer, primary_key=True, autoincrement=True)
    id_team           = Column(ForeignKey('teams.id'), name="fk_teams_teams_players", primary_key=True)
    id_user           = Column(ForeignKey('users.id'), name="fk_users_teams_players", primary_key=True)
    date              = Column(DateTime)
    team              = relationship('Team', foreign_keys=id_team)
    player            = relationship('User', foreign_keys=id_user)
    activate          = Column(Boolean, default=True)

    def __init__(self, id_team, id_user, date, activate):
          self.id_team  = id_team
          self.id_user  = id_user
          self.date     = date
          self.activate = activate
         
    def __repr__(self):
        return "<TeamPlayer %r>" % self.date

class Match(Base):
    __tablename__         = "matches"
    id                    = Column(Integer, primary_key=True, autoincrement=True)
    id_team_one           = Column(ForeignKey('teams_players.id'), name="fk_teams_players_matches_one", primary_key=True)
    id_team_two           = Column(ForeignKey('teams_players.id'), name="fk_teams_players_matches_two", primary_key=True)
    # [VITORIA,EMPATE,DERROTA]
    match_status_team_one = Column(String(25))
    match_status_team_two = Column(String(25))
    match_date            = Column(DateTime)
    activate              = Column(Boolean, default=True)

    def __init__(self, id_team_one, id_team_two, match_status_team_one, match_status_team_two, match_date, activate):
        self.id_team_one  = id_team_one 
        self.id_team_two  = id_team_two 
        self.match_status_team_one = match_status_team_one  
        self.match_status_team_two = match_status_team_two   
        self.match_date   = match_date
        self.activate     = activate     
         
    def __repr__(self):
        return "<MATCH %r>" % self.match_date


class Statistic(Base):
    __tablename__         = "statistics"
    id                    = Column(Integer, primary_key=True, autoincrement=True)
    id_user               = Column(ForeignKey('users.id'), name="fk_users_statistics", primary_key=True)
    id_match              = Column(ForeignKey('matches.id'), name="fk_match_statistics", primary_key=True)
    date                  = Column(DateTime)
    # ['GOL', 'ASSSITENCIA', 'VITORIA', 'DERROTA', 'EMPATE']
    status                = Column(String(50))
    activate              = Column(Boolean, default=True)
    #match                 = relationship('Match', back_populates="matchs")
    #user                  = relationship('User', back_populates="users")

    def __init__(self, id_user, id_match, date, status, activate):
        self.id_user  = id_user 
        self.id_match = id_match 
        self.date     = date 
        self.status   = status
        self.activate = activate     
         
    def __repr__(self):
        return "<STATISTICS %r>" % self.date

class RoleUser(Base):
    __tablename__ = "roles_users"
    id         = Column(Integer, primary_key=True, autoincrement=True)
    id_role    = Column(ForeignKey('roles.id'), name="fk_role_roles_users", primary_key=True)
    id_user    = Column(ForeignKey('users.id'), name="fk_user_roles_users", primary_key=True)
    #role       = relationship('Role', foreign_keys=id_role, back_populates="roles_users")
    #user       = relationship('User', foreign_keys=id_user,  back_populates="roles_users")
    activate   = Column(Boolean, default=True)

    def __init__(self, user, role, activate=True):
        self.role     = role
        self.user     = user
        self.activate = activate




