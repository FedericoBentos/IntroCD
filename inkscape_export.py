import os
import subprocess

def svg2pdf(source_path, target_path):
    print(str(source_path))
    print(str(target_path))
    cmd = ["inkscape", str(source_path), "--export-area-drawing", "--export-type=pdf", "-o", str(target_path)]
    subprocess.run(cmd)