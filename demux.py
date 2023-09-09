import subprocess
import os

def demux_mkv(input_file, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get information about the tracks in the input MKV file
    track_info_command = ['mkvinfo', input_file]
    
    try:
        # Run the mkvinfo command to get track information
        track_info_output = subprocess.check_output(track_info_command, universal_newlines=True)

        # Split the output into lines
        lines = track_info_output.split('\n')

        # Initialize a list to store audio track IDs
        audio_track_ids = []

        # Parse the track information to find audio track IDs
        for line in lines:
            if "| + Track type: audio" in line:
                track_id = line.split(":")[0].strip()
                audio_track_ids.append(track_id)

        # Extract each audio track
        for track_id in audio_track_ids:
            output_file = os.path.join(output_dir, f'audio_track_{track_id}.mkv')
            extract_command = ['mkvextract', input_file, 'tracks', output_file, track_id]
            subprocess.run(extract_command, check=True)

        print(f"Demuxing of {input_file} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error demuxing {input_file}: {e}")

if __name__ == "__main__":
    output_dir = os.getcwd()
    print(output_dir)
    # Specify the input MKV file and output directory
    input_file = 'Drive.2011.1080p.BluRay.DTS.x264.D-Z0N3.mkv'
    output_dir = 'output'

    # Call the demux_mkv function
    demux_mkv(input_file, output_dir)
