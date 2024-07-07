import wave
def embed_data(audio_file, secret_message, output_file):
    
    audio = wave.open(audio_file, 'rb')
    
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    secret_bits = ''.join([format(ord(char), '08b') for char in secret_message])
    secret_bits += '1111111111111110'
    if len(secret_bits) > len(frame_bytes) * 8:
        raise ValueError("Secret message is too large to fit in the audio file.")
    
    for i in range(len(secret_bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(secret_bits[i])
    
    with wave.open(output_file, 'wb') as modified_audio:
        modified_audio.setparams(audio.getparams())
        modified_audio.writeframes(bytes(frame_bytes))
    
    audio.close()
    print("Data embedded successfully.")
    embed_data('input.wav', 'pw@56789', 'output.wav')
