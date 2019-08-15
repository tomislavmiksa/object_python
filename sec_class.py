class SecretString:
     def __init__(self, plain_string, pass_phrase ):
          self._plain_string = plain_string
          self.__pass_phrase = pass_phrase

     def decrypt(self, pass_phrase):
          if pass_phrase == self. __pass_phrase:
               return self._plain_string
          else:
               return 'corak'
           
     def pwd(self, pass_phrase):
          if pass_phrase == self. __pass_phrase:
               return self.__pass_phrase
          else:
               return 'corak'
