# For Packet Process

UINT32 = 4
UINT16 = 2
UINT8 = 1


def join(msg, offset, hex_len):
    """Retrieves a section of the hex array and concatenates them into a string

    Parameters
    ----------
    msg: array/list
        The original hex data array
    offset: int
        The current position inside the data array
    hex_len:
        The length of the output string

    Returns
    -------
    out: str
        The specified concatenated hex array in string form

    """
    try:
        out = ''.join(msg[offset:offset + hex_len])
    except TypeError:
        raise TypeError('Input should be a hex array')
    return out


def header_offset_check(key):
    """Checks the header name and returns the hex length for it

    Parameters
    ----------
    key: str of header
        The header section name
    Returns
    -------
        The hex length for the corresponding header or 0 if no match

    """
    return {
        'ver': UINT16,
        'm_len': UINT16,
        'seq_no': UINT32,
        'time': UINT32,
        'set_id': UINT16,
        'set_len': UINT16,
    }.get(key, 0)


def template_check(template_id):
    """Checks the template ID and returns the template name corresponding to it

    Parameters
    ----------
    template_id: hex str of template id
        The template id retrieved from the parsed RAP packet
    Returns
    -------
       The corresponding template name associated with the hex value

    """
    return {
        '0001': 'SRC_IPV4',
        '0002': 'DST_IPV4',
        '0003': 'SRC_PORT',
        '0004': 'DST_PORT',
        '0005': 'PROTO',
        '0006': 'SRC_IPV6',
        '0007': 'DST_IPV6',
        '0008': 'IPV4_TOS',
        '0009': 'IPv6_FLOW_LABEL',
        '0010': 'PKT_COUNT',
        '0011': 'KBYTE_COUNT',
        '000a': 'CLASS_LABEL',
        '000b': 'MATCH_DIR',
        '000c': 'MSG_TYPE',
        '000d': 'TIME_TYPE',
        '000e': 'TIMEOUT',
        '000f': 'ACT_FLAG',
        '8000': 'ACT',
        '8001': 'ACT_PAR',
        '8002': 'CLASS_NAME',
        '8003': 'EXPORT_NAME',
        'c000': 'CLASS_TAG',
    }.get(template_id, '0000')


def msg_check(offset, template):
    """Checks the template ID and returns the hex length corresponding to it

    Parameters
    ----------
    offset: int
        The current position inside the data array
    template:
        The template name
    Returns
    -------
       The hex length for the corresponding template name or 0 if no match

    """
    return {
        'T_ID': 0,
        'T_FLAG': 0,
        'CLASS_NAME': UINT8 * 8,
        'MSG_TYPE': UINT8,
        'SRC_IPV4': UINT32,
        'DST_IPV4': UINT32,
        'SRC_PORT': UINT16,
        'DST_PORT': UINT16,
        'PROTO': UINT8,
        'PKT_COUNT': UINT32,
        'KBYTE_COUNT': UINT32,
        'TIME_TYPE': UINT8,
        'TIMEOUT': UINT16,
        'ACT': UINT8 * 8,
        'ACT_FLAG': UINT16,
        'ACT_PAR': UINT8 * template[-1],
    }.get(offset, 0)