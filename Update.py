import os
import shutil

def sync_dirs(source_dir, dest_dir):
    """
    Recursively update all files and directories in dest_dir to match those in source_dir.
    """
    # Iterate through all files and directories in the source directory
    for name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, name)
        dest_path = os.path.join(dest_dir, name)
        
        # If it's a file, copy it over to the destination directory
        if os.path.isfile(source_path):
            shutil.copy2(source_path, dest_path)
            
        # If it's a directory, recurse into it and call this function again
        elif os.path.isdir(source_path):
            os.makedirs(dest_path, exist_ok=True)
            sync_dirs(source_path, dest_path)
            
        # If it's not a file or directory, ignore it
        else:
            pass



def main(source_dir, dest_dir):
    # Main code goes here
    sync_dirs(source_dir, dest_dir)
    # ...

if __name__ == "__main__":
    # Example usage
    source_dir = r"C:\Users\josip.nigojevic\Git\zaprobatskriptu\src"
    dest_dir = r"C:\Users\josip.nigojevic\Git\zaprobatskriptu\dst"
    main(source_dir, dest_dir)
