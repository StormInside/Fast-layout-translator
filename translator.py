class Translator():

    ru = {
        "й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р",
        "о","л","д","ж","э","я","ч","с","м","и","т","ь","б","ю"
    }
    ru_caps = {
        "Х":"{","Ъ":"}","Ж":":",
        'Э':'"',"Б":"<","Ю":">",
    }
    ru_en = {
        "й":"q","ц":"w","ы":"s",
        "у":"e","к":"r","в":"d",
        "е":"t","с":"c","а":"f",
        "н":"y","м":"v","п":"g",
        "г":"u","и":"b","р":"h",
        "ш":"i","т":"n","о":"j",
        "щ":"o","ь":"m","л":"k",
        "з":"p","б":",","д":"l",
        "х":"[","ю":".","ж":";",
        "ъ":"]",".":"/","э":"'",
        "ф":"a",",":"?","я":"z",
        "ч":"x",
    }
    en_ru = {
        "q":"й","a":"ф","z":"я",
        "w":"ц","s":"ы","x":"ч",
        "e":"у","d":"в","c":"с",
        "r":"к","f":"а","v":"м",
        "t":"е","g":"п","b":"и",
        "y":"н","h":"р","n":"т",
        "u":"г","j":"о","m":"ь",
        "i":"ш","k":"л",",":"б",
        "o":"щ","l":"д",".":"ю",
        "p":"з",";":"ж","/":".",
        "[":"х","'":"э","?":",",
        "]":"ъ","{":"Х","}":"Ъ",
        ":":"Ж",'"':"Э","<":"Б",
        ">":"Ю","&":"?",
    }


    def translate(self, text):

        t = list(text)

        if self.check_language(text) == "RU":
            for i in range(0, len(t)):
                if (t[i] != " "):
                    if (t[i] in self.ru_caps):
                        t[i] = self.ru_caps[t[i]]
                    elif (t[i] in self.ru_en):
                        t[i] = self.ru_en[t[i]]
                    elif (t[i].lower() in self.ru_en):
                        t[i] = self.ru_en[t[i].lower()].upper()
        else:
             for i in range(0, len(t)):
                if (t[i] != " "):
                    if (t[i] in self.en_ru):
                        t[i] = self.en_ru[t[i]]
                    elif (t[i].lower() in self.en_ru):
                        t[i] = self.en_ru[t[i].lower()].upper()

        return "".join(t)

    def check_language(self, text):
        for s in text:
            if s != " ":
                if(s in self.ru or s in self.ru_caps or s.lower() in self.ru):
                    return "RU"
        return "EN"

