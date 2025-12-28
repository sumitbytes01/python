class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
obj = ChaiUtils()
cleaned = obj.clean_ingredients("hello,  i , ,  am , you")
print(cleaned)


# no need of creating object
cleaned2 = ChaiUtils.clean_ingredients("hello.  , there, i ,,, am using,,    whatsapp!!    ")
print(cleaned2)