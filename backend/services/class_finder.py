import ast

class ClassFinder:
    @staticmethod
    def find_classes(python_code: str) -> list:
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
    
    @staticmethod
    def find_classes_with_parents(source_code: str):
        class_info = []
        try:
            tree = ast.parse(source_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    bases = [base.id if isinstance(base, ast.Name) else ast.unparse(base)
                             for base in node.bases]
                    class_info.append({"class_name": node.name, "parent_classes": bases})
        except Exception as e:
            print("AST parsing error:", e)
        return class_info

