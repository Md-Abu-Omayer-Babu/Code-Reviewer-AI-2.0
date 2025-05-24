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
    def find_classes_with_parents(python_code: str):
        code = '''
            class Animal:
                pass

            class Dog(Animal):
                pass

            class Cat(Animal):
                pass

            class Bat(Mammal, Flyer):
                pass

            class Fish:
                pass

            class Shark(Fish):
                pass
            '''
        
        '''
        returns 
        classes :
        {
            Animal: [Dog, Cat]
            Fish: [Shark]
        }
        '''

        parent_classes = {}
        
        lines = python_code.split("\n")
        for line in lines:
            line = line.strip().split("#")[0]
            if line.startswith("class "):
                # Extract class name and its parents
                class_name = line.split("class ")[1].split(":")[0].strip()
                if "(" in class_name:
                    class_name, parents = class_name.split("(")
                    class_name = class_name.strip()
                    parents = [p.strip() for p in parents.strip(")").split(",")]
                    for parent in parents:
                        if parent not in parent_classes:
                            parent_classes[parent] = []
                        parent_classes[parent].append(class_name)

        return parent_classes
