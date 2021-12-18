import os
import pathlib
import shutil

if __name__ == "__main__":
    p = pathlib.Path('tests/')
    p.mkdir(parents=True, exist_ok=True)

    dest_path = 'tests/{file}'
    
    for root, dirs, files in os.walk('s2/'):
        for file in files:
            if '_test' in file or 'testing' in file:
                print(os.path.join(root, file))
                shutil.move(os.path.join(root, file), dest_path.format(file = file))