"""
Group: Katherine Fuentes, Krista Mathew, Jigyasa Dahal, Afreen Ahmed
Assignment: Final Project Check in 2 - Skincare
Date: 11/26/24
"""

##Layout of the code/Docstrings
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
  def __init__(self, user, products):
    """Sets the user's profile and their current products"""
    self.user = user
    self.products = products
    
  def skincare_recs(self, skin_type, owned, recs): 
    """Skincare recommendations based on user's skin from products they have"""
    self.skin_type = skin_type
    self.owned = owned 
    self.recs = {skin_type:owned}
    
  def skincare_sug(self, newProducts, skin_type, new_routine):
    """Suggests additional products that the user does not already own"""
    self.newProducts = []
    self.skin_type = skin_type 
    self.new_routine = new_routine 
  
## Unit Tests and Example Usage
"""Asserts the four main skin types and equates it to the corresponding object. """

assert self.skin_type == "combo skin" 
assert self.skin_type == "oily skin" 
assert self.skin_type == "normal skin" 
assert self.skin_type == "dry skin"
assert advice.skincare_recs() == ["Oil-Free Moisturizer", "SPF 50 Sunscreen"]
assert advice.skincare_sug(possible_products) == ["Toner"]
assert user.skin_profile()["user_log"]["2024-11-20"]["record"] == "oily skin"

if __name__ == "__main__":
  user = User("oily skin", ["hydration", "acne control"])
  user.log("2024-11-20", "oily skin", "skin is oily with slight texture")
  user.log("2024-11-21", "combo skin", "skin has improved but texture remains")
  
  moisturizer = Skincare_Product("Oil-Free Moisturizer", "oily skin", "hydration")
  cleanser = Skincare_Product("Foaming Facial Cleanser", "oily skin", "hydration")
  sunscreen = Skincare_Product("SPF 50 Sunscreen", "combo skin", "UV protection")
  user_products = [moisturizer, cleanser, sunscreen]

  possible_products = [
    Skincare_Product("Hydrating Serum", "dry skin", "hydration", owned = False),
    Skincare_Product("Toner", "oily skin", "acne control", owned = False),
    Skincare_Product("Oil-Free Moisturizer", "oily skin", "hydration", owned = True),
    Skincare_Product("SPF sunscreen", "combo", "UV protection", owned = False)
  ]

  advice = Skincare_Advice(user, user_products)

  print(f"Recommended products that you own: {advice.skincare_sug(skincare_recs()}")
  print(f"\nProducts you might want to purchase: {adivce.skincare_sug(possible_products)}")
