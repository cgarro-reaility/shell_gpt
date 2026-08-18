with open("tests/test_shell.py", "r") as f:
    content = f.read()

# Make them all EXECUTION_MODEL first
content = content.replace('cfg.get("GEMINI_LIGHTWEIGHT_MODEL")', 'cfg.get("GEMINI_EXECUTION_MODEL")')

# Then set LIGHTWEIGHT for describe_shell tests
content = content.replace(
    'test_describe_shell(completion):\n    completion.return_value = mock_comp("lists the contents of a folder")\n    role = SystemRole.get(DefaultRoles.DESCRIBE_SHELL.value)\n\n    args = {"prompt": "ls", "--describe-shell": True}\n    result = runner.invoke(app, cmd_args(**args))\n\n    completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_EXECUTION_MODEL")))',
    'test_describe_shell(completion):\n    completion.return_value = mock_comp("lists the contents of a folder")\n    role = SystemRole.get(DefaultRoles.DESCRIBE_SHELL.value)\n\n    args = {"prompt": "ls", "--describe-shell": True}\n    result = runner.invoke(app, cmd_args(**args))\n\n    completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

content = content.replace(
    'test_describe_shell_stdin(completion):\n    completion.return_value = mock_comp("lists the contents of a folder")\n    role = SystemRole.get(DefaultRoles.DESCRIBE_SHELL.value)\n\n    args = {"--describe-shell": True}\n    stdin = "What is in current folder"\n    result = runner.invoke(app, cmd_args(**args), input=stdin)\n\n    expected_prompt = f"{stdin}"\n    completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_EXECUTION_MODEL")))',
    'test_describe_shell_stdin(completion):\n    completion.return_value = mock_comp("lists the contents of a folder")\n    role = SystemRole.get(DefaultRoles.DESCRIBE_SHELL.value)\n\n    args = {"--describe-shell": True}\n    stdin = "What is in current folder"\n    result = runner.invoke(app, cmd_args(**args), input=stdin)\n\n    expected_prompt = f"{stdin}"\n    completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

with open("tests/test_shell.py", "w") as f:
    f.write(content)
