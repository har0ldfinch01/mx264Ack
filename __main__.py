import demux
import os
if __name__ == "__main__":
    # Specify the input MKV file and output directory
    input_file = 'input.mkv'
    output_dir = os.getcwd()

    # Call the demux_mkv function
    demux.demux_mkv("Drive.2011.1080p.BluRay.DTS.x264.D-Z0N3.mkv", output_dir)