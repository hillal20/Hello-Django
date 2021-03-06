from graphene_django import DjangoObjectType
import graphene 
from  .models import PersonalNote as PersonalNoteModel


class PersonalNote(DjangoObjectType):
      class Meta:
        model = PersonalNoteModel
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
      personalnotes = graphene.List(PersonalNote)
      def resolve_personalnotes(self, info):
          user = info.context.user
          if user.is_anonymous:
             return PersonalNoteModel.objects.none()
          else:
              return PersonalNoteModel.objects.filter(user=user)


schema = graphene.Schema(query=Query)