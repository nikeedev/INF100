def string_to_data(content_string):
    bits = []
    for c in content_string:
        for x in f'{ord(c):08b}':
            bits.append(int(x))
    
    # print(bits)
    return bits

def get_core_bit_list(content_string):
    mode_bits = [0, 1, 0, 0]
    len_bits = [int(x) for x in f'{len(content_string):08b}']
    data = string_to_data(content_string)
    terminator = [0, 0, 0, 0]

    bits = mode_bits + len_bits + data + terminator

    return bits

def pad_bit_list(core_bit_list: list, pad_to_bytes: int):
    diff = True
    
    padding_len = ((pad_to_bytes * 8) - len(core_bit_list))//8

    if padding_len == 0:
        return core_bit_list

    #print(f"\n-----\npadding_len: {padding_len}\n------")

    for i in range(padding_len):
        if diff:
            core_bit_list += [1, 1, 1, 0, 1, 1, 0, 0]
            diff = False
        else:
            core_bit_list += [0, 0, 0, 1, 0, 0, 0, 1]
            diff = True
    
    #print(f"\n-----\ncore bit list len: {len(core_bit_list)}\n------")
    #print(f"\n-----\ncore bit list len: {core_bit_list}\n------")
    return core_bit_list

def string_to_bit_list(content_string, qr_layout):
    complete_bit_list = []
    error_correction_level = ""

    core_bit_list = get_core_bit_list(content_string)
    
    core_bit_list_len = len(core_bit_list)

    for level in ["H", "Q", "M", "L"]:
        error_correction_bits = qr_layout["error_correction_bytes"][level] * 8

        if core_bit_list_len + error_correction_bits <= qr_layout["byte_capacity"]*8:
            error_correction_level = level
            break
    else:
        raise ValueError("For lite byte kapasitet tildelt. Klarer ikke å plassere feilrettingsnivå i bit-listen.")
    
    space_left = qr_layout["byte_capacity"] - qr_layout["error_correction_bytes"][level]
    complete_bit_list = pad_bit_list(core_bit_list, space_left)

    from qr6_error_correction import generate_error_correction 
    complete_bit_list = generate_error_correction(complete_bit_list, error_correction_level)

    return (complete_bit_list, error_correction_level)

# if __name__ == "__main__":




