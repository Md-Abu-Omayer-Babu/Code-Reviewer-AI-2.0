def commentFinder(python_code: str):
    comments = ""
    i = 0
    
    while i < len(python_code):
        if python_code[i] == "#":
            comment = ""
            while i < len(python_code) and python_code[i] != "\n":
                comment += python_code[i]
                i += 1
            comments += comment + "\n"
        else:
            i += 1
    
    if comments == "":
        return "No comments found"
    return comments


code = """
# This is a header comment
x = 5  # This is an inline comment
print(x)  # Output the value
"""
print(commentFinder(code))
