import os
import argparse
import csv

class REW():
    def __init__(self):
        pass

    def parse_export(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        measurement_start = "RT60 data saved by REW"
        measurement_blocks = []
        current_block = []

        for line in lines:
            if measurement_start in line and current_block:
                measurement_blocks.append(current_block)
                current_block = []
            current_block.append(line)
        
        if current_block:
            measurement_blocks.append(current_block)

        stripped_blocks = []
        for block in measurement_blocks:
            if len(block) > 15:  # Ensure there are enough lines to strip
                stripped_block = block[14:-1]
                stripped_blocks.append(stripped_block)

        # Parse each stripped block as CSV
        parsed_blocks = []
        for block in stripped_blocks:
            csv_reader = csv.reader(block)
            parsed_block = list(csv_reader)
            parsed_blocks.append(parsed_block)

        measurements = []
        # Example usage
        for block in parsed_blocks:
            for row in block:
                measurements.append({
                        "Frequency": int(row[0]),
                        "Topt": float(row[9])
                })
                
        averages = {}
        for measurement in measurements:
            frequency = measurement["Frequency"]
            topt = measurement["Topt"]

            if frequency in averages:
                averages[frequency] += topt / len(parsed_blocks)
            else:
                averages[frequency] = topt / len(parsed_blocks)

        return averages