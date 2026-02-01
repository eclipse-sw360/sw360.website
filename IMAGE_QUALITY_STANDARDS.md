# Image Quality Standards for SW360 Website

## Overview
This document defines the quality standards for all images used in the SW360 website documentation.

## Why Image Quality Matters

### User Experience
- Blurry images make it difficult for users to understand features
- Low-resolution screenshots reduce trust in the documentation
- Unclear UI elements lead to confusion and support requests

### Professional Appearance
- High-quality images reflect the quality of the SW360 project
- Clear documentation helps with adoption and onboarding
- Professional screenshots improve the project's credibility

## Quality Standards

### Minimum Requirements

#### File Size
- **Full-page screenshots**: Minimum 50KB, ideally 100-500KB
- **UI element icons**: Minimum 5KB, ideally 10-20KB
- **Small icons/buttons**: Minimum 2KB, ideally 5-10KB

#### Resolution
- **Full-page screenshots**: 1920x1080 pixels or higher
- **Section screenshots**: Minimum 800x600 pixels
- **UI elements**: Minimum 200x200 pixels

#### Format
- **Primary format**: PNG (lossless compression)
- **Alternative**: JPG only for photos with complex gradients
- **Avoid**: GIF for static images (except animations)

### Image Categories

#### 1. Documentation Screenshots
These show the SW360 application interface and features.

**Requirements:**
- Resolution: 1920x1080 or higher
- File size: 100KB - 500KB
- Format: PNG
- Must show entire browser window or relevant section
- Text must be readable at 100% zoom

**Examples:**
- Login pages
- Dashboard views
- Component detail pages
- Project administration screens

#### 2. UI Icons and Elements
These show buttons, icons, and small interface elements.

**Requirements:**
- Resolution: Minimum 100x100 pixels
- File size: 10KB - 50KB
- Format: PNG
- Must be sharp and well-defined
- Should show the element clearly without surrounding clutter

**Examples:**
- Action buttons (Edit, Delete, Copy)
- Status icons
- Navigation elements

#### 3. Workflow Diagrams
These illustrate processes and workflows.

**Requirements:**
- Resolution: Minimum 1200x800 pixels
- File size: 50KB - 200KB
- Format: PNG
- Clear arrows and labels
- Readable text

#### 4. Setup/Configuration Images
These show installation and configuration steps.

**Requirements:**
- Resolution: 1920x1080 or higher
- File size: 50KB - 300KB
- Format: PNG
- Show complete dialog boxes or terminal windows
- Highlight important settings

## Screenshot Guidelines

### Before Taking Screenshots

1. **Environment Setup**
   - Use a clean browser (Chrome or Firefox recommended)
   - Clear cache and cookies
   - Use incognito/private mode
   - Set browser zoom to 100%
   - Maximize browser window (1920x1080 minimum)

2. **Content Preparation**
   - Use realistic but non-sensitive data
   - Ensure good sample data is loaded
   - Remove personal information
   - Use consistent test data across screenshots

3. **Display Settings**
   - Use default browser theme
   - Avoid browser extensions that modify the UI
   - Ensure good contrast and visibility
   - Disable dark mode unless documenting that feature

### Taking Screenshots

#### Full-Page Screenshots
```
Recommended Tools:
- GoFullPage browser extension
- Built-in developer tools
- Puppeteer/Playwright for automation

Steps:
1. Navigate to the page/feature
2. Ensure all data is loaded
3. Wait for any animations to complete
4. Capture full page or relevant section
5. Review for clarity and completeness
```

#### Specific UI Elements
```
Recommended Tools:
- Browser developer tools (element inspector)
- Snipping Tool / Snip & Sketch (Windows)
- Screenshot utility (Mac)

Steps:
1. Use developer tools to isolate the element
2. Ensure element is fully visible
3. Include some context (surrounding UI)
4. Capture at high resolution
```

### After Taking Screenshots

1. **Review**
   - Check text readability
   - Verify image clarity
   - Ensure no sensitive data is exposed
   - Confirm all important elements are visible

2. **Optimization**
   - Save as PNG with minimal compression
   - Avoid over-compression
   - Keep original dimensions
   - Don't upscale small images

