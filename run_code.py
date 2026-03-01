def read_file_content(file_name):
    with open(file_name, "r") as f:
        return f.read()
def read_program(file_name):
    with open(file_name, "r") as f:
        print(f.read())
def run_program(code_file):
    variables = {}
    for line_number, line in enumerate(code_file.split("\n"), 1):
        stripped = line.strip()

        if not stripped:
            continue

        parts = stripped.split(None, 1)
        command = parts[0].upper()

        # ---------------- DISPLAY ----------------
        if command == "DISPLAY":
            if len(parts) < 2:
                print(f"Line {line_number}: DISPLAY needs an argument")
                continue

            content = parts[1].strip()

            # Variable support
            if content in variables:
                print(variables[content])

            # Quoted string
            elif content.startswith('"') and content.endswith('"'):
                print(content[1:-1])
            else:
                print(f"Line {line_number}: Invalid DISPLAY syntax")

        # ---------------- SET ----------------

                        
        # ---------------- UNKNOWN ----------------
# ---------------- ASSIGNMENT OR UNKNOWN ----------------
        else:
            if "=" not in stripped:
                print(f"Line {line_number}: Unknown command")
                continue

            name, value = map(str.strip, stripped.split("=", 1))
            if not name:
                print(f"Line {line_number}: Must set variable name")
                continue
            
            if not value:
                print(f"Line {line_number}: Must set a value")
                continue
            if "+" in value:
                left, right = map(str.strip, value.split("+", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val + right_val
                continue
            if "-" in value:
                left, right = map(str.strip, value.split("-", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val - right_val
                continue
            if "*" in value:
                left, right = map(str.strip, value.split("*", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val * right_val
                continue
            if "/" in value:
                left, right = map(str.strip, value.split("/", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val / right_val
                continue
            if "%" in value:
                left, right = map(str.strip, value.split("%", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val % right_val
                continue
            if "//" in value:
                left, right = map(str.strip, value.split("//", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val // right_val
                continue
            if "**" in value:
                left, right = map(str.strip, value.split("**", 1))


                # Try left operand
                if left in variables:
                    left_val = variables[left]
                else:
                    try:
                        left_val = float(left) if "." in left else int(left)
                    except ValueError:
                        print(f"Line {line_number}: Invalid left operand '{left}'")
                        continue

                # Try right operand
                if right in variables:
                    right_val = variables[right]
                else:
                    try:
                        right_val = float(right) if "." in right else int(right)
                    except ValueError:
                        print(f"Line {line_number}: Invalid right operand '{right}'")
                        continue

                # Store the result
                variables[name] = left_val ** right_val
                continue
            # -------- STRING --------
            if value.startswith('"'):
                if not value.endswith('"'):
                    print(f"Line {line_number}: Unclosed string")
                    continue
                variables[name] = value[1:-1]

            # -------- INTEGER ------ 
            else:
                try:
                    # First try integer
                    variables[name] = int(value)
                except ValueError:
                    try:
                        # Then try float
                        variables[name] = float(value)
                    except ValueError:
                        # -------- VARIABLE REFERENCE --------
                        if value in variables:
                            variables[name] = variables[value]
                        else:
                            print(f"Line {line_number}: Invalid value")
            