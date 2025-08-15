#!/usr/bin/env python3
"""
Setup script for para_notes application.
Creates the necessary folder structure and files.
"""

import os
import sys
from pathlib import Path


def initialize(destination=None):

    if destination is None:
        destination = os.getcwd()
    
    # Convert destination to Path object
    dest_path = Path(destination)
    
    # Create overarching folder for app data
    para_notes_path = dest_path / "para_notes"
    
    try:
        para_notes_path.mkdir(exist_ok=True)
        print(f"Created main directory: {para_notes_path}")
        
        # Create the 5 categories 
        subfolders = [
            "Projects",
            "Areas", 
            "Resources",
            "Archives",
            "Unorganized"
        ]
        
        for folder in subfolders:
            folder_path = para_notes_path / folder
            folder_path.mkdir(exist_ok=True)
            print(f"Created subfolder: {folder_path}")
        
        # Create folders.txt file with folder information
        folders_txt_path = para_notes_path / "folders.txt"
        folders_content = "Projects\n"
        folders_content += "Areas\n"
        folders_content += "Resources\n"
        folders_content += "Archives\n"
        folders_content += "Unorganized"
        
        with open(folders_txt_path, 'w', encoding='utf-8') as f:
            f.write(folders_content)
        
        print(f"Created folders.txt: {folders_txt_path}")
        print(f"\nApplication Initialized!")
        return str(para_notes_path)
        
    except Exception as e:
        print(f"Error Initializing: {e}")
        return None


def main():
    if len(sys.argv) > 1:
        destination = sys.argv[1]
        print(f"Using specified destination: {destination}")
    else:
        destination = None
        print("Using current directory as destination")
    
    result = initialize(destination)
    
    if result:
        print(f"Location: {result}")
    else:
        print("\nApplication Initialization Failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
