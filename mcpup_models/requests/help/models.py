"""Pydantic models for requests.help functions."""

import requests.help

from pydantic_function_models import ValidatedFunction


class Info:
    """Generate information for a bug report."""

    # Original function signature: ()
    # Module: requests.help

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.help

        return requests.help.info

    model = ValidatedFunction(requests.help.info).model


from pydantic_function_models import ValidatedFunction


class Main:
    """Pretty-print the bug information as JSON."""

    # Original function signature: ()
    # Module: requests.help

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.help

        return requests.help.main

    model = ValidatedFunction(requests.help.main).model


__all__ = ["Info", "Main"]
