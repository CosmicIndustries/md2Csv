import pandas as pd


# Function to convert markdown to CSV
def md_to_csv(filename):
    # Initialize an empty list to store the data
    data = []

    # Open the markdown file
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        # Variables to store the current user input and assistant output
        user_input = ""
        assistant_output = ""
        # Boolean to keep track of the text following headings
        in_input = False
        in_output = False
        # Iterate through each line in the file
        for line in lines:
            # Check if the line starts with "USER"
            if line.startswith("## USER"):
                # If there's previous user input and assistant output, add it to the data list
                if user_input and assistant_output:
                    data.append([user_input, assistant_output])
                    user_input = ""
                    assistant_output = ""
                in_input = True
                in_output = False
            elif line.startswith("## ASSISTANT"):
                in_input = False
                in_output = True
            else:
                if in_input:
                    user_input += line
                if in_output:
                    assistant_output += line
        # Add the last user input and assistant output to the data list
        if user_input and assistant_output:
            data.append([user_input, assistant_output])

    # Create a dataframe from the data list
    df = pd.DataFrame(data, columns=["User Input", "Assistant Output"])

    # Write the dataframe to a csv file
    df.to_csv(f"{filename}.csv", index=False)
    print(f"{filename}.csv")


# Take the input file name from the user
input_file = input("Enter the name of the markdown file: ")

# Call the md_to_csv function to convert the markdown to CSV
md_to_csv(input_file)

print('All done')
