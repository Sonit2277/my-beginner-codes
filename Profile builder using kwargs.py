def build_profile(**kwargs):
    # print each key: value pair
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Example usage
build_profile(name="Alice", age=30, city="New York")
