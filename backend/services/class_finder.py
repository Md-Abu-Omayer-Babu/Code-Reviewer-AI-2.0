def classFinder(python_code: str):
    classes = []
    lines = python_code.split("\n")

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("class "):
            # Remove inline comment if any
            stripped = stripped.split("#")[0]
            parts = stripped.split()
            if len(parts) > 1:
                class_name = parts[1].split(":")[0].split("(")[0]
                classes.append(class_name)
    return classes
