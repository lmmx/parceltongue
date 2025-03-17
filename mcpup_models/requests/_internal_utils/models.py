"""Pydantic models for requests._internal_utils functions."""

import requests._internal_utils

from pydantic_function_models import ValidatedFunction


class ToNativeString:
    """Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise."""

    # Original function signature: (string, encoding='ascii')
    # Module: requests._internal_utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests._internal_utils

        return requests._internal_utils.to_native_string

    model = ValidatedFunction(requests._internal_utils.to_native_string).model


from pydantic_function_models import ValidatedFunction


class UnicodeIsAscii:
    """Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool"""

    # Original function signature: (u_string)
    # Module: requests._internal_utils

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests._internal_utils

        return requests._internal_utils.unicode_is_ascii

    model = ValidatedFunction(requests._internal_utils.unicode_is_ascii).model


__all__ = ["ToNativeString", "UnicodeIsAscii"]
