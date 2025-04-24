def functionUnderClass(python_code: str):
    functions = {"Global_Functions": []}
    current_class = "Global_Functions"
    
    lines = python_code.split("\n")
    
    for line in lines:
        lines = line.lstrip()
        indentation_level = len(line) - len(lines)
        
        if lines.startswith("class "):
            class_name = lines.split()[1].split("(")[0].split(":")[0]
            current_class = class_name
            functions[current_class] = []
        
        elif lines.startswith("def "):
            function_name = lines.split()[1].split("(")[0]
            
            if indentation_level == 0:  # Function is at the global level
                functions["Global_Functions"].append(function_name)
            else:
                functions[current_class].append(function_name)
    
    return functions
