def read_file_content(file_name):
    with open(file_name, "r") as f:
        return f.read()
def read_program(file_name):
    with open(file_name, "r") as f:
        print(f.read())
def run_program(code_file):
    for line_number, line in enumerate(code_file.split("\n"), 1):
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.upper().startswith("DISPLAY "):
            content = stripped[7:].strip()

            start = content.find('"')
            end = content.rfind('"')

            if start == -1 or end == -1 or end <= start:
                print(f"Line {line_number}: Missing quotes")
                continue

            text = content[start + 1:end]
            print(text)

        else:
            print(f"Line {line_number}: Unknown command")