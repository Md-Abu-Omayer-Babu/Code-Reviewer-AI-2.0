class FunctionFinder:
    @staticmethod
    def find_functions(python_code: str) -> list:
        functions = []
        lines = python_code.split("\n")
        
        for line in lines:
            parts = line.split()
            if "def" in parts:
                if len(parts) > 1:
                    function_name = parts[1].split("(")[0]
                    functions.append(function_name)
        return functions
