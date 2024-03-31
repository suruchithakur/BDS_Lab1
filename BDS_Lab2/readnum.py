def calculate_call_summary(input_file, output_file):
    # Dictionary to store call durations for each phone number
    call_summary = {}

    # Read input file and process call data
    with open(input_file, 'r') as f:
        for line in f:
            data = line.strip().split()
            phone1, phone2, duration, _ = data
            
            # Update call summary for phone1
            if phone1 in call_summary:
                call_summary[phone1] += int(duration)
            else:
                call_summary[phone1] = int(duration)
                
            # Update call summary for phone2
            if phone2 in call_summary:
                call_summary[phone2] += int(duration)
            else:
                call_summary[phone2] = int(duration)

    # Write call summary to output file
    with open(output_file, 'w') as f:
        f.write("Phone number Class duration in seconds\n")
        for phone, duration in call_summary.items():
            f.write(f"{phone} {duration}\n")

    print("Call summary written to", output_file)

# Example usage:
input_file = "call_data.txt"
output_file = "call_summary.txt"
calculate_call_summary(input_file, output_file)
