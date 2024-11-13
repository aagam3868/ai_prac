# Fact base and rule base
knowledge_base = {
    "facts": {
        "animal_is_mammal": ["dog", "cat", "human"],
        "animal_is_bird": ["sparrow", "eagle"],
        "animal_lays_eggs": ["sparrow", "eagle", "crocodile"],
        "animal_has_fur": ["dog", "cat", "human"],
    },
    "rules": {
        "animal_is_mammal -> animal_has_fur": lambda animal: animal in knowledge_base["facts"]["animal_is_mammal"],
        "animal_is_bird -> animal_lays_eggs": lambda animal: animal in knowledge_base["facts"]["animal_is_bird"],
    }
}

# Inference engine
def infer(animal, fact):
    """
    Infer whether the given fact applies to the animal using rules.
    """
    for rule, condition in knowledge_base["rules"].items():
        rule_parts = rule.split(" -> ")
        premise = rule_parts[0].split("_")[2]  # animal_is_mammal -> animal_has_fur (We get mammal)

        # Check if the premise applies to the animal
        if condition(animal):
            if fact in rule_parts[1]:  # Check if inferred fact is present
                return f"Yes, the {animal} {fact.replace('_', ' ')}."

    return f"No, the {animal} does not {fact.replace('_', ' ')}."


# Query system
def query(animal, fact):
    # Check if the fact is explicitly known
    if fact in knowledge_base["facts"] and animal in knowledge_base["facts"][fact]:
        return f"Yes, the {animal} {fact.replace('_', ' ')}."
    # If not, use inference engine to check if it can be inferred
    return infer(animal, fact)


# Example Queries
animal = input("Enter the name of the animal: ").lower()
fact = input("Enter the fact to check (e.g., animal_has_fur, animal_lays_eggs): ").lower()

# Check the fact
result = query(animal, fact)
print(result)
