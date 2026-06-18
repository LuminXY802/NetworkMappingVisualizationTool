import scanner.profiles as profiles


def execute_tool(tool_name, target):
    if tool_name not in profiles.TOOL_REGISTRY:
        return {
            "tool": tool_name,
            "error": "unknown tool"
        }

    result = profiles.TOOL_REGISTRY[tool_name](target)

    return {
        "tool": tool_name,
        "data": result
    }


def run(profile_name, target):
    if profile_name not in profiles.DISCOVERY_PROFILES:
        raise ValueError("Invalid profile")

    profile = profiles.DISCOVERY_PROFILES[profile_name]

    results = []

    for tool_name in profile["tools"]:
        results.append(execute_tool(tool_name, target))

    return {
        "target": target,
        "profile": profile_name,
        "results": results
    }