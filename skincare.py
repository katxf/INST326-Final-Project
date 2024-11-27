"""
Group: Katherine Fuentes, Krista Mathew, Jigyasa Dahal, Afreen Ahmed
Assignment: Final Project Check-In 2 - Skincare
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
    self.user_log[date] = {"record": record}
    
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
    
  def skincare_recs(self): 
    """Skincare recommendations based on user's skin from products they have"""
    return[product.name for product in self.products if product.skin_type == self.user.skin_type]
    
  def skincare_sug(self, possible_products):
    """Suggests additional products that the user does not already own"""
    return [product.name for product in possible_products if product.skin_type == self.user.skin_type and not product.owned]
  
## Unit Tests and Example Usage
if __name__ == "__main__":
  """Invokes all the methods of class User, class Skincare_product, and Skincare_Advice.
    It sets an example user profile that states their skin type and what skin concern they are targetting """
    
    user = User("oily skin", ["hydration", "acne control"])
    user.log("2024-11-20", "oily skin")
    user.log("2024-11-21", "combo skin")

    """Defines each product on what skin type it is meant for and the purpose """  
    moisturizer = Skincare_Product("Oil-Free Moisturizer", "oily skin", "hydration")
    cleanser = Skincare_Product("Foaming Facial Cleanser", "oily skin", "hydration")
    sunscreen = Skincare_Product("SPF 50 Sunscreen", "combo skin", "UV protection")
    user_products = [moisturizer, cleanser, sunscreen]
  
    """States the product, what skin type it is meant for, its purpose, and whether user owns the product """
    possible_products = [
    Skincare_Product("Hydrating Serum", "dry skin", "hydration", owned = False),
    Skincare_Product("Toner", "oily skin", "acne control", owned = False),
    Skincare_Product("Oil-Free Moisturizer", "oily skin", "hydration", owned = True),
    Skincare_Product("SPF Sunscreen", "combo", "UV protection", owned = False)
    ]

    advice = Skincare_Advice(user, user_products)

    """Asserts the four main skin types and equates it to the corresponding object. """
    assert advice.skincare_recs() == ["Oil-Free Moisturizer", "Foaming Facial Cleanser"]
    assert advice.skincare_sug(possible_products) == ["Toner"]
    assert user.skin_profile()["user_log"]["2024-11-20"]["record"] == "oily skin"

    print(f"Recommended products that you own: {advice.skincare_recs()}")
    print(f"\nProducts you might want to purchase: {advice.skincare_sug(possible_products)}")
