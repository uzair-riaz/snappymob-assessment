from random_object_generator import RandomObjectGenerator

def write_random_objects_to_file(file_path):
    # target_size_in_bytes = 10 * 1024 * 1024
    target_size_in_bytes = 1000

    with open(file_path, "w") as file:
        current_size = 0
        while current_size < target_size_in_bytes:
            random_object = str(RandomObjectGenerator.generate_random_object())
            if current_size > 0:
                file.write(',')
            file.write(random_object)
            current_size += len(random_object)

if __name__ == "__main__":
    write_random_objects_to_file("random_objects.txt")