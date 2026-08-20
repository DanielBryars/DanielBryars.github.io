(function () {
    const figures = Array.from(document.querySelectorAll('main figure'));
    const imageFigures = figures.filter((figure) => figure.querySelector('img'));

    if (!imageFigures.length || !('HTMLDialogElement' in window)) {
        return;
    }

    const dialog = document.createElement('dialog');
    dialog.className = 'image-lightbox';
    dialog.setAttribute('aria-label', 'Image preview');
    dialog.innerHTML = `
        <div class="image-lightbox-inner">
            <div class="image-lightbox-bar">
                <button class="image-lightbox-close" type="button">Close</button>
            </div>
            <img alt="">
            <p class="image-lightbox-caption"></p>
        </div>
    `;
    document.body.appendChild(dialog);

    const lightboxImage = dialog.querySelector('img');
    const caption = dialog.querySelector('.image-lightbox-caption');
    const closeButton = dialog.querySelector('.image-lightbox-close');

    const largestSrc = (image) => {
        // A gallery can point at a bigger file than anything in its srcset:
        // the party photographs keep a 2400px version that the grid never
        // loads, so the lightbox shows the frame properly.
        const full = image.getAttribute('data-full');
        if (full) {
            return full;
        }

        const srcset = image.getAttribute('srcset');
        if (!srcset) {
            return image.currentSrc || image.src;
        }

        const candidates = srcset.split(',')
            .map((entry) => entry.trim().split(/\s+/))
            .map(([src, width]) => ({
                src,
                width: Number((width || '').replace('w', '')) || 0
            }))
            .sort((a, b) => b.width - a.width);

        return candidates[0]?.src || image.currentSrc || image.src;
    };

    const openImage = (figure) => {
        const image = figure.querySelector('img');
        const figureCaption = figure.querySelector('figcaption')?.textContent.trim() || '';
        lightboxImage.src = largestSrc(image);
        lightboxImage.alt = image.alt || figureCaption || 'Expanded project image';
        caption.textContent = figureCaption || image.alt || '';
        dialog.showModal();
        closeButton.focus();
    };

    imageFigures.forEach((figure) => {
        const image = figure.querySelector('img');
        const label = figure.querySelector('figcaption')?.textContent.trim() || image.alt || 'project image';
        image.tabIndex = 0;
        image.setAttribute('role', 'button');
        image.setAttribute('aria-label', `Open larger image: ${label}`);

        image.addEventListener('click', () => openImage(figure));
        image.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                openImage(figure);
            }
        });
    });

    closeButton.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
        if (event.target === dialog) {
            dialog.close();
        }
    });
})();
