with open("sgpt/handlers/handler.py", "r") as f:
    content = f.read()

# We need to fix the tool call aggregation logic.
# LiteLLM sometimes sends multiple tool calls in a single chunk or splits them weirdly.
# Currently, it aggregates ALL arguments across ALL tool calls into a single string.
# Let's see how tool calls are aggregated.
