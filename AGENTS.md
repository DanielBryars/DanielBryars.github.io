# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Project Overview

This is a static GitHub Pages portfolio website for Daniel Bryars (danielbryars.github.io). The site showcases personal projects, CV, and contact information with a retro-terminal aesthetic using the VT323 monospace font.

## Site Structure

### Core Pages
- **index.html** - Landing page with rotating background images (Sparks1-6.jpg), navigation menu, social badges, and build info
- **about.html** - About page
- **cv.html** - CV formatted as syntax-highlighted Python code in a terminal-style dark theme
- **cool-projects/index.html** - Project gallery using flip cards (front/back) with "i" info buttons

### Project Pages
Individual project HTML files in `cool-projects/` directory:
- MegaBookCase.html, RobotArm.html, SpiralStairCase.html, VintageStringLights.html
- OtterSurfboard.html, ShadowPrinting.html, SpeedBoat.html, DriftTrike.html
- HiscotsLights.html, MGEVProject.html, BenEater8BitComputer.html, ClockProject.html
- CurvingSkirtingBoard.html, CVInABox.html, 3DPrinters.html

## Styling Architecture

### CSS Organization
- **fonts.css** - Custom font definitions
- **styles.css** - Global styles including:
  - Background layers with fade transitions
  - Menu navigation positioning and hover effects
  - CV terminal theme (syntax highlighting: comments, keywords, strings, functions, class names)
  - Social badges positioning (fixed bottom-right)
  - Build info display (fixed bottom-right)
  - CV box container with 3D perspective transforms
  - Responsive mobile styles
- **cool-projects/styles.css** - Project-specific styles:
  - CSS grid layout for project tiles (auto-fit, minmax 300px)
  - 3D flip card mechanics (perspective: 1000px, rotateY transform)
  - Info button styling with green matrix-style glow effects
  - Terminal/cyberpunk aesthetic (dark backgrounds, green accents)

### Visual Theme
- Retro terminal aesthetic with VT323 monospace font
- Dark backgrounds with rgba overlays for transparency
- Matrix-style green (#00ff00) accent colors with glow effects
- 3D transforms and perspective effects for interactive elements
- Background image rotation system on landing page (30-second intervals)

## Build System

### Build Info Generation
Run `./update-build-info.sh` to update build metadata:
- Generates `build-info.json` with current git commit hash and timestamp
- Displayed on landing page as small badge (bottom-right corner)
- Format: "Build: [7-char hash] | [date]"

### Asset Locations
- Images: `images/` directory (includes Sparks1-6.jpg for rotating backgrounds)
- Fonts: `fonts/` directory
- Videos: `video/` directory
- Audio: Root directory (ShippingForecast WAV files)
- Ontology data: `ontology/` directory

## Key Interactive Features

### Landing Page (index.html)
- Two-layer background system for crossfading images (bgLayer1, bgLayer2)
- Image rotation every 30 seconds (BACKGROUND_ROTATION_INTERVAL_MS)
- Images cycle through Sparks1.jpg to Sparks6.jpg
- Social badges fixed to bottom-right (Stack Overflow, LinkedIn, GitHub, Email)
- Build info loaded via fetch and displayed dynamically

### Project Gallery (cool-projects/index.html)
- Grid of flip cards using 3D CSS transforms
- "i" button in top-right corner triggers card flip (180deg rotateY)
- Front shows project title with link, back shows description
- JavaScript adds click listeners to all `.info-button` elements
- Clicking info button toggles `.flipped` class on `.card-inner`

### CV Page (cv.html)
- CV formatted as Python code with VS Code dark theme syntax highlighting
- Color classes: .comment, .keyword, .string, .function, .class-name, .self
- Terminal-style container (#1e1e1e background)

## Development Commands

Since this is a static site with no build process:
- **Local development**: Open HTML files directly in browser or use a local server (e.g., `python -m http.server`)
- **Update build info**: `./update-build-info.sh` (generates build-info.json)
- **Deploy**: Push to master branch (GitHub Pages auto-deploys)

## Git Workflow

- **Main branch**: master
- **Deployment**: Automatic via GitHub Pages on push to master
- **CNAME file**: Points to bryars.com domain

## Important Conventions

- All project pages should maintain consistent structure with global styles
- Social badges use shields.io badges for consistency
- Background images must be named Sparks[1-6].jpg and placed in images/ directory
- Project cards require both card-front and card-back divs with info-button
- Terminal aesthetic should use VT323 font and maintain green/dark color scheme
