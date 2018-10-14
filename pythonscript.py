import ast
import sys

code = """
a = [1, 6, "ok", 'lmao']
"""
AST = ast.parse(code)  # Remove this

# if len(sys.argv) > 1:
#     with open(sys.argv[1]) as file:
#         AST = ast.parse(file.read())


def generate(code):
    generated_code = ""

    def generate_event(event):
        def valueOf(obj):
            if isinstance(obj, ast.Name):
                return obj.id
            elif isinstance(obj, ast.Num):
                return obj.n
            elif isinstance(obj, ast.Str):
                return obj.s
            elif isinstance(obj, ast.Dict):
                obj_dict = {}
                for key, val in zip(obj.keys, obj.values):
                    obj_dict[valueOf(key)] = valueOf(val)
                return obj_dict
            elif isinstance(obj, ast.List):
                obj_list = list(map(valueOf, obj.elts))
                return obj_list
            else:
                raise Exception("Unknown type: %s" % str(type(event.value)))

        event_code = ""
        if isinstance(event, ast.Assign):
            event_code = "var "
            for target in event.targets:
                if isinstance(target, ast.Name):
                    event_code += target.id
                    event_code += " = "
                else:
                    raise Exception("Unknown target.")
            event_code += str(valueOf(event.value))
        elif isinstance(event, ast.Expr):
            ... # TODO: Allow expressions
        else:
            raise Exception("Unknown event.")

        return event_code + ";\n"

    AST = ast.parse(code)

    for event in AST.body:
        generated_code += generate_event(event)

    return generated_code

print(generate(code))
