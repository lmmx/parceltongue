"""Pydantic models for requests functions."""

import requests

from pydantic_function_models import ValidatedFunction


class CheckCompatibility:
    """Pydantic model for function parameters."""

    # Original function signature: (urllib3_version, chardet_version, charset_normalizer_version)
    # Module: requests

    @staticmethod
    def get_original_function():
        """Get the original function this model is based on."""
        import requests

        return requests.check_compatibility

    model = ValidatedFunction(requests.check_compatibility).model


__all__ = ["CheckCompatibility"]
