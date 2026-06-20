def validate(result):

    if result["out_of_pocket"] < 0:
        return False

    return True