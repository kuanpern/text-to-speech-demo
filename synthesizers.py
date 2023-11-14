import os
import requests
import google.auth
import google.auth.transport.requests

# refer to https://cloud.google.com/text-to-speech/docs/voices for available voices
# custom voice is not supported yet at the moment, need to contact Google sales team


class GCPSpeechSynthesizer:
    def __init__(self, 
        default_voice_settings,
        endpoint='https://texttospeech.googleapis.com/v1/text:synthesize'
    ):
        
        self.endpoint = endpoint
        self.default_voice_settings = default_voice_settings
        self.allowed_language_codes = list(default_voice_settings.keys())
        self.refresh_gcp_creds()
    # end def

    def refresh_gcp_creds(self):

        # assume env var GOOGLE_APPLICATION_CREDENTIALS is already set
        # creds, project_id = google.auth.default()
        credential_filepath = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        creds, project_id = google.auth.load_credentials_from_file(
            credential_filepath, 
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        ) # end google.auth.load_credentials_from_file

        auth_req = google.auth.transport.requests.Request()
        creds.refresh(auth_req)

        self.project_id = project_id
        self.creds = creds
    # end def

    def synthesize_speech(self, text, language_code, voice_setting=None, audio_encoding="mp3"):

        # validate input
        assert language_code in self.allowed_language_codes, "language_code must be one of {}".format(self.allowed_language_codes)

        # generate the payload
        if voice_setting is None:
            voice_setting = self.default_voice_settings[language_code]
        # end if
        payload = {
            "input":{
                "text": text
            },
            "voice": voice_setting,
            "audioConfig":{
                "audioEncoding": audio_encoding.upper()
            }
        } # end payload

        # generate the API request
        if self.creds.expired:
            self.refresh_gcp_creds()
        # end if

        headers = {
            'Authorization': 'Bearer ' + self.creds.token,
            'Content-Type': 'application/json; charset=utf-8',
            'x-goog-user-project': self.project_id,
        } # end headers

        r = requests.post(self.endpoint, headers=headers, json=payload)

        # TODO: validate response
        data = r.json()
        audio_content = data['audioContent']
        return audio_content
    # end def
# end class


