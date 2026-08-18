import os
from unittest.mock import patch
from tests.utils import app, cmd_args, runner, mock_comp
from sgpt.role import DefaultRoles, SystemRole

@patch("sgpt.handlers.handler.completion")
def test_shell(completion):
    role = SystemRole.get(DefaultRoles.SHELL.value)
    completion.return_value = mock_comp("git commit -m test")
    args = {"prompt": "make a commit using git", "--shell": True}
    result = runner.invoke(app, cmd_args(**args))
    print(f"Exit code: {result.exit_code}")
    print(f"Exception: {result.exception}")
    print(f"Output: {result.output}")
    print(f"Calls: {completion.call_args_list}")

test_shell()
