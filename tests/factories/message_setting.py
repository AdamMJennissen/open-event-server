from app.api.helpers.system_mails import MailType
from app.models.Communication_Context.message_setting import MessageSettings
from tests.factories.base import BaseFactory


class MessageSettingsFactory(BaseFactory):
    class Meta:
        model = MessageSettings

    action = MailType.EVENT_ROLE
    enabled = True
