import os

if __name__ == "__main__":
    src = []
    for root, dirs, files in os.walk('s2'):
        for file in files:
            if 'test' not in file and file.endswith('.cc'):
                src.append(os.path.relpath(os.path.join(root, file)).replace('\\', '/') + '\n')
    
    with open('src.txt', 'w') as f:
        f.writelines(src)