serial_number = ""
batteries = []
lit_indicators = []

def serial_number_last_odd() -> bool:
    return serial_number[-1].isalpha() and serial_number[-1] % 2 == 1
