from object_type import ObjectType

def read_random_objects_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            random_objects = file.read()
            objects = random_objects.split(",")

            for object in objects:
                object = object.strip()
                object_type = ObjectType.get_from_object(object)
                print("Object: ", object, "Type: ", object_type)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    read_random_objects_from_file("random_objects.txt")
