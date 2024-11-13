"""
Group: Katherine Fuentes, Krista Mathew, Jigyasa Dahal, Afreen Ahmed
Assignment: Final Project Check in - Skincare
Date: 11/12/24
"""

##Layout of the code/Docustrings
class User:
  """A class for the user's skin profile including skin type, goals, and their daily log"""
  def __init__(self, skin_type, goals):
    """Sets user's inputted skin type and goals for a certain day"""
    self.skin_type = skin_type
    self.goals = goals
    self.user_log = {}

  def log(self, date, record):
    """Log for the user's daily skin details"""
    self.user_log[date] = record
    
  def skin_profile(self): ## creates a profile for user which stores their own skin data
    """Returns user's profile information"""
    return {"skin_type": self.skin_type, "goals": self.goals, "user_log": self.user_log}

class Skincare_Product:
  """A class for skincare products that the user currently owns"""
  def __init__(self, name, skin_type, target, owned=True):
    """Sets the details for each of the user's currently owned skincare product"""
    self.name = name
    self.skin_type = skin_type
    self.target = target
    self.owned = owned
    
  def skincare_products(self):
    """Returns the user's skincare product information"""
    return {"name": self.name, "skin_type": self.skin_type, "target": self.target, "owned": self.owned}
class Skincare_Advice:
  """A class that recommends skincare products based on their current inventory and skin type. 
  As well as new products that the user does not own"""
def skincare_recs(): 
  """Skincare recommendations based on user's skin from products they have"""
  self.skin_type = skin_type
  self.owned = owned 
  self.recs = {skin_type:owned}
def skincare_sug(): 
  """Suggests additional products that the user does not already own"""
  self.newProducts = []
  self.skin_type = skin_type 
  self.new_routine = new_routine 
  
## Unit Tests 

assert self.owned == self.recs
assert self.owned != self.newProducts 
assert self.skin_type == "combo skin" 
assert self.skin_type == "oily skin" 
assert self.skin_type == "normal skin" 
assert self.skin_type == " dry skin"
