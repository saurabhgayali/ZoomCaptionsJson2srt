import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_path}'.")
        return None

def parse_captions(json_data):
    parsed_captions = []
    for entry in json_data:
        caption = entry.get("Caption")
        duration = entry.get("CaptionDuration")
        time = entry.get("Time")
        if caption is not None and duration is not None and time is not None:
            parsed_captions.append({
                "Caption": caption,
                "CaptionDuration": duration,
                "Time": time
            })
    return parsed_captions

def create_srt_file(captions, output_file_path):
    try:
        with open(output_file_path, 'w') as srt_file:
            caption_number = 1
            for caption in captions:
                start_time = caption["Time"]
                end_time = start_time + caption["CaptionDuration"]
                srt_file.write(f"{caption_number}\n")
                srt_file.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
                srt_file.write(f"{caption['Caption']}\n\n")
                caption_number += 1
        print(f"SRT file '{output_file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    file_path = 'captions.json'
    json_content = read_json_file(file_path)
    if json_content:
        parsed_data = parse_captions(json_content)
        output_file_path = 'output.srt'
        create_srt_file(parsed_data, output_file_path)

if __name__ == "__main__":
    main()
