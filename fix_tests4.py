with open("tests/test_shell.py", "r") as f:
    content = f.read()

content = content.replace('cfg.get("GEMINI_EXECUTION_MODEL")', 'cfg.get("GEMINI_EXECUTION_MODEL", "gemini/gemini-flash-latest")')
content = content.replace('cfg.get("GEMINI_LIGHTWEIGHT_MODEL")', 'cfg.get("GEMINI_LIGHTWEIGHT_MODEL", "gemini/gemini-flash-lite-latest")')

with open("tests/test_shell.py", "w") as f:
    f.write(content)
