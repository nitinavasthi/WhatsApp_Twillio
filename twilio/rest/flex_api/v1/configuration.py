# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ConfigurationList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the ConfigurationList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationList
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationList
        """
        super(ConfigurationList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a ConfigurationContext

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        """
        return ConfigurationContext(self._version, )

    def __call__(self):
        """
        Constructs a ConfigurationContext

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        """
        return ConfigurationContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.ConfigurationList>'


class ConfigurationPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ConfigurationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationPage
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationPage
        """
        super(ConfigurationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConfigurationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        return ConfigurationInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.ConfigurationPage>'


class ConfigurationContext(InstanceContext):
    """  """

    def __init__(self, version):
        """
        Initialize the ConfigurationContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        """
        super(ConfigurationContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Configuration'.format(**self._solution)

    def fetch(self, ui_version=values.unset):
        """
        Fetch a ConfigurationInstance

        :param unicode ui_version: Pinned UI version

        :returns: Fetched ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        params = values.of({'UiVersion': ui_version, })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ConfigurationInstance(self._version, payload, )

    def create(self):
        """
        Create a new ConfigurationInstance

        :returns: Newly created ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        data = values.of({})

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload, )

    def update(self):
        """
        Update the ConfigurationInstance

        :returns: Updated ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        data = values.of({})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ConfigurationContext {}>'.format(context)


