def merge_files():
    input_file = '06.Project Input File.txt'
    merge_file = '06.Project Merge File.txt'
    output_file = '06.Project Output File.txt'

    # Initialize record counts
    input_count = 0
    merge_count = 0
    output_count = 0

    # Open the output file for writing
    with open(output_file, 'w') as output:
        # Open the input file for reading
        with open(input_file, 'r') as input:
            # Open the merge file for reading
            with open(merge_file, 'r') as merge:
                # Read the input file line by line
                for line in input:
                    input_count += 1  # Count the input file records
                    output.write(line)  # Write the input line to the output file

                    # If we encounter the placeholder, insert the merge file content
                    if '**Insert Merge File Here**' in line:
                        for merge_line in merge:
                            merge_count += 1  # Count the merge file records
                            output.write(merge_line)  # Write the merge line to the output file

                # After finishing the merge file, continue copying the remaining lines from the input file
                for line in input:
                    input_count += 1  # Count the input file records
                    output.write(line)  # Write the input line to the output file

                    output_count += 1  # Count each line written to the output

    # Count total records for input, merge, and output files
    with open(input_file, 'r') as input:
        input_count = len(input.readlines())

    with open(merge_file, 'r') as merge:
        merge_count = len(merge.readlines())

    with open(output_file, 'r') as output:
        output_count = len(output.readlines())

    # Print the number of records
    print(f"{input_count} input file records")
    print(f"{merge_count} merge file records")
    print(f"{output_count} output file records")


# Run the function
merge_files()

