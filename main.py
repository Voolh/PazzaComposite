from abc import ABC, abstractmethod


class PizzaIngredient(ABC):

    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def title(self) -> str:
        pass


class Ingredient(PizzaIngredient):

    def __init__(self, title: str, cost: int):
        self.__cost = cost
        self.__title = title

    def cost(self) -> int:
        return self.__cost

    def title(self) -> str:
        return self.__title


class PizzaParts(PizzaIngredient):

    def __init__(self, title: str):
        self.ingredients = []
        self.__title = title

    def cost(self) -> int:
        cost = 0
        for ingredient in self.ingredients:
            cost += ingredient.cost()
        return cost

    def title(self) -> str:
        return self.__title

    def add_ingredient(self, ingredient: PizzaIngredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient: PizzaIngredient):
        self.ingredients.remove(ingredient)

    def reset(self):
        self.ingredients = []


class Pizza(PizzaParts):

    def __init__(self, title: str):
        super(Pizza, self).__init__(title)

    def cost(self) -> int:
        pizza_price = 0

        for ingredient in self.ingredients:
            ingredient_cost = ingredient.cost()
            print(f"Cost is '{ingredient.title()}' = {ingredient_cost} credits")
            pizza_price += ingredient_cost

        print(f"Pizza price '{self.title()}' = {pizza_price} credits")

        return pizza_price


if __name__ == "__main__":

    dough = PizzaParts("dough")
    dough.add_ingredient(Ingredient('flour', 3))
    dough.add_ingredient(Ingredient('egg', 2))
    dough.add_ingredient(Ingredient('salt', 2))
    dough.add_ingredient(Ingredient('sugar', 3))

    sauce = Ingredient('BBQ', 11)

    topping = PizzaParts('topping')
    topping.add_ingredient(Ingredient('parmezane', 13))
    topping.add_ingredient(Ingredient('masdame', 9))
    topping.add_ingredient(Ingredient('mozarella', 7))

    pizza = Pizza('Cheese Pizza')
    pizza.add_ingredient(dough)
    pizza.add_ingredient(sauce)
    pizza.add_ingredient(topping)

    print(pizza.cost())