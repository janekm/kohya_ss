import os
import argparse

def main(args):
    '''Move files that have captions to output_directory'''
    input_directory = args.input_directory
    output_directory = args.output_directory
    caption_directory = args.caption_directory
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over all files in the input directory
    for file in os.listdir(input_directory):
        # Split the file name into the base name and the extension
        base_name, file_extension = os.path.splitext(file)

        # Check if there is a corresponding caption file in the caption directory
        caption_file = os.path.join(caption_directory, base_name + ".txt")
        if os.path.exists(caption_file):
            # If there is, move the file and the caption file to the output directory
            input_file = os.path.join(input_directory, file)
            output_file = os.path.join(output_directory, file)
            os.rename(input_file, output_file)

            output_caption_file = os.path.join(output_directory, base_name + ".txt")
            os.rename(caption_file, output_caption_file)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("input_directory", type=str, help="input directory for train images")
  parser.add_argument("output_directory", type=str, help="output directory for train images")
  parser.add_argument("caption_directory", type=str, help="directory for train captions")

  args = parser.parse_args()

  main(args)
