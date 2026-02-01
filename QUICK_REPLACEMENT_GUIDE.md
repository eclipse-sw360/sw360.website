# Quick Replacement Guide for Issue #174

## ⚠️ IMMEDIATE ACTION NEEDED

The blurry images have been **analyzed and documented**. Since I don't have access to a running SW360 instance, I cannot take the actual screenshots. However, I've created everything needed for someone WITH access to complete this quickly.

## 📊 What I Found

- **52 blurry images** identified (22 critical, 30 high priority)
- **Multiple corrupted images** (like SignIn.png showing code instead of screenshot)
- **Documentation heavily affected** - these images are used throughout user guides

## 🎯 Most Critical Replacements (Do These First!)

### UI Icons (Under 5KB) - 15 minutes each
1. **Delete_Trash.png** - Used 10+ times across docs
2. **Edit_Pen.png** - Used 5+ times across docs  
3. **SortIcon.png** - Used 5+ times across docs
4. **Copy_Duplicate.png** - Used in Projects
5. **ClearingRequest.png** - Used 3 times

### Screenshots (5-25KB) - 30 minutes each
1. **SignIn.png** - CORRUPTED! Shows code instead of screenshot
2. **ProjectAdministration.png** - Used in Project guide
3. **LicenseClearing_1.png** - Used in Project guide
4. **navigationbar-search.png** - Used in search docs

## 📚 Documentation Created

### For Someone WITH SW360 Access:

1. **SCREENSHOT_REQUIREMENTS.md** ⭐ START HERE
   - Detailed instructions for each image
   - Exact steps to navigate to each feature
   - Expected file sizes and dimensions
   - **Time estimate**: 4-5 hours total

2. **IMAGES_TO_REPLACE_CHECKLIST.md**
   - 52 checkboxes to track progress
   - File sizes and locations
   - **Use this** to track what's done

3. **BLURRY_IMAGES_GUIDE.md**
   - Complete technical guide
   - Screenshot tools and techniques
   - Quality standards

4. **check_image_quality.py**
   - Run this to verify new images
   - Checks file sizes automatically
   - **Run after** replacing images

## 🚀 How to Complete This (For SW360 User)

### Step 1: Setup (5 minutes)
```bash
# Clone repo if not already done
git clone https://github.com/eclipse-sw360/sw360.website.git
cd sw360.website

# Install screenshot tool
# Option A: Chrome extension "GoFullPage"
# Option B: Firefox extension "FireShot"
# Option C: Built-in tools
```

### Step 2: Open SW360 (2 minutes)
```
1. Login to your SW360 instance
2. Maximize browser (1920x1080)
3. Set zoom to 100%
```

### Step 3: Capture Icons (15 minutes)
```
Navigate to: Components page
Capture these icons from action column:
- Delete_Trash.png → Trash/delete icon
- Edit_Pen.png → Edit/pencil icon  
- SortIcon.png → Sort icon from table headers
- Copy_Duplicate.png → Copy icon

Settings:
- Size: 48x48 pixels
- Format: PNG
- Save to: static/img/ImagesBasic/
```

### Step 4: Capture Screenshots (3-4 hours)
Follow **SCREENSHOT_REQUIREMENTS.md** for detailed steps.

Quick batch approach:
1. **Component Screenshots** (1 hour)
   - Open one component
   - Capture all sections mentioned in checklist
   
2. **Project Screenshots** (1 hour)
   - Open one project
   - Capture all tabs and sections
   
3. **Other Screenshots** (1-2 hours)
   - Login page
   - License pages
   - Admin pages
   - etc.

### Step 5: Verify (5 minutes)
```bash
python check_image_quality.py
# Should show 0 critical/low quality images
```

### Step 6: Submit PR (10 minutes)
```bash
git checkout -b fix-blurry-images-batch-1
git add static/img/ImagesBasic/*.png
git commit -m "fix: Replace blurry screenshots (Batch 1)

Replaced 10 critical low-quality images:
- Delete_Trash.png (2.2KB → 15KB)
- Edit_Pen.png (2.4KB → 12KB)
- SignIn.png (9.1KB → 145KB) - Fixed corrupted image
- ProjectAdministration.png (12KB → 180KB)
- [list others...]

All images now meet quality standards (>25KB, readable text)

Fixes part of #174"

git push origin fix-blurry-images-batch-1
# Create PR on GitHub
```

## 🎓 Tips for Best Results

### Browser Setup:
- **Resolution**: 1920x1080 minimum
- **Zoom**: 100% (Ctrl+0)
- **Mode**: Normal (not incognito, avoid extensions)

### Screenshot Tool:
- **GoFullPage** extension recommended
- Capture **full page** for page screenshots
- Capture **element only** for icons

### Quality Check:
Before saving each image:
- [ ] Text is readable at 100% zoom?
- [ ] No sensitive data visible?
- [ ] Shows correct SW360 feature?
- [ ] File size > 25KB (for screenshots)?

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Setup & reading docs | 15 min |
| UI Icons (5 images) | 30 min |
| Component screenshots (10) | 1.5 hours |
| Project screenshots (15) | 2 hours |
| Other screenshots (22) | 2 hours |
| Verification & PR | 30 min |
| **TOTAL** | **~6-7 hours** |

## 🔄 Batch Strategy

**Don't do all 52 at once!** Break into batches:

**Batch 1**: UI Icons (22 images, ~1 hour) ⭐ START HERE
**Batch 2**: Component pages (10 images, ~1.5 hours)  
**Batch 3**: Project pages (15 images, ~2 hours)
**Batch 4**: Remaining (5 images, ~1 hour)

Submit separate PRs for each batch - easier to review!

## ❓ Common Questions

**Q: What if I don't have SW360 access?**  
A: Ask maintainers for demo credentials or access to test instance.

**Q: Can I use the public sw360.org screenshots?**  
A: Yes, if they're clearer than current ones. Check quality first.

**Q: What format should I use?**  
A: PNG only. No JPG or GIF for screenshots.

**Q: What if an image is referenced but not in the checklist?**  
A: Check `check_image_quality.py` output - it scans all images.

**Q: How do I check if my screenshots are good enough?**  
A: Run `python check_image_quality.py` - it will tell you!

## 📞 Need Help?

- Check **SCREENSHOT_REQUIREMENTS.md** for detailed steps
- Comment on **GitHub Issue #174** with questions
- Join the project communication channels

---

## ✅ Current Status

- ✅ **Issue verified**: 52 blurry images found
- ✅ **Documentation created**: 5 comprehensive guides
- ✅ **Backup made**: Original images saved
- ✅ **Requirements documented**: Every image specified
- ⏳ **Pending**: Actual screenshots from SW360 instance

**Ready for someone with SW360 access to complete!**

---

**Last Updated**: 2026-02-01  
**Issue**: #174  
**Status**: Documented & Ready for Implementation  
**Effort Required**: 6-7 hours (can be split into 4 batches)