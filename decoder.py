import wave
def extract_data(stego_audio_file):
    audio = wave.open(stego_audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    secret_bits = ''.join(map(str, extracted_bits))
    start_index = secret_bits.find('1111111111111110')
    secret_bits = secret_bits[:start_index]
    secret_message = ''.join([chr(int(secret_bits[i:i+8], 2)) for i in range(0, len(secret_bits), 8)])
    audio.close() 
    return secret_message
extracted_message = extract_data('output.wav')
print("Extracted Message:", extracted_message)
