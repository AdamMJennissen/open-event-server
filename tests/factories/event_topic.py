from app.models.Event_Context.event_topic import EventTopic
from tests.factories import common
from tests.factories.base import BaseFactory


class EventTopicFactory(BaseFactory):
    class Meta:
        model = EventTopic

    name = common.string_
    slug = common.slug_
    system_image_url = common.imageUrl_
