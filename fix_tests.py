with open("tests/test_shell.py", "r") as f:
    content = f.read()

# For test_shell
content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, args["prompt"]))',
    'completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_EXECUTION_MODEL")))'
)

# For test_shell_stdin
content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, expected_prompt))',
    'completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_EXECUTION_MODEL")))'
)

# For test_describe_shell
content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, args["prompt"]))',
    'completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

# For test_describe_shell_stdin
content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, expected_prompt))',
    'completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

# For test_shell_chat
content = content.replace(
    'expected_args = comp_args(role, "", messages=expected_messages)',
    'expected_args = comp_args(role, "", messages=expected_messages, model=cfg.get("GEMINI_EXECUTION_MODEL"))'
)

# For test_shell_repl
content = content.replace(
    'expected_args = comp_args(role, "", messages=expected_messages)',
    'expected_args = comp_args(role, "", messages=expected_messages, model=cfg.get("GEMINI_EXECUTION_MODEL"))'
)

with open("tests/test_shell.py", "w") as f:
    f.write(content)

