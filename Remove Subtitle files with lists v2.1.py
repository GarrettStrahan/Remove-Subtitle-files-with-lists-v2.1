#Renamed Remove SRT v2.0 to Remove Subtitle files with lists v2.1
#Changes this version supports remove .sub (subtitle files) as well as .srt files.
#Changes with Version 2.0 of this program allows the detection of strange character and will process the file even if there are odd character. Version 1.0 would crash and wouldn't output the new text file. This new program works correctly with strange characters
#Python script to process a text file containing a list of movies and it will remove all the elements (the lines in the file) that contains the .srt as the filename extension
#.srt file are subtitle files, if you use the dir > movies.txt to list your movies then this file will remove all the subtitle files out of the text file so you can get a correct count of movies.
#How to use this? Put your movies.txt in this python folder and run the script, then you will get a new file called newfile.txt
#Rename the file how you want and move it where you want.
#Programmed by Garrett Strahan
#Programmed with Python 3.12


import chardet

def detect_encoding(file_path):
    """Detect the encoding of a file."""
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def process_movie_list(input_file, output_file):
    try:
        # Detect the encoding of the input file
        encoding = detect_encoding(input_file)
        print(f"Detected encoding: {encoding}")

        # Read the input file with the detected encoding
        with open(input_file, 'r', encoding=encoding) as file:
            movie_list = file.readlines()

        # Remove newline characters and filter out items ending with .srt
        filtered_movies = [movie.strip() for movie in movie_list if not movie.strip().endswith('.srt')]
        filtered_movies = [movie.strip() for movie in movie_list if not movie.strip().endswith('.sub')]

        # Write the filtered list to the output file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            for movie in filtered_movies:
                file.write(movie + '\n')

        print(f"Filtered list saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'movies.txt' with your input file name
# Replace 'newfile.txt' with your desired output file name
input_file = 'movies.txt'
output_file = 'newfile.txt'

process_movie_list(input_file, output_file)
