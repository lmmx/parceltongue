"""Pydantic models for requests.api functions."""

import requests.api

from pydantic_function_models import ValidatedFunction


class Delete:
    """Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.delete

    model = ValidatedFunction(requests.api.delete).model


from pydantic_function_models import ValidatedFunction


class Get:
    """Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, params=None, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.get

    model = ValidatedFunction(requests.api.get).model


from pydantic_function_models import ValidatedFunction


class Head:
    """Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes. If
        `allow_redirects` is not provided, it will be set to `False` (as
        opposed to the default :meth:`request` behavior).
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.head

    model = ValidatedFunction(requests.api.head).model


from pydantic_function_models import ValidatedFunction


class Options:
    """Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.options

    model = ValidatedFunction(requests.api.options).model


from pydantic_function_models import ValidatedFunction


class Patch:
    """Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, data=None, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.patch

    model = ValidatedFunction(requests.api.patch).model


from pydantic_function_models import ValidatedFunction


class Post:
    """Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, data=None, json=None, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.post

    model = ValidatedFunction(requests.api.post).model


from pydantic_function_models import ValidatedFunction


class Put:
    """Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \\*\\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response"""

    # Original function signature: (url, data=None, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.put

    model = ValidatedFunction(requests.api.put).model


from pydantic_function_models import ValidatedFunction


class Request:
    """Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      >>> req
      <Response [200]>"""

    # Original function signature: (method, url, **kwargs)
    # Module: requests.api

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.api

        return requests.api.request

    model = ValidatedFunction(requests.api.request).model


__all__ = ["Delete", "Get", "Head", "Options", "Patch", "Post", "Put", "Request"]
