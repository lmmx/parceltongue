"""Pydantic models for requests.adapters functions."""

import requests.adapters

from pydantic_function_models import ValidatedFunction


class Socksproxymanager:
    """Pydantic model for function parameters."""

    # Original function signature: (*args, **kwargs)
    # Module: requests.adapters

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.adapters

        return requests.adapters.SOCKSProxyManager

    model = ValidatedFunction(requests.adapters.SOCKSProxyManager).model


__all__ = ["Socksproxymanager"]
