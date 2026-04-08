# Contributing Images to SW360 Website

Thank you for helping improve the SW360 website documentation! This guide will walk you through replacing blurry screenshots with high-quality ones.

## Quick Start (5 Minutes)

### Prerequisites
- A computer with internet access
- A GitHub account (free to create)
- SW360 access (local installation or demo instance)
- 30-60 minutes per image batch

### Your First Image Replacement

#### Step 1: Pick an Image
1. Open `IMAGES_TO_REPLACE_CHECKLIST.md`
2. Look for unchecked items (marked with `[ ]`)
3. Start with **Critical Priority** images (under 5KB)
4. Pick one image to replace

#### Step 2: Understand What You're Replacing
Look at the filename to understand what feature it shows:
- `SignIn.png` → Login page screenshot
- `ProjectAdministration.png` → Project admin UI
- `ClearingRequest.png` → Clearing request feature
- `Componentpage/Create_Release1.png` → Component release creation

#### Step 3: Access SW360
**Option A: Local Installation**
```bash
# If you have SW360 installed locally
cd /path/to/sw360
./start.sh  # or however you start SW360
```

**Option B: Demo Instance**
- Ask the maintainers for demo access
- Or use screenshots from the current website (if quality is good)

**Option C: Current Website**
- Go to https://www.eclipse.org/sw360/
- Take screenshots from there if they're clearer

#### Step 4: Take a New Screenshot

**Browser Setup**:
1. Open Chrome or Firefox
2. Press F11 for full-screen mode
3. Set zoom to 100% (Ctrl+0 or Cmd+0)
4. Navigate to the feature in SW360

**Taking the Screenshot**:

**Method 1: Browser Extension (Recommended)**
1. Install "GoFullPage" extension
2. Navigate to the page
3. Click the extension icon
4. Download as PNG

**Method 2: Built-in Tools**
- **Windows**: Win + Shift + S, select area
- **Mac**: Cmd + Shift + 4, select area
- **Linux**: Depends on your desktop environment

**Quality Check**:
- Can you read all the text clearly?
- Is the image at least 1920 pixels wide?
- Does it show the full page or relevant section?
- File size should be 50KB-300KB

#### Step 5: Save with Correct Name
1. Rename your screenshot to match the old filename exactly
2. Example: If replacing `SignIn.png`, name your file `SignIn.png`
3. Save as PNG format (not JPG or GIF)

#### Step 6: Replace the Old Image

**Using File Explorer/Finder**:
1. Navigate to the image location in the repository
2. Delete or rename the old blurry image
3. Copy your new image there
4. Make sure the filename is identical

**Example**:
```
Old: sw360.website/static/img/ImagesBasic/SignIn.png (9.1KB, blurry)
New: sw360.website/static/img/ImagesBasic/SignIn.png (150KB, clear)
```

#### Step 7: Test Your Change

**View the Image**:
1. Open the new image in an image viewer
2. Verify it's clear and readable
3. Check the file size is > 25KB

**Optional - Test Website Locally**:
```bash
# Install Hugo if you haven't
# https://gohugo.io/installation/

# Run the website locally
cd sw360.website
hugo server

# Open http://localhost:1313 in browser
# Navigate to where the image is used
# Verify it displays correctly
```

#### Step 8: Submit Your Work

**Using Git Command Line**:
```bash
# Navigate to the repository
cd sw360.website

# Create a new branch
git checkout -b fix-blurry-signin-image

# Add your changes
git add static/img/ImagesBasic/SignIn.png

# Commit with a descriptive message
git commit -m "fix: Replace blurry SignIn.png with high-quality version

- Replaced 9.1KB blurry image with 150KB clear version
- New image shows login page at 1920x1080 resolution
- Text is now readable and UI elements are clear

Fixes part of #174"

# Push to GitHub
git push origin fix-blurry-signin-image

# Then go to GitHub and create a Pull Request
```

**Using GitHub Desktop (Easier for Beginners)**:
1. Open GitHub Desktop
2. Select the sw360.website repository
3. Click "Current Branch" → "New Branch"
4. Name it: `fix-blurry-[image-name]`
5. Make your changes (replace the image)
6. GitHub Desktop will show the changed file
7. Write a summary: "Replace blurry SignIn.png"
8. Write description explaining the change
9. Click "Commit to [branch name]"
10. Click "Publish Branch"
11. Click "Create Pull Request"

#### Step 9: Update the Checklist
1. Open `IMAGES_TO_REPLACE_CHECKLIST.md`
2. Find the image you replaced
3. Change `[ ]` to `[x]`
4. Save the file
5. Commit this change too

#### Step 10: Wait for Review
- Maintainers will review your PR
- They may ask for changes
- Once approved, they'll merge it
- Your contribution is now live! 🎉