class ConfigurationInstance(InstanceResource):
    """  """

    class Status(object):
        OK = "ok"
        INPROGRESS = "inprogress"
        NOTSTARTED = "notstarted"

    def __init__(self, version, payload):
        """
        Initialize the ConfigurationInstance

        :returns: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        super(ConfigurationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'attributes': payload['attributes'],
            'status': payload['status'],
            'taskrouter_workspace_sid': payload['taskrouter_workspace_sid'],
            'taskrouter_target_workflow_sid': payload['taskrouter_target_workflow_sid'],
            'taskrouter_target_taskqueue_sid': payload['taskrouter_target_taskqueue_sid'],
            'taskrouter_taskqueues': payload['taskrouter_taskqueues'],
            'taskrouter_skills': payload['taskrouter_skills'],
            'taskrouter_worker_channels': payload['taskrouter_worker_channels'],
            'taskrouter_worker_attributes': payload['taskrouter_worker_attributes'],
            'taskrouter_offline_activity_sid': payload['taskrouter_offline_activity_sid'],
            'runtime_domain': payload['runtime_domain'],
            'messaging_service_instance_sid': payload['messaging_service_instance_sid'],
            'chat_service_instance_sid': payload['chat_service_instance_sid'],
            'ui_language': payload['ui_language'],
            'ui_attributes': payload['ui_attributes'],
            'ui_version': payload['ui_version'],
            'service_version': payload['service_version'],
            'call_recording_enabled': payload['call_recording_enabled'],
            'call_recording_webhook_url': payload['call_recording_webhook_url'],
            'crm_enabled': payload['crm_enabled'],
            'crm_type': payload['crm_type'],
            'crm_callback_url': payload['crm_callback_url'],
            'crm_fallback_url': payload['crm_fallback_url'],
            'crm_attributes': payload['crm_attributes'],
            'public_attributes': payload['public_attributes'],
            'plugin_service_enabled': payload['plugin_service_enabled'],
            'plugin_service_attributes': payload['plugin_service_attributes'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ConfigurationContext for this ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationContext
        """
        if self._context is None:
            self._context = ConfigurationContext(self._version, )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account responsible for this configuration
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The time the Configuration was created, given as GMT in ISO 8601 format
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The time the Configuration was last updated, given as GMT in ISO 8601 format
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def attributes(self):
        """
        :returns: Attiributes
        :rtype: dict
        """
        return self._properties['attributes']

    @property
    def status(self):
        """
        :returns: Status of the Flex onboarding
        :rtype: ConfigurationInstance.Status
        """
        return self._properties['status']

    @property
    def taskrouter_workspace_sid(self):
        """
        :returns: The unique ID of the TaskRouter Workspace
        :rtype: unicode
        """
        return self._properties['taskrouter_workspace_sid']

    @property
    def taskrouter_target_workflow_sid(self):
        """
        :returns: The unique ID of the TaskRouter Target Workflow
        :rtype: unicode
        """
        return self._properties['taskrouter_target_workflow_sid']

    @property
    def taskrouter_target_taskqueue_sid(self):
        """
        :returns: The unique ID of the TaskRouter Target TaskQueue
        :rtype: unicode
        """
        return self._properties['taskrouter_target_taskqueue_sid']

    @property
    def taskrouter_taskqueues(self):
        """
        :returns: Array of TaskRouter TaskQueues
        :rtype: dict
        """
        return self._properties['taskrouter_taskqueues']

    @property
    def taskrouter_skills(self):
        """
        :returns: Skill description for TaskRouter workers
        :rtype: dict
        """
        return self._properties['taskrouter_skills']

    @property
    def taskrouter_worker_channels(self):
        """
        :returns: TaskRouter default channel capacities and availability for workers
        :rtype: dict
        """
        return self._properties['taskrouter_worker_channels']

    @property
    def taskrouter_worker_attributes(self):
        """
        :returns: The taskrouter_worker_attributes
        :rtype: dict
        """
        return self._properties['taskrouter_worker_attributes']

    @property
    def taskrouter_offline_activity_sid(self):
        """
        :returns: The unique ID of the offline activity
        :rtype: unicode
        """
        return self._properties['taskrouter_offline_activity_sid']

    @property
    def runtime_domain(self):
        """
        :returns: Flex resources hosting URL for the main UI
        :rtype: unicode
        """
        return self._properties['runtime_domain']

    @property
    def messaging_service_instance_sid(self):
        """
        :returns: Unique 34 character ID of the Messaging Service
        :rtype: unicode
        """
        return self._properties['messaging_service_instance_sid']

    @property
    def chat_service_instance_sid(self):
        """
        :returns: The unique id of the Chat Service this user belongs to
        :rtype: unicode
        """
        return self._properties['chat_service_instance_sid']

    @property
    def ui_language(self):
        """
        :returns: Main language of the Flex UI
        :rtype: unicode
        """
        return self._properties['ui_language']

    @property
    def ui_attributes(self):
        """
        :returns: UI Attributes
        :rtype: dict
        """
        return self._properties['ui_attributes']

    @property
    def ui_version(self):
        """
        :returns: Pinned UI version
        :rtype: unicode
        """
        return self._properties['ui_version']

    @property
    def service_version(self):
        """
        :returns: Flex Service version
        :rtype: unicode
        """
        return self._properties['service_version']

    @property
    def call_recording_enabled(self):
        """
        :returns: Call recording enabled
        :rtype: bool
        """
        return self._properties['call_recording_enabled']

    @property
    def call_recording_webhook_url(self):
        """
        :returns: Call recording webhook url
        :rtype: unicode
        """
        return self._properties['call_recording_webhook_url']

    @property
    def crm_enabled(self):
        """
        :returns: Flag indicating whether CRM is present for Flex
        :rtype: bool
        """
        return self._properties['crm_enabled']

    @property
    def crm_type(self):
        """
        :returns: CRM Type
        :rtype: unicode
        """
        return self._properties['crm_type']

    @property
    def crm_callback_url(self):
        """
        :returns: CRM Callback URL
        :rtype: unicode
        """
        return self._properties['crm_callback_url']

    @property
    def crm_fallback_url(self):
        """
        :returns: CRM Fallback URL
        :rtype: unicode
        """
        return self._properties['crm_fallback_url']

    @property
    def crm_attributes(self):
        """
        :returns: CRM Attributes
        :rtype: dict
        """
        return self._properties['crm_attributes']

    @property
    def public_attributes(self):
        """
        :returns: Public Attributes
        :rtype: dict
        """
        return self._properties['public_attributes']

    @property
    def plugin_service_enabled(self):
        """
        :returns: Is plugin service Enabled
        :rtype: bool
        """
        return self._properties['plugin_service_enabled']

    @property
    def plugin_service_attributes(self):
        """
        :returns: Plugin service Attributes
        :rtype: dict
        """
        return self._properties['plugin_service_attributes']

    @property
    def url(self):
        """
        :returns: The URL for this resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, ui_version=values.unset):
        """
        Fetch a ConfigurationInstance

        :param unicode ui_version: Pinned UI version

        :returns: Fetched ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        return self._proxy.fetch(ui_version=ui_version, )

    def create(self):
        """
        Create a new ConfigurationInstance

        :returns: Newly created ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        return self._proxy.create()

    def update(self):
        """
        Update the ConfigurationInstance

        :returns: Updated ConfigurationInstance
        :rtype: twilio.rest.flex_api.v1.configuration.ConfigurationInstance
        """
        return self._proxy.update()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ConfigurationInstance {}>'.format(context)
