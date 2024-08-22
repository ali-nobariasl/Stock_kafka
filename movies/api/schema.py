import graphene
from graphene_django.types import DjangoObjectType
from .models import Movie , Dicrector
import graphql_jwt
from graphql_jwt.shortcuts import get_token, get_user_by_token
from graphql_jwt.decorators import login_required
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    #adding extra attributes which is  not in model
    movie_age = graphene.String()
    def resolve_movie_age(self, info):
        return 'old' if self.year < 2000 else 'new'

# this is for other model class, and also for adding foreign key
class DicrectorType(DjangoObjectType):
    class Meta:
        model= Dicrector


# implementing relay
class MovieNode(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = ['title','year']
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    #all_movies = graphene.List(MovieType)
    all_movies = DjangoFilterConnectionField(MovieNode)
    #movie = graphene.Field(MovieType, id = graphene.Int(), title = graphene.String())
    movie = relay.Node.Field(MovieNode)

    '''
    # should have resolve_'name of attributes' function for each attribute
    def resolve_movie(self,info,**kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')
        if id is not None:
            return Movie.objects.get(pk=id)
        if title is not None:
            return Movie.objects.get(title=title)
        return None
    '''

    # should have resolve_'name of attributes' function for each attribute    
    @login_required
    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()
    

    # same sructure for Dicrector model
    all_dicrectors = graphene.List(DicrectorType)

    def resolve_all_dicrectors(self, info, **kwargs):
        return Dicrector.objects.all()
    

#for mutation
class MovieCreateMutation(graphene.Mutation):
    # this is for arguments we want to accept when creating movies
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)
    
    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year):
        
        movie = Movie.objects.create(title=title, year=year)
        return MovieCreateMutation(movie=movie)
    



class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        year = graphene.Int()
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)
    
    def mutate(self, info,id, title, year):
        movie = Movie.objects.get(pk= id)
        if title is not None:
            movie.title = title
        if year is not None:
            movie.year = year
        movie.save()

        return MovieUpdateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    movie = graphene.Field(MovieType)

    def mutate(self, id ):
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return MovieUpdateMutation(movie=None)

class Mutation:
    # this token type use username and password for authentication
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()