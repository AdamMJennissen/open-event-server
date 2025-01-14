from flask_rest_jsonapi import ResourceDetail, ResourceList

from app.api.bootstrap import api
from app.api.helpers.db import safe_query_kwargs
from app.api.helpers.permission_manager import has_access, is_logged_in
from app.api.schema.video_channel import VideoChannelSchema, VideoChannelSchemaPublic
from app.models import db
from app.models.Event_Context.video_channel import VideoChannel
from app.models.Event_Context.video_stream import VideoStream


class VideoChannelListPost(ResourceList):
    """Post to Video Channel List"""

    methods = ['POST']
    decorators = (api.has_permission('is_admin', methods="POST"),)
    schema = VideoChannelSchema
    data_layer = {
        'session': db.session,
        'model': VideoChannel,
    }


class VideoChannelList(ResourceList):
    """List of Video Channels"""

    def before_get(self, unused_args, unused_kwargs):
        """Providing the requester with the (public) video channel schema"""
        if is_logged_in() and has_access('is_admin'):
            self.schema = VideoChannelSchema
        else:
            self.schema = VideoChannelSchemaPublic

    methods = ['GET']
    schema = VideoChannelSchemaPublic
    data_layer = {
        'session': db.session,
        'model': VideoChannel,
    }


class VideoChannelDetail(ResourceDetail):
    """Details of Video Channel"""

    def before_get(self, unused_args, kwargs):
        """
        Providing the requester with the (public) video channel schema,
        as well as further details.
        """
        if is_logged_in() and has_access('is_admin'):
            self.schema = VideoChannelSchema
        else:
            self.schema = VideoChannelSchemaPublic

        if kwargs.get('video_stream_id'):
            stream = safe_query_kwargs(VideoStream, kwargs, 'video_stream_id')
            kwargs['id'] = stream.channel_id

    schema = VideoChannelSchema
    decorators = (
        api.has_permission(
            'is_admin',
            methods="PATCH,DELETE",
        ),
    )
    data_layer = {
        'session': db.session,
        'model': VideoChannel,
    }