## Tips for Success

### Choosing Which Images to Replace

**Start Here (Easiest)**:
- UI icons in `ImagesBasic/` folder
- Simple buttons and elements
- Login/Sign-in pages

**Then Move To**:
- Component pages
- Project pages
- License pages

**Save for Last**:
- Complex workflows
- Multi-step processes
- Images requiring specific data setup

### Common Mistakes to Avoid

❌ **Wrong**:
- Taking screenshots at weird zoom levels (80%, 120%)
- Saving as JPG (loses quality)
- Using very old SW360 versions
- Including personal/sensitive data
- Forgetting to maximize browser window

✅ **Right**:
- Always 100% zoom
- Save as PNG
- Use current SW360 version
- Use test/demo data only
- Full browser window (1920x1080)

### Batch Replacements (More Efficient)

Instead of one image at a time, do related images together:

**Example Batch**: Project Page Images
1. `ProjectAdministration.png`
2. `ProjectLinkedreleasesandprojects.png`
3. `EditProject_Attachments.png`
4. `LicenseClearing_1.png`

**Steps**:
1. Navigate to Project section in SW360
2. Take all 4 screenshots in one session
3. Replace all 4 images
4. Submit one PR with all changes

### Time Estimates

- **Simple icon/button**: 5-10 minutes
- **Single page screenshot**: 15-20 minutes
- **Complex workflow**: 30-45 minutes
- **Batch of 5 related images**: 1-2 hours

## Understanding the File Structure

```
sw360.website/
└── static/
    └── img/
        ├── ImagesBasic/              # Main documentation
        │   ├── LicensePage/          # License features
        │   ├── Componentpage/        # Component features
        │   ├── Project_Page/         # Project features
        │   ├── PackagesPage/         # Package features
        │   └── VulnerabiblitiesPage/ # Vulnerability features
        ├── sw360screenshots/         # General screenshots
        ├── workflow/                 # Workflow diagrams
        └── couchdb/                  # Database setup
```

## Quality Standards Reference

### Minimum Requirements
- **Format**: PNG only
- **Resolution**: 1920x1080 (Full HD) minimum
- **File size**: 50KB-500KB for screenshots
- **Text**: Must be readable at 100% zoom

### Quick Quality Check
Before submitting, verify:
- [ ] File size > 25KB (check in file properties)
- [ ] Can read text without zooming
- [ ] Image is clear, not pixelated
- [ ] Shows correct SW360 feature
- [ ] No sensitive/personal data visible

## Getting Help

### Stuck on Something?
1. Check `IMAGE_QUALITY_STANDARDS.md` for detailed guidelines
2. Look at `BLURRY_IMAGES_GUIDE.md` for examples
3. Ask in the project's communication channels
4. Comment on Issue #174 with your question

### Can't Install SW360?
- Ask maintainers for demo access
- Try the public website for simple screenshots
- Focus on UI icons that don't need SW360 running

### Not Sure About Quality?
- Run: `python check_image_quality.py`
- It will tell you if your image meets standards
- Ask for feedback in your Pull Request

## Example Pull Request

**Title**: `fix: Replace blurry SignIn and navigation images`

**Description**:
```markdown
## Summary
Replaced 3 blurry screenshots in the ImagesBasic folder with high-quality versions.

## Images Replaced
1. **SignIn.png** (9.1KB → 145KB)
   - Was: Blurry login page, unreadable text
   - Now: Clear 1920x1080 screenshot, all text readable

2. **navigationbar-search.png** (10.3KB → 120KB)
   - Was: Pixelated search UI
   - Now: Clear search interface showing all elements

3. **ProjectAdministration.png** (11.3KB → 180KB)
   - Was: Compressed admin panel, hard to read
   - Now: Sharp admin interface with clear labels

## Testing
- [x] Verified all images display correctly in documentation
- [x] Checked file sizes meet minimum requirements (>25KB)
- [x] Confirmed text is readable at 100% zoom
- [x] Updated IMAGES_TO_REPLACE_CHECKLIST.md

## Related Issue
Part of #174 - Replace blurry screenshots with clear images
```

## Recognition

Your contribution will be:
- ✅ Listed in the project's commit history
- ✅ Shown in your GitHub profile
- ✅ Credited in release notes
- ✅ Helping thousands of SW360 users!

## Next Steps

1. Read through this guide completely
2. Open `IMAGES_TO_REPLACE_CHECKLIST.md`
3. Pick your first image
4. Follow the steps above
5. Submit your first PR
6. Celebrate! 🎉

**Remember**: Every image you replace makes the documentation better. Even replacing just one image is a valuable contribution!

---

**Questions?** Comment on Issue #174 or ask the community.

**Ready to start?** Pick an image from the checklist and go for it!

Happy contributing! 🚀