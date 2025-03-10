"""Pydantic models for requests.hooks functions."""

import requests.hooks

from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DefaultHooks:
    """Pydantic model for function parameters."""

    # Original function signature: ()
    # Module: requests.hooks

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.hooks
        return requests.hooks.default_hooks

    model = ValidatedFunction(requests.hooks.default_hooks).model


from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import BaseModel, Field
from pydantic_function_models import ValidatedFunction

class DispatchHook:
    """Dispatches a hook dictionary on a given piece of data."""

    # Original function signature: (key, hooks, hook_data, **kwargs)
    # Module: requests.hooks

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests.hooks
        return requests.hooks.dispatch_hook

    model = ValidatedFunction(requests.hooks.dispatch_hook).model


__all__ = ['DefaultHooks', 'DispatchHook']
