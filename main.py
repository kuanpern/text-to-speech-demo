import json
import base64
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# read configs
from configs import default_voice_settings


# read sample input
logger.info("Reading sample input...")
with open('assets/samples.json', 'r') as fin:
    content = json.load(fin)
    text = content['text']
# end with

# instantiate the synthesizer
logger.info("Instantiating the synthesizer...")
from synthesizers import GCPSpeechSynthesizer
gcp_speech_synthesizer = GCPSpeechSynthesizer(
    endpoint='https://texttospeech.googleapis.com/v1/text:synthesize',
    default_voice_settings=default_voice_settings
) # end gcp_speech_synthesizer

# synthesize_speech
logger.info("Synthesizing speech...")
audio_content = gcp_speech_synthesizer.synthesize_speech(
    text=text,
    language_code="en-GB"
) # end gcp_speech_synthesizer.synthesize_speech
audio_content = base64.b64decode(audio_content)

# write_to_file
output_file = 'sample-audio-output.mp3'
logger.info("Writing to file ({})...".format(output_file))
with open(output_file, 'wb') as fout:
    fout.write(audio_content)
# end with

logger.info("Done!")