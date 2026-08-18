with open("tests/test_shell.py", "r") as f:
    content = f.read()

content = content.replace('cfg.get("GEMINI_EXECUTION_MODEL", "gemini/gemini-flash-latest")', 'cfg.get("GEMINI_EXECUTION_MODEL")')
content = content.replace('cfg.get("GEMINI_LIGHTWEIGHT_MODEL", "gemini/gemini-flash-lite-latest")', 'cfg.get("GEMINI_LIGHTWEIGHT_MODEL")')

with open("tests/test_shell.py", "w") as f:
    f.write(content)
