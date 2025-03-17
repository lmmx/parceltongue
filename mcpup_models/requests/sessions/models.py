"""Pydantic models for requests.sessions functions."""

import requests.sessions

from pydantic_function_models import ValidatedFunction


class MergeHooks:
    """Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely."""

    # Original function signature: (request_hooks, session_hooks, dict_class=<class 'collections.OrderedDict'>)
    # Module: requests.sessions

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.sessions

        return requests.sessions.merge_hooks

    model = ValidatedFunction(requests.sessions.merge_hooks).model


from pydantic_function_models import ValidatedFunction


class MergeSetting:
    """Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`"""

    # Original function signature: (request_setting, session_setting, dict_class=<class 'collections.OrderedDict'>)
    # Module: requests.sessions

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.sessions

        return requests.sessions.merge_setting

    model = ValidatedFunction(requests.sessions.merge_setting).model


from pydantic_function_models import ValidatedFunction


class Session:
    """Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session"""

    # Original function signature: ()
    # Module: requests.sessions

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.sessions

        return requests.sessions.session

    model = ValidatedFunction(requests.sessions.session).model


__all__ = ["MergeHooks", "MergeSetting", "Session"]
