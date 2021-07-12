import re


class AllergenAssessment:
    def __init__(self, filename):
        self.filename = filename
        self.foods = []    # list of (ingredients, allergens)
        self.ingredient_for = {}  # allergen -> [ingredients] that might contain that allergen.
        self.ingredient_allergen = {}
        self.load()

    def load(self):
        line_re = re.compile("(.*) \\(contains (.*)\\)")

        with open(self.filename) as f:
            for line in f.readlines():
                m = line_re.match(line)
                if m is not None:
                    ingredients = m.group(1).split(' ')
                    allergens = [x.strip() for x in m.group(2).split(',')]
                    self.foods.append( (ingredients, allergens) )

                    # Start dict of ingredient->allergen, with no allergens known yet.
                    for ingredient in ingredients:
                        self.ingredient_allergen[ingredient] = None

    def determine_ingredients_for_allergens(self):
        # Go through all foods
        for food in self.foods:
            # For each allergen
            for allergen in food[1]:
                # If this allergen is new, add it to self.ingredient_for
                if allergen not in self.ingredient_for:
                    self.ingredient_for[allergen] = food[0]

                # Else, if this allergen isn't new, eliminate any ingredient that isn't in this food.
                else:
                    new_set = []
                    for i in self.ingredient_for[allergen]:
                        if i in food[0]:
                            new_set.append(i)
                    self.ingredient_for[allergen] = new_set

        # Now, for any allergen with only one possible ingredient, eliminate that ingredient from other allergens
        # Repeat until nothing changes
        change = True
        while change:
            change = False
            for allergen in self.ingredient_for:
                if len(self.ingredient_for[allergen]) == 1:
                    # Eliminate this from others
                    ingredient = self.ingredient_for[allergen][0]
                    # print(f"Eliminate {ingredient} from all but {allergen}")
                    for allergen2 in self.ingredient_for:
                        if allergen2 == allergen:
                            continue
                        # print(f"    Checking {allergen2}")
                        if ingredient in self.ingredient_for[allergen2]:
                            # print(f"    from {allergen2}")
                            self.ingredient_for[allergen2].remove(ingredient)
                            change = True

        # Set ingredient -> allergen map with known allergens now.
        for allergen in self.ingredient_for:
            ingredient = self.ingredient_for[allergen][0]
            self.ingredient_allergen[ingredient] = allergen

    def count_non_allergen_occurrences(self):
        occurrence = 0

        for food in self.foods:
            for ingredient in food[0]:
                if self.ingredient_allergen[ingredient] is None:
                    occurrence += 1

        return occurrence

    def cdil(self):
        s = ""
        for a in sorted(self.ingredient_for.keys()):
            s += f",{self.ingredient_for[a][0]}"
        return s[1:]  # Trim initial comma

    def part1(self):
        self.determine_ingredients_for_allergens()
        return self.count_non_allergen_occurrences()

    def part2(self):
        self.determine_ingredients_for_allergens()
        return self.cdil()

if __name__ == '__main__':
    aa = AllergenAssessment("data/day21_input.txt")
    print(f"CDIL: {aa.part2()}")


