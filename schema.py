from graphene import relay, ObjectType, Schema, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Bucket as BucketModel, Item as ItemModel


class Bucket(SQLAlchemyObjectType):
    class Meta:
        model = BucketModel
        interfaces = (relay.Node,)


class Item(SQLAlchemyObjectType):
    class Meta:
        model = ItemModel
        interfaces = (relay.Node,)


class Query(ObjectType):
    node = relay.Node.Field()

    # Allows sorting over multiple columns, by default over the primary key
    all_items = List(Item)
    # Disable sorting over this field
    # all_buckets = SQLAlchemyConnectionField(Bucket.connection, sort=None)


schema = Schema(query=Query)
