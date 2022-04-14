"""
The study of caesar ciphers of decoding / encoding a message
using a default offset of 13, or the specified offset.
Outputs the coded / decoded message.

The study of vigenere ciphers and rotation of letters based on
keyword letter index.  Interesting puzzle to figure out.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot_dict = {}

encode = True
decode = False

def create_rot_dict(offset, xcode=decode):
    """
    rotate_index + offset (above), let's avoid IndexError,
    by subtracting 26 (length of the alphabet) from the the rotidx
    (ie... 28 - 26 = 2 << new index number)
    build and then return the dictionary
    """
    if xcode == decode:
        offset = abs(offset - 26)
    for idx, char in enumerate(alphabet):
        rotidx = idx + offset
        if rotidx >= 26:
            rotidx -= 26
        rot_dict[char] = alphabet[rotidx]
    return rot_dict

def encode_decode(message):
    """
    iterate over the provided message
    if character is a space or special character,
    just add it in place (there is no rotation)
    update decoded_message from the rotation dictionary character
    """
    new_message = ""
    for char in message:
        if char not in alphabet:
            new_message += char
        else:
            new_message += rot_dict[char]
    return new_message

def convert(message, offset=13, xcode=encode):
    """
    lower the message
    create the rotation dict with the provided offset
    send the message for conversion
    return the message
    """
    message = message.lower()
    create_rot_dict(offset, xcode)
    new_message = encode_decode(message)
    return new_message

def find_offset(message):
    for i in range(26):
        print(f"{i}:\t{convert(message, i)}")

def create_keyword_ref(keyword):
    keyword_ref = []
    for key in keyword:
        k = alphabet.find(key)
        keyword_ref.append(k)
    return keyword_ref

def vigenere_encode(message, keyword):
    vigenere_str = ""
    keyword_ref = create_keyword_ref(keyword)
    key_idx = 0
    for char in message:
        if char not in alphabet:
            vigenere_str += char
        else:
            alpha_index = alphabet.find(char) + keyword_ref[key_idx]
            if alpha_index >= 26:
                alpha_index -= 26
            # print(alpha_index, keyword_ref[key_idx], alpha_index - keyword_ref[key_idx], alphabet[alpha_index])
            vigenere_str += alphabet[alpha_index]
            key_idx += 1
            if key_idx == len(keyword):
                key_idx = 0
    return vigenere_str


def vigenere_decode(message, keyword):
    vigenere_str = ""
    keyword_ref = create_keyword_ref(keyword)
    key_idx = 0
    for char in message:
        if char not in alphabet:
            vigenere_str += char
        else:
            alpha_index = alphabet.find(char) - keyword_ref[key_idx]
            if alpha_index < 0:
                alpha_index += 26
            # print(alpha_index, alphabet[alpha_index], keyword_ref[key_idx])
            vigenere_str += alphabet[alpha_index]
            key_idx += 1
            if key_idx == len(keyword):
                key_idx = 0
    return vigenere_str

if __name__ == '__main__':

    # rot
    message1 = "you were able to decode this? nice work! you are becoming quite the expert at cryptography!" # clear message (obvs)
    message2 = "lbh jrer noyr gb qrpbqr guvf? avpr jbex! lbh ner orpbzvat dhvgr gur rkcreg ng pelcgbtencul!" # rot, offset = 13 Working
    message3 = "fvb dlyl hisl av kljvkl aopz? upjl dvyr! fvb hyl iljvtpun xbpal aol lewlya ha jyfwavnyhwof!" # rot, offset = 7  Not working, need to do the math on this
    message3 = "vlr tbob xyib ql abzlab qefp? kfzb tloh! vlr xob ybzljfkd nrfqb qeb bumboq xq zovmqldoxmev!" # rot, offset = 7  Not working, need to do the math on this

    # print(create_rot_dict(13))
    # print(convert(message1, 23))
    #  -or- 
    # print(convert(message1, 23, encode))
    # print(create_rot_dict(7))
    # print(convert(message3, 23, decode))
    # find_offset(message3)


    # vigenere:
    # message4 = "qrz cljh fhsw wt jlurik azlx? tpuh buyc! bta hjh gkjgpntn ixnzl lkj kehhwz hl fwewlrlxhhkd!" # vigenere
    # keyword = "sdfgh"

    # print(vigenere_encode(message1, keyword))
    # print(vigenere_decode(message4, keyword))







