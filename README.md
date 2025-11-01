# DanielBryars.github.io

Personal portfolio website hosted on GitHub Pages with a retro BBC Teletext aesthetic.

## Overview

This repository hosts the personal portfolio website of Daniel Bryars, featuring a unique design inspired by classic BBC Teletext graphics. The site includes a CV, about page, and demo projects.

## Design Theme

The website recreates the distinctive look and feel of 1980s BBC Teletext/Ceefax:
- Black background with yellow text
- Pixelated "Pixelify Sans" font
- Block graphics and simple layouts
- Retro computing aesthetic

## Pages

- **index.html**: Main landing page with navigation
- **cv.html**: Professional CV and experience
- **about.html**: Personal information and background
- **bbcb-demo.html**: BBC-related demo content

## Technical Details

- **Static Site**: Pure HTML/CSS, no build process
- **GitHub Pages**: Hosted via `danielbryars.com` custom domain (CNAME)
- **Build Info**: Automated build timestamp tracking with `update-build-info.sh`
- **Responsive**: Mobile-friendly responsive design

## Assets

- **Audio Files**: BBC Shipping Forecast recordings (μ-law encoded WAV)
- **Custom Fonts**: Google Fonts integration for retro typography
- **Stylesheets**:
  - `styles.css`: Main stylesheet
  - `fonts.css`: Font definitions

## Build System

The site includes a simple build information system:
- `update-build-info.sh`: Shell script to generate build metadata
- `build-info.json`: Contains build timestamp and version info

## Custom Domain

The site is accessible via a custom domain configured through:
```
CNAME → danielbryars.com
```

## Development

To modify the site:

1. Clone the repository
2. Edit HTML/CSS files directly
3. Test locally by opening HTML files in a browser
4. Push changes to `main` branch
5. GitHub Pages automatically deploys updates

## Special Features

### Teletext-Style Graphics
The design uses CSS to recreate the blocky, low-resolution aesthetic of Teletext, including:
- Monospace typography
- Limited color palette
- Character-based layouts
- Retro navigation elements

### Agents Documentation
- `AGENTS.md`: Documentation for AI agents or automated systems

## Browser Compatibility

Works in all modern browsers supporting:
- CSS Grid
- Flexbox
- Google Fonts
- HTML5 audio (for wav files)

## Inspiration

The design pays homage to:
- BBC Teletext / Ceefax
- Retro computing interfaces
- 1980s information services
- British broadcasting history

## Local Development

```bash
# Clone the repository
git clone https://github.com/DanielBryars/DanielBryars.github.io.git

# Open in browser
open index.html
```

## Deployment

Automatically deployed via GitHub Pages when pushing to the main branch. No build step required.

## License

Personal portfolio website - content and design © Daniel Bryars
