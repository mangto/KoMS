# 
# KOrean Morpheme Seperater (based on CREAM)
# github: @mangto  instagram: @imj._.mg
# 

import re

class KoMS:
    def __init__(self):
        return None

    def _seperate_every_case(self, text:str) -> list([ list, list, ...]):
        return 0;

    def clean_text(self, text:str) -> str:
        ''' added version: 0.0.1

        re 모듈을 통해 특수문자를 제거합니다.
        * Remove special characters with "re" module

        알파벳, 숫자, 한글을 제외한 특수문자들이 사라지며, 띄어쓰기는 사라지지 않습니다.
        * It removes every special characters except English, Korean and numbers, and spaces are not removed.
        '''

        result = re.sub('[^\uAC00-\uD7A30-9a-zA-Z\s]', '', text)
        return result

    def spacing_correction(self, text:str, clean_text:bool=False) -> str:
        ''' added version: 0.0.1

        aho corasick(아호 코라식) 알고리즘을 통해 띄어쓰기를 보정합니다.
        * It uses aho corasick algorithm for spacing correction.

        clean_text 값을 True로 지정해 특수문자를 제거할 수 있습니다.
        * You can make "clean_text" "True" to remove special characters. 
        '''

        assert type(text) == str, f"invalid text type: {type(text)}"

        if (clean_text): text = self.clean_text(text)
        result = text.replace(" ", "")
        
        return result