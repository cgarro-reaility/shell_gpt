with open("tests/test_shell.py", "r") as f:
    content = f.read()

content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_EXECUTION_MODEL")))',
    'completion.assert_called_once_with(**comp_args(role, args["prompt"], model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

content = content.replace(
    'completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_EXECUTION_MODEL")))',
    'completion.assert_called_once_with(**comp_args(role, expected_prompt, model=cfg.get("GEMINI_LIGHTWEIGHT_MODEL")))'
)

with open("tests/test_shell.py", "w") as f:
    f.write(content)

