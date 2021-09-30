"""
  Um exemplo de objetos com muitas dependências
"""

class Input: 
  def __init__(self, title):
    self.__title = title
    self.__value = ""
  
  def isValid(self):
    return len(self.__value) != 0

  @property
  def title(self):
    return self.__title 

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    self.__value = value

class Button: 
  def __init__(self, title):
    self.__title = title

  def click(self, inputs):
  
    valid = True
    for i in inputs:
      valid = i.isValid()
      if not valid:
        print("Valor invalido para: " + i.title)
        return
        
    print("Login realizado")
    
   
class Login:
  def __init__(self, emailInput, passInput, subimitButton):
    self.__emailInput = emailInput
    self.__passInput = passInput
    self.__subimitButton = subimitButton
  
  def send(self):
    self.__subimitButton.click([self.__emailInput, self.__passInput])
    
if __name__ == "__main__":
  button = Button("login")
  emailInput = Input("E-mail")
  passInput = Input("Senha")

  login = Login(emailInput, passInput, button)

  emailInput.value = "test@test.com"
  passInput.value = "test1234"

  login.send()

  
