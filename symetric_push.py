import filecmp
import os
import shutil
import subprocess
import pyautogui
import time


def copy_missing_files(source_dir, dest_dir):
    # Get a list of all files and directories in the source directory
    source_items = os.scandir(source_dir)
    
    # Check each item in the source directory
    for item in source_items:
        # If it's a directory, check if it exists in the destination directory
        if item.is_dir():
            dir_name = item.name
            dest_path = os.path.join(dest_dir, dir_name)
            
            # If the directory doesn't exist in the destination directory, copy it (and its contents)
            if not os.path.exists(dest_path):
                shutil.copytree(item.path, dest_path)
                print(f"Copied directory '{dir_name}' to '{dest_dir}'")
            
            # If the directory already exists in the destination directory, recurse into it to copy its contents
            else:
                copy_missing_files(item.path, dest_path)
        
        # If it's a file, check if it exists in the destination directory
        elif item.is_file():
            file_name = item.name
            dest_path = os.path.join(dest_dir, file_name)
            
            # If the file doesn't exist in the destination directory, copy it
            if not os.path.exists(dest_path):
                shutil.copy2(item.path, dest_path)
                print(f"Copied file '{file_name}' to '{dest_dir}'")

def copy_missing_changes(source_dir, dest_dir):
    """
    Copies files and directories missing from either the source or destination directory to the other directory.
    If there are files of the same name in both directories that are different by content, copies the ones from the source directory to the destination.
    """
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Get the relative path of the current directory within the source directory
        rel_dirpath = os.path.relpath(dirpath, source_dir)
        # Construct the corresponding directory path within the destination directory
        dest_rel_dirpath = os.path.join(dest_dir, rel_dirpath)

        # Create the directory in the destination if it doesn't exist
        if not os.path.exists(dest_rel_dirpath):
            os.makedirs(dest_rel_dirpath)

        # Loop through the files in the current directory
        for filename in filenames:
            # Construct the full path of the file in the source directory
            src_file = os.path.join(dirpath, filename)
            # Construct the corresponding path of the file in the destination directory
            dest_file = os.path.join(dest_rel_dirpath, filename)

            # If the file doesn't exist in the destination directory, or if it has a different size or content, copy it from the source
            if not os.path.exists(dest_file) or not filecmp.cmp(src_file, dest_file):
                shutil.copy2(src_file, dest_file)


def git_commit_push(passphrase, key_path, path, commit_message):
    """
    Opens Git Bash, initializes the SSH agent, adds the key to the agent, performs a commit and push on the specified path,
    and then stops the SSH agent.
    """
    try:
        # Open Git Bash using the Windows search bar
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write('Git Bash')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)

        # Initialize the SSH agent
        pyautogui.write('eval $(ssh-agent -s)')
        pyautogui.press('enter')
        time.sleep(1)

        # Add the SSH key to the agent
        pyautogui.write(f'ssh-add {key_path}')
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write(passphrase)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write(f'cd {path}')
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('git add .')
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write(f'git commit -m "{commit_message}"')
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('git push -f')
        pyautogui.press('enter')
        time.sleep(10)

        # Stop the SSH agent
        pyautogui.write('ssh-agent -k')
        pyautogui.press('enter')
        time.sleep(1)

        print("Git commit and push successful.")

    except Exception as e:
        print(f"Git commit and push error: {e}")

def main(path_one, path_two):
    # u argumentu su isti pathovi ali jedni su apsolutni drugi su relativni, svaki za svoju upotrebu
    path='git/tost/Test'
    path2 = 'git/Test'
    key='Desktop/kljuc'
    passphrase = 'jaje'
    

    copy_missing_files(path_one, path_two)
    copy_missing_changes(path_one, path_two)
    git_commit_push(passphrase, key, path2, ' Automatizirano_pushanje.txt')
    git_commit_push(passphrase, key, path, ' Automatizirano_pushanje.txt')

# dodat subproces otvaranje git bash

# napisat u uputama da triba relocirat na grane na kojima se nalaze promjene na oba repa

# risit autentikaciju

# git add .

# git commit sa porukon 

# git push

# dodat da se prima string kao argument a on je git message







if __name__ == '__main__':
    path1 = r'C:\Users\josip\git\Test'
    path2 = r'C:\Users\josip\git\tost\Test'
    main(path1, path2)
