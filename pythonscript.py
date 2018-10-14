#!/usr/bin/env python3
import ast
import sys


def generate(code):
    generated_code = "// Generated with Pythonscript.\n"

    def generate_event(event):
        def valueOf(obj):
            if isinstance(obj, ast.Name):
                return obj.id
            elif isinstance(obj, ast.Num):
                return obj.n
            elif isinstance(obj, ast.Str):
                return obj.s
            elif isinstance(obj, ast.NameConstant):
                if obj.value == True:
                    return 'true'
                elif obj.value == False:
                    return 'false'
                else:
                    return Exception("Unknown NameConstant")
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

    for event in ast.parse(code):
        generated_code += generate_event(event)

    return generated_code


if len(sys.argv) > 1:
    if sys.argv[1] == "gen":
        try:
            with open(sys.argv[2], 'r') as file:
                with open(sys.argv[3], 'w') as target:
                    target.write(generate(file.read()))
        except Exception as e:
            print("Error while generating & writing files:", e)
else:
    print("Generating code: pythonscript gen FILE TARGET")
