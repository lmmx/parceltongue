"""Pydantic models for requests.cookies functions."""

import requests.cookies

from pydantic_function_models import ValidatedFunction


class CookiejarFromDict:
    """Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    :rtype: CookieJar"""

    # Original function signature: (cookie_dict, cookiejar=None, overwrite=True)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.cookiejar_from_dict

    model = ValidatedFunction(requests.cookies.cookiejar_from_dict).model


from pydantic_function_models import ValidatedFunction


class CreateCookie:
    """Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie")."""

    # Original function signature: (name, value, **kwargs)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.create_cookie

    model = ValidatedFunction(requests.cookies.create_cookie).model


from pydantic_function_models import ValidatedFunction


class ExtractCookiesToJar:
    """Extract the cookies from the response into a CookieJar.

    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
    :param request: our own requests.Request object
    :param response: urllib3.HTTPResponse object"""

    # Original function signature: (jar, request, response)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.extract_cookies_to_jar

    model = ValidatedFunction(requests.cookies.extract_cookies_to_jar).model


from pydantic_function_models import ValidatedFunction


class GetCookieHeader:
    """Produce an appropriate Cookie header string to be sent with `request`, or None.

    :rtype: str"""

    # Original function signature: (jar, request)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.get_cookie_header

    model = ValidatedFunction(requests.cookies.get_cookie_header).model


from pydantic_function_models import ValidatedFunction


class MergeCookies:
    """Add cookies to cookiejar and returns a merged CookieJar.

    :param cookiejar: CookieJar object to add the cookies to.
    :param cookies: Dictionary or CookieJar object to be added.
    :rtype: CookieJar"""

    # Original function signature: (cookiejar, cookies)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.merge_cookies

    model = ValidatedFunction(requests.cookies.merge_cookies).model


from pydantic_function_models import ValidatedFunction


class MorselToCookie:
    """Convert a Morsel object into a Cookie containing the one k/v pair."""

    # Original function signature: (morsel)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.morsel_to_cookie

    model = ValidatedFunction(requests.cookies.morsel_to_cookie).model


from pydantic_function_models import ValidatedFunction


class RemoveCookieByName:
    """Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n)."""

    # Original function signature: (cookiejar, name, domain=None, path=None)
    # Module: requests.cookies

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.cookies

        return requests.cookies.remove_cookie_by_name

    model = ValidatedFunction(requests.cookies.remove_cookie_by_name).model


__all__ = [
    "CookiejarFromDict",
    "CreateCookie",
    "ExtractCookiesToJar",
    "GetCookieHeader",
    "MergeCookies",
    "MorselToCookie",
    "RemoveCookieByName",
]
