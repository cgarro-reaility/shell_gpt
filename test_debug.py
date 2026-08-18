import os
from tests.utils import app, cmd_args, runner

args = {"prompt": "make a commit using git", "--shell": True}
result = runner.invoke(app, cmd_args(**args))
print(f"Exception: {result.exception}")
import traceback
if result.exception:
    traceback.print_exception(type(result.exception), result.exception, result.exception.__traceback__)
