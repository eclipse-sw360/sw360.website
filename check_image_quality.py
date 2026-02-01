#!/usr/bin/env python3
"""
Script to identify low-quality/blurry images in the SW360 website repository.
This script scans all image files and reports those that are likely too small
or compressed to be useful for documentation.
"""

import os
import sys
from pathlib import Path

# Configuration
MIN_QUALITY_THRESHOLD_KB = 25  # Images under this size are flagged
CRITICAL_THRESHOLD_KB = 5      # Images under this size are critically low quality

# Directories to scan
IMAGE_DIRS = [
    "static/img/ImagesBasic",
    "static/img/sw360screenshots", 
    "static/img/workflow",
    "static/img/couchdb",
    "static/img/PackagesPage"
]

# Supported image extensions
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}

def get_file_size_kb(filepath):
    """Get file size in kilobytes"""
    try:
        size_bytes = os.path.getsize(filepath)
        return size_bytes / 1024
    except OSError:
        return 0

def scan_images(base_path):
    """Scan all images and categorize by quality"""
    critical_images = []
    low_quality_images = []
    acceptable_images = []
    
    for image_dir in IMAGE_DIRS:
        dir_path = Path(base_path) / image_dir
        
        if not dir_path.exists():
            print(f"Warning: Directory {dir_path} does not exist, skipping...")
            continue
            
        for ext in IMAGE_EXTENSIONS:
            for image_file in dir_path.rglob(f"*{ext}"):
                size_kb = get_file_size_kb(image_file)
                relative_path = image_file.relative_to(base_path)
                
                image_info = {
                    'path': str(relative_path),
                    'size_kb': size_kb,
                    'filename': image_file.name
                }
                
                if size_kb < CRITICAL_THRESHOLD_KB:
                    critical_images.append(image_info)
                elif size_kb < MIN_QUALITY_THRESHOLD_KB:
                    low_quality_images.append(image_info)
                else:
                    acceptable_images.append(image_info)
    
    return critical_images, low_quality_images, acceptable_images

def print_report(critical, low_quality, acceptable):
    """Print formatted report"""
    print("=" * 80)
    print("SW360 WEBSITE IMAGE QUALITY REPORT")
    print("=" * 80)
    print()
    
    # Critical images
    print(f"[CRITICAL] (Under {CRITICAL_THRESHOLD_KB}KB): {len(critical)} images")
    print("-" * 80)
    if critical:
        for img in sorted(critical, key=lambda x: x['size_kb']):
            print(f"  {img['size_kb']:>6.1f} KB  {img['path']}")
    else:
        print("  None found")
    print()
    
    # Low quality images
    print(f"[LOW QUALITY] ({CRITICAL_THRESHOLD_KB}KB - {MIN_QUALITY_THRESHOLD_KB}KB): {len(low_quality)} images")
    print("-" * 80)
    if low_quality:
        for img in sorted(low_quality, key=lambda x: x['size_kb']):
            print(f"  {img['size_kb']:>6.1f} KB  {img['path']}")
    else:
        print("  None found")
    print()
    
    # Acceptable images
    print(f"[ACCEPTABLE] (Over {MIN_QUALITY_THRESHOLD_KB}KB): {len(acceptable)} images")
    print("-" * 80)
    print(f"  {len(acceptable)} images meet quality standards")
    print()
    
    # Summary
    total_flagged = len(critical) + len(low_quality)
    total_images = len(critical) + len(low_quality) + len(acceptable)
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total images scanned: {total_images}")
    print(f"Images needing replacement: {total_flagged} ({total_flagged/total_images*100:.1f}%)")
    print(f"  - Critical: {len(critical)}")
    print(f"  - Low Quality: {len(low_quality)}")
    print()
    
    if total_flagged > 0:
        print("[!] Action required: Replace flagged images with higher quality versions")
        print("[i] See BLURRY_IMAGES_GUIDE.md for detailed instructions")
    else:
        print("[OK] All images meet quality standards!")
    
    print()

def generate_markdown_list(critical, low_quality):
    """Generate markdown list of images to replace"""
    output = "# Images Requiring Replacement\n\n"
    output += "## Critical Priority (Under 5KB)\n\n"
    
    for img in sorted(critical, key=lambda x: x['size_kb']):
        output += f"- [ ] `{img['path']}` ({img['size_kb']:.1f} KB)\n"
    
    output += "\n## High Priority (5KB - 25KB)\n\n"
    
    for img in sorted(low_quality, key=lambda x: x['size_kb']):
        output += f"- [ ] `{img['path']}` ({img['size_kb']:.1f} KB)\n"
    
    output += "\n---\n\n"
    output += "**Instructions**: Check off items as they are replaced\n"
    
    return output

def main():
    """Main function"""
    # Determine base path (repository root)
    script_dir = Path(__file__).parent.absolute()
    base_path = script_dir
    
    print("Scanning for low-quality images...")
    print(f"Base path: {base_path}")
    print()
    
    # Scan images
    critical, low_quality, acceptable = scan_images(base_path)
    
    # Print report
    print_report(critical, low_quality, acceptable)
    
    # Generate markdown checklist
    if len(sys.argv) > 1 and sys.argv[1] == "--generate-checklist":
        checklist = generate_markdown_list(critical, low_quality)
        checklist_file = base_path / "IMAGES_TO_REPLACE_CHECKLIST.md"
        with open(checklist_file, 'w', encoding='utf-8') as f:
            f.write(checklist)
        print(f"[OK] Generated checklist: {checklist_file}")
    
    # Return exit code based on findings
    total_flagged = len(critical) + len(low_quality)
    if total_flagged > 0:
        print(f"[!] Found {total_flagged} images requiring attention")
        return 1
    else:
        print("[OK] All images meet quality standards")
        return 0

if __name__ == "__main__":
    sys.exit(main())
