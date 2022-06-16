def is_valid(content, expected_type):
    if content != "":
        if expected_type == "str":
            try:
                content = str(content)
                if len(content) < 50:
                    return True
                else:
                    print("ookook")
                    return False
            except ValueError:
                return False

        if expected_type == "int":
            try:
                content = int(content)
                return True
            except ValueError:
                return False
    return False
