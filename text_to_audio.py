from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False).to(device = "cpu")

def text_to_audio(text):    
    tts.tts_to_file(text=text, file_path='output.wav')
