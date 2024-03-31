def map_function(input_file):
    call_durations = {}  # Dictionary to store call durations for each phone number

    # Read input file and process call data
    with open(input_file, 'r') as f:
        for line in f:
            # Split the line by whitespace into a list of elements
            data = line.strip().split()
            
            # Ensure that there are at least 4 elements in the data list
            if len(data) >= 4:
                phone1 = data[0]  # First element is phone1
                phone2 = data[1]  # Second element is phone2
                duration = data[2]  # Third element is duration
            else:
                # If there are not enough elements, skip this line
                continue
            
            # Update call duration for phone1
            if phone1 in call_durations:
                call_durations[phone1] += int(duration)
            else:
                call_durations[phone1] = int(duration)
                
            # Update call duration for phone2
            if phone2 in call_durations:
                call_durations[phone2] += int(duration)
            else:
                call_durations[phone2] = int(duration)

    # Output phone numbers and call durations
    for phone, duration in call_durations.items():
        print(f"{phone}\t{duration}")

# Example usage:
input_file = "call_data.txt"
map_function(input_file)
