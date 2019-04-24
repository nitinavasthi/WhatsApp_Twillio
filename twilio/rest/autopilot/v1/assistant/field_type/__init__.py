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
from twilio.rest.autopilot.v1.assistant.field_type.field_value import FieldValueList


class FieldTypeList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the FieldTypeList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeList
        """
        super(FieldTypeList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }
        self._uri = '/Assistants/{assistant_sid}/FieldTypes'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FieldTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FieldTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FieldTypeInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FieldTypePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FieldTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FieldTypePage(self._version, response, self._solution)

    def create(self, unique_name, friendly_name=values.unset):
        """
        Create a new FieldTypeInstance

        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can be up to 255 characters long.

        :returns: Newly created FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        data = values.of({'UniqueName': unique_name, 'FriendlyName': friendly_name, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def get(self, sid):
        """
        Constructs a FieldTypeContext

        :param sid: A 34-character string that uniquely identifies this resource.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        return FieldTypeContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FieldTypeContext

        :param sid: A 34-character string that uniquely identifies this resource.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        return FieldTypeContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.FieldTypeList>'


class FieldTypePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FieldTypePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the Assistant.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        super(FieldTypePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FieldTypeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.FieldTypePage>'


class FieldTypeContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the FieldTypeContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.
        :param sid: A 34-character string that uniquely identifies this resource.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        super(FieldTypeContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/FieldTypes/{sid}'.format(**self._solution)

        # Dependents
        self._field_values = None

    def fetch(self):
        """
        Fetch a FieldTypeInstance

        :returns: Fetched FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FieldTypeInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the FieldTypeInstance

        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can be up to 255 characters long.
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.

        :returns: Updated FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'UniqueName': unique_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return FieldTypeInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the FieldTypeInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def field_values(self):
        """
        Access the field_values

        :returns: twilio.rest.autopilot.v1.assistant.field_type.field_value.FieldValueList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.field_value.FieldValueList
        """
        if self._field_values is None:
            self._field_values = FieldValueList(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                field_type_sid=self._solution['sid'],
            )
        return self._field_values

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.FieldTypeContext {}>'.format(context)


class FieldTypeInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the FieldTypeInstance

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        super(FieldTypeInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'links': payload['links'],
            'assistant_sid': payload['assistant_sid'],
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FieldTypeContext for this FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        if self._context is None:
            self._context = FieldTypeContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field Type.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A user-provided string that identifies this resource. It is non-unique and can be up to 255 characters long.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: A 34-character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a FieldTypeInstance

        :returns: Fetched FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the FieldTypeInstance

        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can be up to 255 characters long.
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.

        :returns: Updated FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return self._proxy.update(friendly_name=friendly_name, unique_name=unique_name, )

    def delete(self):
        """
        Deletes the FieldTypeInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def field_values(self):
        """
        Access the field_values

        :returns: twilio.rest.autopilot.v1.assistant.field_type.field_value.FieldValueList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.field_value.FieldValueList
        """
        return self._proxy.field_values

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.FieldTypeInstance {}>'.format(context)
