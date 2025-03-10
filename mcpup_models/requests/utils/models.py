"""Pydantic models for requests.utils functions."""

import requests.utils

from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class AddDictToCookiejar:
    """Returns a CookieJar from a key/value dictionary.
    
    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar"""

    # Original function signature: (cj, cookie_dict)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.add_dict_to_cookiejar

    model = ValidatedFunction(requests.utils.add_dict_to_cookiejar).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class AddressInNetwork:
    """This function allows you to check if an IP belongs to a network subnet
    
    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24
    
    :rtype: bool"""

    # Original function signature: (ip, net)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.address_in_network

    model = ValidatedFunction(requests.utils.address_in_network).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class AtomicOpen:
    """Write a file to the disk in an atomic fashion"""

    # Original function signature: (filename)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.atomic_open

    model = ValidatedFunction(requests.utils.atomic_open).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class CheckHeaderValidity:
    """Verifies that header parts don't contain leading whitespace
    reserved characters, or return characters.
    
    :param header: tuple, in the format (name, value)."""

    # Original function signature: (header)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.check_header_validity

    model = ValidatedFunction(requests.utils.check_header_validity).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DefaultHeaders:
    """:rtype: requests.structures.CaseInsensitiveDict"""

    # Original function signature: ()
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.default_headers

    model = ValidatedFunction(requests.utils.default_headers).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DefaultUserAgent:
    """Return a string representing the default user agent.
    
    :rtype: str"""

    # Original function signature: (name='python-requests')
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.default_user_agent

    model = ValidatedFunction(requests.utils.default_user_agent).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DictFromCookiejar:
    """Returns a key/value dictionary from a CookieJar.
    
    :param cj: CookieJar object to extract cookies from.
    :rtype: dict"""

    # Original function signature: (cj)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.dict_from_cookiejar

    model = ValidatedFunction(requests.utils.dict_from_cookiejar).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DictToSequence:
    """Returns an internal sequence dictionary update."""

    # Original function signature: (d)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.dict_to_sequence

    model = ValidatedFunction(requests.utils.dict_to_sequence).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DottedNetmask:
    """Converts mask from /xx format to xxx.xxx.xxx.xxx
    
    Example: if mask is 24 function returns 255.255.255.0
    
    :rtype: str"""

    # Original function signature: (mask)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.dotted_netmask

    model = ValidatedFunction(requests.utils.dotted_netmask).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ExtractZippedPaths:
    """Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged."""

    # Original function signature: (path)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.extract_zipped_paths

    model = ValidatedFunction(requests.utils.extract_zipped_paths).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class FromKeyValList:
    """Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,
    
    ::
    
        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])
    
    :rtype: OrderedDict"""

    # Original function signature: (value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.from_key_val_list

    model = ValidatedFunction(requests.utils.from_key_val_list).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetAuthFromUrl:
    """Given a url with authentication components, extract them into a tuple of
    username,password.
    
    :rtype: (str,str)"""

    # Original function signature: (url)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_auth_from_url

    model = ValidatedFunction(requests.utils.get_auth_from_url).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetEncodingFromHeaders:
    """Returns encodings from given HTTP Header Dict.
    
    :param headers: dictionary to extract encoding from.
    :rtype: str"""

    # Original function signature: (headers)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_encoding_from_headers

    model = ValidatedFunction(requests.utils.get_encoding_from_headers).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetEncodingsFromContent:
    """Returns encodings from given content string.
    
    :param content: bytestring to extract encodings from."""

    # Original function signature: (content)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_encodings_from_content

    model = ValidatedFunction(requests.utils.get_encodings_from_content).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetEnvironProxies:
    """Return a dict of environment proxies.
    
    :rtype: dict"""

    # Original function signature: (url, no_proxy=None)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_environ_proxies

    model = ValidatedFunction(requests.utils.get_environ_proxies).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetNetrcAuth:
    """Returns the Requests tuple auth for a given url from netrc."""

    # Original function signature: (url, raise_errors=False)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_netrc_auth

    model = ValidatedFunction(requests.utils.get_netrc_auth).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GetUnicodeFromResponse:
    """Returns the requested content back in unicode.
    
    :param r: Response object to get unicode content from.
    
    Tried:
    
    1. charset from content-type
    2. fall back and replace all unicode characters
    
    :rtype: str"""

    # Original function signature: (r)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.get_unicode_from_response

    model = ValidatedFunction(requests.utils.get_unicode_from_response).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GuessFilename:
    """Tries to guess the filename of the given object."""

    # Original function signature: (obj)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.guess_filename

    model = ValidatedFunction(requests.utils.guess_filename).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class GuessJsonUtf:
    """:rtype: str"""

    # Original function signature: (data)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.guess_json_utf

    model = ValidatedFunction(requests.utils.guess_json_utf).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class IsIpv4Address:
    """:rtype: bool"""

    # Original function signature: (string_ip)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.is_ipv4_address

    model = ValidatedFunction(requests.utils.is_ipv4_address).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class IsValidCidr:
    """Very simple check of the cidr format in no_proxy variable.
    
    :rtype: bool"""

    # Original function signature: (string_network)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.is_valid_cidr

    model = ValidatedFunction(requests.utils.is_valid_cidr).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class IterSlices:
    """Iterate over slices of a string."""

    # Original function signature: (string, slice_length)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.iter_slices

    model = ValidatedFunction(requests.utils.iter_slices).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ParseDictHeader:
    """Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:
    
    >>> d = parse_dict_header('foo="is a fish", bar="as well"')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [('bar', 'as well'), ('foo', 'is a fish')]
    
    If there is no value for a key it will be `None`:
    
    >>> parse_dict_header('key_without_value')
    {'key_without_value': None}
    
    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.
    
    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict"""

    # Original function signature: (value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.parse_dict_header

    model = ValidatedFunction(requests.utils.parse_dict_header).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ParseHeaderLinks:
    """Return a list of parsed link headers proxies.
    
    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"
    
    :rtype: list"""

    # Original function signature: (value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.parse_header_links

    model = ValidatedFunction(requests.utils.parse_header_links).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ParseListHeader:
    """Parse lists as described by RFC 2068 Section 2.
    
    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.
    
    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.
    
    The return value is a standard :class:`list`:
    
    >>> parse_list_header('token, "quoted value"')
    ['token', 'quoted value']
    
    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.
    
    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list"""

    # Original function signature: (value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.parse_list_header

    model = ValidatedFunction(requests.utils.parse_list_header).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class PrependSchemeIfNeeded:
    """Given a URL that may or may not have a scheme, prepend the given scheme.
    Does not replace a present scheme with the one provided as an argument.
    
    :rtype: str"""

    # Original function signature: (url, new_scheme)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.prepend_scheme_if_needed

    model = ValidatedFunction(requests.utils.prepend_scheme_if_needed).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class RequoteUri:
    """Re-quote the given URI.
    
    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.
    
    :rtype: str"""

    # Original function signature: (uri)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.requote_uri

    model = ValidatedFunction(requests.utils.requote_uri).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ResolveProxies:
    """This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such as NO_PROXY to strip proxy configurations.
    
    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs
    
    :rtype: dict"""

    # Original function signature: (request, proxies, trust_env=True)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.resolve_proxies

    model = ValidatedFunction(requests.utils.resolve_proxies).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class RewindBody:
    """Move file pointer back to its recorded starting position
    so it can be read again on redirect."""

    # Original function signature: (prepared_request)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.rewind_body

    model = ValidatedFunction(requests.utils.rewind_body).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class SelectProxy:
    """Select a proxy for the url, if applicable.
    
    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs"""

    # Original function signature: (url, proxies)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.select_proxy

    model = ValidatedFunction(requests.utils.select_proxy).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class SetEnviron:
    """Set the environment variable 'env_name' to 'value'
    
    Save previous value, yield, and then restore the previous value stored in
    the environment variable 'env_name'.
    
    If 'value' is None, do nothing"""

    # Original function signature: (env_name, value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.set_environ

    model = ValidatedFunction(requests.utils.set_environ).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ShouldBypassProxies:
    """Returns whether we should bypass proxies or not.
    
    :rtype: bool"""

    # Original function signature: (url, no_proxy)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.should_bypass_proxies

    model = ValidatedFunction(requests.utils.should_bypass_proxies).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class StreamDecodeResponseUnicode:
    """Stream decodes an iterator."""

    # Original function signature: (iterator, r)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.stream_decode_response_unicode

    model = ValidatedFunction(requests.utils.stream_decode_response_unicode).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class SuperLen:
    """Pydantic model for function parameters."""

    # Original function signature: (o)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.super_len

    model = ValidatedFunction(requests.utils.super_len).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class ToKeyValList:
    """Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,
    
    ::
    
        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
    
    :rtype: list"""

    # Original function signature: (value)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.to_key_val_list

    model = ValidatedFunction(requests.utils.to_key_val_list).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class UnquoteHeaderValue:
    """Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.
    
    :param value: the header value to unquote.
    :rtype: str"""

    # Original function signature: (value, is_filename=False)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.unquote_header_value

    model = ValidatedFunction(requests.utils.unquote_header_value).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class UnquoteUnreserved:
    """Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.
    
    :rtype: str"""

    # Original function signature: (uri)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.unquote_unreserved

    model = ValidatedFunction(requests.utils.unquote_unreserved).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class Urldefragauth:
    """Given a url remove the fragment and the authentication part.
    
    :rtype: str"""

    # Original function signature: (url)
    # Module: requests.utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.utils
        return requests.utils.urldefragauth

    model = ValidatedFunction(requests.utils.urldefragauth).model


__all__ = ['AddDictToCookiejar', 'AddressInNetwork', 'AtomicOpen', 'CheckHeaderValidity', 'DefaultHeaders', 'DefaultUserAgent', 'DictFromCookiejar', 'DictToSequence', 'DottedNetmask', 'ExtractZippedPaths', 'FromKeyValList', 'GetAuthFromUrl', 'GetEncodingFromHeaders', 'GetEncodingsFromContent', 'GetEnvironProxies', 'GetNetrcAuth', 'GetUnicodeFromResponse', 'GuessFilename', 'GuessJsonUtf', 'IsIpv4Address', 'IsValidCidr', 'IterSlices', 'ParseDictHeader', 'ParseHeaderLinks', 'ParseListHeader', 'PrependSchemeIfNeeded', 'RequoteUri', 'ResolveProxies', 'RewindBody', 'SelectProxy', 'SetEnviron', 'ShouldBypassProxies', 'StreamDecodeResponseUnicode', 'SuperLen', 'ToKeyValList', 'UnquoteHeaderValue', 'UnquoteUnreserved', 'Urldefragauth']
