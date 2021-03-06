from properties import Property
from processes import Process
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      FloatProperty, UniqueIdProperty, RelationshipTo, RelationshipFrom)


class Instrument(StructuredNode):
    instrument = StringProperty(unique_index=True, required=True)
    model = StringProperty(unique_index=True, required=True)


class Researcher(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    Facility = StringProperty(unique_index=True, required=True)
