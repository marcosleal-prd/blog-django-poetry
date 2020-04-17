import os

from typing import Any


def get_env(var_name: str) -> str:
    env = os.getenv(var_name)
    if env is None:
        raise EnvironmentError(f"Environment variable {var_name} is not set!")

    return env


def eval_env_as_boolean(var_name: str, default: bool) -> bool:
    return eval_as_boolean(os.getenv(var_name), default)


def eval_as_boolean(value: Any, default: bool) -> bool:
    try:
        valid = {
            "true": True,
            "t": True,
            "y": True,
            "1": True,
            "false": False,
            "f": False,
            "0": False,
        }

        if isinstance(value, bool):
            return value

        if not isinstance(value, str):
            raise ValueError(
                f"Invalid literal for boolean. {value} not a string."
            )

        lower_value = value.lower()
        if lower_value in valid:
            return valid[lower_value]
        else:
            raise ValueError(f"Invalid literal for boolean: {value}")

    except (ValueError, Exception):
        return default
