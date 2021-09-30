class Mediator():
  def notify(self, sender: object, event: str):
    pass

class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator

class Input(BaseComponent):
  def __init__(self, title: str):
    self.__title = title
    self.__value = ""

  @property
  def title(self):
    return self.__title 

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, value):
    self.__value = value

  def isValid(self):
    return len(self.__value) != 0

class Button(BaseComponent):
  def __init__(self, title: str):
    self.__title = title

  @property
  def title(self):
    return self.__title 

  def click(self):
    self.mediator.notify(self, "click")

class Login(Mediator):
  def __init__(self, emailInput: Input, passInput: Input, subimitButton: Button):
    self._emailInput = emailInput
    self._passInput = passInput
    self._subimitButton = subimitButton

    self._emailInput.mediator = self
    self._passInput.mediator = self
    self._subimitButton.mediator = self

  def notify(self, sender: object, event: str):
    if sender.title == "login" and event == "click":
      if not self._emailInput.isValid(): 
        print("Valor invalido para: " + self._emailInput.title)
      elif not self._passInput.isValid(): 
        print("Valor invalido para: " + self._passInput.title)
      else:
        # verificar se o usuário existe
        print("Login realizado")
        pass 
    

if __name__ == "__main__":
  button = Button("login")
  emailInput = Input("E-mail")
  passInput = Input("Senha")

  login = Login(emailInput, passInput, button)

  emailInput.value = "test@test.com"
  passInput.value = "test1234"

  button.click()

  
