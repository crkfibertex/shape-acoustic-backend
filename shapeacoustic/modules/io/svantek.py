import os

class Svantek:
    def __init__(self):
        pass

    def split_measurements(self, file_path):
        print(f"Input file: {file_path}\n")

        with open(file_path, 'r') as file:
            lines = file.readlines()

        print(f"Read file.\n")

        measurement_start = "RT60 data saved by REW V5.30.9"
        measurement_blocks = []
        current_block = []

        for line in lines:
            if measurement_start in line and current_block:
                measurement_blocks.append(current_block)
                current_block = []
            current_block.append(line)
        
        if current_block:
            measurement_blocks.append(current_block)

        base_dir = os.path.dirname(file_path)
        base_name = os.path.basename(file_path).split('.')[0]

        for i, block in enumerate(measurement_blocks):
            new_file_path = os.path.join(base_dir, f"{base_name}_measurement_{i+1}.txt")
            with open(new_file_path, 'w') as new_file:
                new_file.writelines(block)
