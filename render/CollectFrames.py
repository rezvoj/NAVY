import os, glob, subprocess


def collect_saved_frames(folder: str, output: str, fps=23, pattern='*.png'):
    patern_path = os.path.join(folder, pattern)
    output_path = os.path.join(folder, output)
    subprocess.run([
            'ffmpeg', '-y', '-framerate', str(fps), '-pattern_type', 'glob', '-i', patern_path, '-filter_complex',
            "[0:v] split [a][b]; [a] palettegen=stats_mode=full [p]; [b][p] paletteuse=dither=bayer:bayer_scale=3", 
            output_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE
    )
    for file in glob.glob(patern_path):
        os.remove(file)
