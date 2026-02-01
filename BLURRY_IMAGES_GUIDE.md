# Blurry Screenshots Replacement Guide

## Issue Summary
This repository contains numerous blurry and low-quality screenshots that need to be replaced with high-quality, clear images.

## Identified Blurry Images

### Critical Priority (Under 5KB - Extremely Blurry)
These images are too small and compressed to be useful:

**ImagesBasic folder:**
- `Delete_Trash.png` (2.2K) - UI icon
- `ClearingRequest.png` (2.3K) - UI icon
- `Copy_Duplicate.png` (2.3K) - UI icon
- `Edit_Pen.png` (2.4K) - UI icon
- `SortIcon.png` (2.7K) - UI icon
- `Export-Spreadsheet.png` (4.9K) - UI element

**ImagesBasic/LicensePage folder:**
- `Unchecked.png` (847 bytes) - Checkbox icon
- `Checked.png` (1.1K) - Checkbox icon

**ImagesBasic/Componentpage folder:**
- `Split_Icon_1.png` (2.0K) - UI icon
- `Changelog2.png` (2.1K) - UI element
- `Merge_Icon_1.png` (2.1K) - UI icon
- `Changelog1.png` (2.2K) - UI element
- `Merge_Icon_2.png` (2.3K) - UI icon
- `Merge_Icon_3.png` (2.3K) - UI icon
- `Editcomponent.png` (2.9K) - UI element
- `Componentreleases.png` (4.6K) - UI element

**ImagesBasic/PackagesPage folder:**
- `action.png` (2.4K) - UI element

### High Priority (5KB - 25KB - Likely Blurry)
These documentation screenshots are likely too compressed:

**ImagesBasic folder:**
- `SignIn.png` (9.1K) - Login screen
- `navigationbar-search.png` (11K) - Search UI
- `ProjectAdministration.png` (12K) - Admin UI
- `LicenseClearing_1.png` (13K) - License UI
- `ProjectLinkedreleasesandprojects.png` (13K) - Project UI
- `EditProject_Attachments.png` (16K) - Attachments UI
- `admin_menu.png` (20K) - Menu UI
- `Deleteproject1.png` (21K) - Delete UI
- `Project_external_ID_1.png` (22K) - External ID UI
- `Linked-projects_2.png` (23K) - Linked projects UI
- `ProjectExternalURL1.png` (24K) - External URL UI

**ImagesBasic/Componentpage folder:**
- `ComponentSPDXattachment.png` (13K) - SPDX attachment UI
- `Component_SPDX_Attachments_1.png` (14K) - SPDX attachment UI
- `ComponentExternalIds.png` (15K) - External IDs UI
- `ComponentAdditionalroles.png` (16K) - Roles UI
- `Componentadditionaldata.png` (16K) - Additional data UI
- `Component_SPDX_Attachments_2.png` (21K) - SPDX attachment UI
- `Assesment_Summary_Info.png` (25K) - Assessment UI
- `Component_Assesment_summary_info1.png` (25K) - Assessment UI

**ImagesBasic/LicensePage folder:**
- `Linked_Obligations.png` (16K) - Obligations UI

**ImagesBasic/Project_Page folder:**
Multiple duplicates of the above images exist in this folder as well.

### Medium Priority (26KB - 65KB - May Need Review)
- `Addproject4.png` (26K)
- `general-search.png` (26K)
- `ImportSBOM.png` (27K)
- `Loginpage.png` (28K)
- `workflow-add-project.png` (36K)
- `workflow-clearing.png` (42K)
- `workflow-moderation.png` (46K)
- `sw360screenshot-preferences02.png` (38K)
- `ReIndexSearch.png` (15K)

## Screenshot Quality Guidelines

### Recommended Specifications:
1. **Resolution**: Minimum 1920x1080 (Full HD)
2. **Format**: PNG (lossless compression)
3. **File Size**: At least 50KB-200KB for full-page screenshots
4. **Clarity**: Text should be readable at 100% zoom
5. **Compression**: Use minimal compression to preserve quality

### Screenshot Best Practices:
1. Use browser zoom at 100% (not zoomed in or out)
2. Capture full pages or relevant sections
3. Ensure good lighting and contrast
4. Remove personal/sensitive data before capturing
5. Use consistent browser (recommend Chrome or Firefox)
6. Clear browser cache and use incognito mode for clean UI

## How to Replace Images

### For Contributors:
1. Set up SW360 locally or access a demo instance
2. Navigate to the feature shown in the blurry image
3. Take a new screenshot following the guidelines above
4. Save as PNG with descriptive filename
5. Replace the old file in the appropriate directory
6. Test the website locally to ensure the new image displays correctly
7. Submit a pull request with clear description

### For Maintainers:
1. Review the list above
2. Prioritize critical and high-priority images
3. Create issues for batches of related images (e.g., "Replace Component Page Images")
4. Consider automating screenshot capture if possible
5. Update documentation to include screenshot requirements

## Tools for Taking Screenshots

### Browser Extensions:
- **GoFullPage** (Chrome/Firefox) - Captures full page screenshots
- **Fireshot** - Advanced screenshot tool with editing
- **Awesome Screenshot** - Easy-to-use with annotation features

### Built-in Tools:
- **Windows**: Win + Shift + S (Snipping Tool)
- **Mac**: Cmd + Shift + 4/5
- **Linux**: Various tools depending on DE

### Command Line:
- **Puppeteer/Playwright**: Automated screenshot capture for documentation

## Testing Images

After replacement:
1. Build the website locally: `hugo server`
2. Navigate to pages using the images
3. Check image clarity at different screen sizes
4. Verify text readability
5. Ensure consistent styling

## Automation Script

A Python script is provided (`check_image_quality.py`) to identify low-quality images automatically.

Run it with:
```bash
python check_image_quality.py
```

This will scan all images and report those under the quality threshold.

## Related Files

- `check_image_quality.py` - Script to identify blurry images
- `replace_images.md` - Detailed replacement instructions
- `IMAGE_QUALITY_STANDARDS.md` - Quality standards documentation

## Estimated Effort

- **Critical Priority**: ~20 images, 2-4 hours
- **High Priority**: ~25 images, 3-5 hours
- **Medium Priority**: ~15 images, 2-3 hours
- **Total**: ~60 images, 7-12 hours

## Next Steps

1. [ ] Create individual issues for image batches
2. [ ] Set up SW360 demo environment for screenshot capture
3. [ ] Assign contributors to specific sections
4. [ ] Review and merge replacement PRs
5. [ ] Update contribution guidelines with screenshot standards
6. [ ] Close this issue when all images are replaced

---

**Note**: This is an ongoing effort. Contributors are welcome to replace images in any order, focusing on the critical and high-priority ones first.