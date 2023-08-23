# ZoomCaptionsJson2srt
Convert Zoom captions JSON file to SRT subtitle format.

This Python script reads a JSON file containing Zoom captions, extracts the caption text, duration, and time information, and generates an SRT subtitle file with properly timed captions.

## Usage
1. Place your captions.json file in the same directory as the script.

2. Run the script by executing the following command in your terminal:

    ```bash
    python script.py
    ```
3. The generated SRT file named output.srt will be created in the same directory.

## Requirements
* Python 3.x
## File Structure
* script.py: The main Python script that reads the JSON file, parses the data, and creates the SRT file.
* captions.json: Input JSON file containing the Zoom captions.
* output.srt: Output SRT subtitle file with timed captions.
## Note
* Make sure your JSON file adheres to the required structure for captions.
* The time values in the JSON file should be in seconds.
## License
This project is licensed under the MIT License.