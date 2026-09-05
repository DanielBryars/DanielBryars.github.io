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
                <span class="image-lightbox-count" aria-live="polite"></span>
                <button class="image-lightbox-close" type="button">Close</button>
            </div>
            <div class="image-lightbox-stage">
                <button class="image-lightbox-nav image-lightbox-prev" type="button" aria-label="Previous photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5 8 12l7 7"/></svg></button>
                <img alt="">
                <button class="image-lightbox-nav image-lightbox-next" type="button" aria-label="Next photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg></button>
            </div>
            <p class="image-lightbox-caption"></p>
        </div>
    `;
    document.body.appendChild(dialog);

    const lightboxImage = dialog.querySelector('img');
    const stage = dialog.querySelector('.image-lightbox-stage');
    const caption = dialog.querySelector('.image-lightbox-caption');
    const count = dialog.querySelector('.image-lightbox-count');
    const closeButton = dialog.querySelector('.image-lightbox-close');
    const prevButton = dialog.querySelector('.image-lightbox-prev');
    const nextButton = dialog.querySelector('.image-lightbox-next');

    const total = imageFigures.length;
    let current = 0;

    if (total < 2) {
        // A single image has nowhere to go: hide the arrows and the counter.
        dialog.classList.add('image-lightbox-single');
        prevButton.hidden = true;
        nextButton.hidden = true;
        count.hidden = true;
    }

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

    const preloaded = new Set();
    const preload = (index) => {
        const src = largestSrc(imageFigures[index].querySelector('img'));
        if (preloaded.has(src)) {
            return;
        }
        preloaded.add(src);
        const warm = new Image();
        warm.src = src;
    };

    const showIndex = (index) => {
        current = (index + total) % total;
        const figure = imageFigures[current];
        const image = figure.querySelector('img');
        const figureCaption = figure.querySelector('figcaption')?.textContent.trim() || '';
        const src = largestSrc(image);

        lightboxImage.classList.add('is-loading');
        lightboxImage.onload = () => lightboxImage.classList.remove('is-loading');
        lightboxImage.onerror = () => lightboxImage.classList.remove('is-loading');
        lightboxImage.src = src;
        if (lightboxImage.complete) {
            lightboxImage.classList.remove('is-loading');
        }
        lightboxImage.alt = image.alt || figureCaption || 'Expanded project image';
        caption.textContent = figureCaption || image.alt || '';
        count.textContent = `${current + 1} / ${total}`;

        if (total > 1) {
            // Warm the neighbours so the next click is instant.
            preload((current + 1) % total);
            preload((current - 1 + total) % total);
        }
    };

    const openImage = (figure) => {
        showIndex(imageFigures.indexOf(figure));
        dialog.showModal();
        closeButton.focus();
    };

    const step = (delta) => {
        if (total < 2) {
            return;
        }
        showIndex(current + delta);
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

    prevButton.addEventListener('click', () => step(-1));
    nextButton.addEventListener('click', () => step(1));

    dialog.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft') {
            event.preventDefault();
            step(-1);
        } else if (event.key === 'ArrowRight') {
            event.preventDefault();
            step(1);
        }
    });

    // Swipe left or right across the photograph on touch screens.
    let swipeStartX = null;
    let swipeStartY = null;
    stage.addEventListener('pointerdown', (event) => {
        if (event.pointerType === 'mouse') {
            return;
        }
        swipeStartX = event.clientX;
        swipeStartY = event.clientY;
    });
    stage.addEventListener('pointerup', (event) => {
        if (swipeStartX === null) {
            return;
        }
        const dx = event.clientX - swipeStartX;
        const dy = event.clientY - swipeStartY;
        swipeStartX = null;
        swipeStartY = null;
        if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
            step(dx < 0 ? 1 : -1);
        }
    });
    stage.addEventListener('pointercancel', () => {
        swipeStartX = null;
        swipeStartY = null;
    });

    closeButton.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
        if (event.target === dialog) {
            dialog.close();
        }
    });
    dialog.addEventListener('close', () => {
        // Return focus to the thumbnail we ended on, so keyboard users
        // land where they left off rather than where they started.
        imageFigures[current].querySelector('img')?.focus();
    });
})();
