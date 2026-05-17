import profiles

def execute_tool(tool_name, target):
    return profiles.TOOL_REGISTRY[tool_name](target)


def run(profile_name, target):
    profile = profiles.DISCOVERY_PROFILES[profile_name]

    results = []

    for tool_name in profile["tools"]:
        results.append(execute_tool(tool_name, target))

    return results