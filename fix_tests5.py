with open("tests/_integration.py", "r") as f:
    content = f.read()

content = content.replace('assert cfg.get("DEFAULT_MODEL") == "gemini-pro-latest"', 'assert cfg.get("DEFAULT_MODEL") == "gemini/gemini-pro-latest"')

with open("tests/_integration.py", "w") as f:
    f.write(content)
