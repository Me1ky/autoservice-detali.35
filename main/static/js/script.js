document.addEventListener('DOMContentLoaded', function() {
    // 1. Адаптивное бургер-меню
    const header = document.querySelector('header');
    const nav = document.querySelector('nav');

    if (header && nav && window.innerWidth <= 768) {
        const burger = document.createElement('button');
        burger.className = 'burger-btn';
        burger.setAttribute('aria-label', 'Открыть меню');
        burger.textContent = '☰';
        header.style.position = 'relative';
        header.appendChild(burger);

        nav.classList.add('mobile-hidden');

        burger.addEventListener('click', function() {
            const isOpen = nav.classList.toggle('mobile-visible');
            nav.classList.toggle('mobile-hidden', !isOpen);
            burger.textContent = isOpen ? '✕' : '☰';
        });

        const links = nav.querySelectorAll('a');
        links.forEach(function(link) {
            link.addEventListener('click', function() {
                nav.classList.remove('mobile-visible');
                nav.classList.add('mobile-hidden');
                burger.textContent = '☰';
            });
        });
    }

    // 2. Анимация появления блоков при скролле
    const animElements = document.querySelectorAll('.card, .service-item, .contact-item, .stat-card, .page-hero, .hero');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        animElements.forEach(function(el) { observer.observe(el); });
    } else {
        animElements.forEach(function(el) { el.classList.add('visible'); });
    }
});