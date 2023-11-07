import pandas as pd
def generate_default_voice_settings():

    df = pd.read_csv('../assets/gcp_supported_language.csv')
    df.columns = ['Language', 'Voice type', 'languageCode', 'name', 'ssmlGender']
    vals = list(df.transpose().to_dict().values())

    output = {}
    for item in vals:
        name = item['name']
        name = list(name)[:-1]
        name.append('A')
        name = ''.join(name)
        output[item['languageCode']] = {
            "languageCode": item['languageCode'],
            "name": name,
            "ssmlGender": item['ssmlGender']
        }
    # end for
    return output
# end def