3. **Naming**
   - Use descriptive, lowercase names
   - Use underscores for spaces
   - Include version numbers if relevant
   - Examples:
     - ✅ `component_detail_page.png`
     - ✅ `login_screen_v2.png`
     - ❌ `image1.png`
     - ❌ `screenshot.png`

## Common Issues and Solutions

### Issue: Images Are Too Small
**Cause**: Browser zoom was not at 100%, or window was not maximized
**Solution**: Retake screenshot at 100% zoom with maximized window

### Issue: Text Is Blurry
**Cause**: Image compression too high or resolution too low
**Solution**: Save as PNG with no compression, ensure minimum 1920x1080 resolution

### Issue: Image Shows Sensitive Data
**Cause**: Used production data or personal information
**Solution**: Use test/demo data, blur or remove sensitive information

### Issue: UI Elements Are Cut Off
**Cause**: Screenshot captured only part of the element
**Solution**: Include more context around the element

### Issue: Inconsistent Sizes
**Cause**: Screenshots taken at different resolutions/zoom levels
**Solution**: Standardize on 1920x1080 resolution at 100% zoom

## Tools and Resources

### Screenshot Tools

#### Browser Extensions
- **GoFullPage** (Chrome/Firefox/Edge)
  - Captures entire web pages
  - Saves as PNG or PDF
  - Free and easy to use

- **FireShot** (Chrome/Firefox)
  - Advanced editing features
  - Multiple capture modes
  - Annotation tools

- **Awesome Screenshot** (Chrome/Firefox)
  - Screen recording capability
  - Built-in annotation
  - Cloud storage option

#### Desktop Applications
- **ShareX** (Windows)
  - Open source
  - Advanced capture options
  - Built-in editor

- **Snagit** (Windows/Mac)
  - Professional tool
  - Advanced editing
  - Video capture

- **Skitch** (Mac)
  - Simple and effective
  - Good annotation tools
  - Free

#### Command Line
- **Puppeteer** (Node.js)
  ```javascript
  const puppeteer = require('puppeteer');
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto('http://localhost:8080');
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
  ```

- **Playwright** (Node.js/Python)
  ```python
  from playwright.sync_api import sync_playwright
  with sync_playwright() as p:
      browser = p.chromium.launch()
      page = browser.new_page(viewport={'width': 1920, 'height': 1080})
      page.goto('http://localhost:8080')
      page.screenshot(path='screenshot.png')
      browser.close()
  ```

### Image Editing Tools

#### Free Options
- **GIMP** - Full-featured image editor
- **Paint.NET** - Simple Windows editor
- **Photopea** - Browser-based Photoshop alternative

#### Online Tools
- **TinyPNG** - Smart PNG compression
- **Squoosh** - Google's image compression tool
- **Remove.bg** - Remove backgrounds (if needed)

## Review Checklist

Before submitting new images:

- [ ] Image is at least 1920x1080 for full pages
- [ ] File size is at least 50KB for screenshots
- [ ] Format is PNG (unless JPG is necessary)
- [ ] Text is readable at 100% zoom
- [ ] No sensitive data is visible
- [ ] Image is not over-compressed
- [ ] Filename is descriptive
- [ ] Image matches current UI version

## Automation

### Pre-commit Hook
Consider adding a pre-commit hook to check image quality:

```bash
#!/bin/bash
# .git/hooks/pre-commit
python check_image_quality.py
if [ $? -ne 0 ]; then
    echo "❌ Low-quality images detected. Please fix before committing."
    exit 1
fi
```

### CI/CD Integration
Add image quality checks to your CI pipeline:

```yaml
# .github/workflows/image-quality.yml
name: Image Quality Check
on: [pull_request]
jobs:
  check-images:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Check image quality
        run: python check_image_quality.py
```

## Contribution Guidelines

When contributing new images:

1. Follow the quality standards above
2. Run `python check_image_quality.py` before submitting
3. Include the image in your PR description
4. Test the image displays correctly in the documentation
5. Update relevant documentation files if needed

## Questions?

If you have questions about image quality or need help:
- Check the [BLURRY_IMAGES_GUIDE.md](BLURRY_IMAGES_GUIDE.md)
- Open an issue in the repository
- Ask in the project communication channels

---

**Last Updated**: 2026-02-01
**Version**: 1.0