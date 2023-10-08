import os
import json

# Initialize the recipe book as an empty dictionary
recipe_book = {}

# Function to load recipes from a JSON file
def load_recipes():
    if os.path.exists("recipe_book.json"):
        with open("recipe_book.json", "r") as file:
            return json.load(file)
    return {}

# Function to save recipes to a JSON file
def save_recipes():
    with open("recipe_book.json", "w") as file:
        json.dump(recipe_book, file)

# Function to add a recipe
def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    instructions = input("Enter the cooking instructions: ")
    recipe_book[name] = {"ingredients": ingredients, "instructions": instructions}
    save_recipes()
    print(f"Recipe for '{name}' added successfully!")

# Function to view all recipes
def view_recipes():
    if not recipe_book:
        print("No recipes found.")
    else:
        print("\nRecipes:")
        for name in recipe_book:
            print(f"- {name}")

# Function to view a specific recipe
def view_recipe(name):
    if name in recipe_book:
        recipe = recipe_book[name]
        print(f"\nRecipe: {name}")
        print("Ingredients: " + ", ".join(recipe["ingredients"]))
        print("Instructions:")
        print(recipe["instructions"])
    else:
        print(f"Recipe '{name}' not found.")

# Main loop
if __name__ == "__main__":
    recipe_book = load_recipes()

    while True:
        print("\nRecipe Book Menu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. View Recipe Details")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            name = input("Enter the recipe name: ")
            view_recipe(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")