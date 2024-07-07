import wave
import numpy as np

def embed_data(audio_file, secret_message, output_file):
    audio = wave.open(input.wav , 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    secret_bits = ''.join([format(ord(char), '08b') for char in secret_message])
    secret_bits += '1111111111111110'  # Delimiter

    if len(secret_bits) > len(frame_bytes) * 8:
        raise ValueError("Secret message is too large to fit in the audio file.")
    
    for i in range(len(secret_bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(secret_bits[i])
    
    with wave.open(output_file, 'wb') as modified_audio:
        modified_audio.setparams(audio.getparams())
        modified_audio.writeframes(bytes(frame_bytes))
    
    audio.close()
    print("Data embedded successfully.")

def extract_data(stego_audio_file):
    audio = wave.open(stego_audio_file, 'rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    secret_bits = ''.join(map(str, extracted_bits))
    secret_message = ''.join([chr(int(secret_bits[i:i+8], 2)) for i in range(0, len(secret_bits), 8)])
    secret_message = secret_message.split('1111111111111110')[0]
    audio.close()
    return secret_message

# Example usage for embedding
embed_data('input.wav', 'Secret Message', 'output.wav')

# Example usage for extracting
extracted_message = extract_data('output.wav')
print("Extracted Message:", extracted_message)
