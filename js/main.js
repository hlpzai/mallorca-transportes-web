(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('main-nav');

  if (toggle && header) {
    toggle.addEventListener('click', function () {
      var isOpen = header.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        header.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (item.open) {
        faqItems.forEach(function (other) {
          if (other !== item) other.removeAttribute('open');
        });
      }
    });
  });

  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var nombre = (data.get('nombre') || '').toString().trim();
      var telefono = (data.get('telefono') || '').toString().trim();
      var email = (data.get('email') || '').toString().trim();
      var servicio = (data.get('servicio') || '').toString().trim();
      var mensaje = (data.get('mensaje') || '').toString().trim();

      var subject = 'Solicitud de presupuesto - ' + servicio;
      var body =
        'Nombre: ' + nombre + '\n' +
        'Teléfono: ' + telefono + '\n' +
        'Email: ' + email + '\n' +
        'Servicio: ' + servicio + '\n\n' +
        'Detalles:\n' + (mensaje || '(sin detalles adicionales)');

      var mailto = 'mailto:info@mallorcatransportes.com' +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);

      window.location.href = mailto;
    });
  }

  var carousel = document.getElementById('testimonial-carousel');
  var track = document.getElementById('carousel-track');
  var dotsWrap = document.getElementById('carousel-dots');
  if (carousel && track && dotsWrap) {
    var originals = Array.prototype.slice.call(track.children);
    var count = originals.length;
    var index = 0;
    var itemsPerView = 1;
    var AUTOPLAY_MS = 5000;
    var TRANSITION_MS = 500;
    var timer = null;
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var dots = [];
    originals.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.setAttribute('aria-label', 'Ir a la opinión ' + (i + 1));
      dot.addEventListener('click', function () { goTo(i); restart(); });
      dotsWrap.appendChild(dot);
      dots.push(dot);
    });

    function getItemsPerView() {
      var w = window.innerWidth;
      if (w >= 1024) return 3;
      if (w >= 640) return 2;
      return 1;
    }

    // Appends clones of the first N slides so the loop can scroll seamlessly
    // past the real last card into a visual repeat of the first card(s).
    function rebuildClones() {
      Array.prototype.slice.call(track.querySelectorAll('.is-clone')).forEach(function (el) {
        el.remove();
      });
      var n = Math.min(itemsPerView, count);
      for (var i = 0; i < n; i++) {
        var clone = originals[i].cloneNode(true);
        clone.classList.add('is-clone');
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      }
    }

    function getStepPx() {
      var first = track.children[0];
      if (!first) return 0;
      var trackStyle = window.getComputedStyle(track);
      var gap = parseFloat(trackStyle.columnGap || trackStyle.gap || '0') || 0;
      return first.getBoundingClientRect().width + gap;
    }

    function render(withTransition) {
      track.style.transition = withTransition === false ? 'none' : '';
      track.style.transform = 'translateX(-' + (index * getStepPx()) + 'px)';
      var activeDot = index % count;
      dots.forEach(function (d, i) { d.classList.toggle('active', i === activeDot); });
    }

    function goTo(i) {
      index = i;
      render();
    }

    function next() {
      index++;
      render();
      if (index >= count) {
        window.setTimeout(function () {
          index = index - count;
          render(false);
          // force reflow so the next transition re-enables cleanly
          void track.offsetWidth;
          track.style.transition = '';
        }, TRANSITION_MS);
      }
    }

    function prev() {
      if (index <= 0) {
        index = count;
        render(false);
        void track.offsetWidth;
        track.style.transition = '';
      }
      index--;
      render();
    }

    function start() {
      if (reduceMotion || count <= itemsPerView) return;
      stop();
      timer = window.setInterval(next, AUTOPLAY_MS);
    }
    function stop() {
      if (timer) { window.clearInterval(timer); timer = null; }
    }
    function restart() { stop(); start(); }

    function setup() {
      var newItemsPerView = getItemsPerView();
      if (newItemsPerView !== itemsPerView || !track.querySelector('.is-clone')) {
        itemsPerView = newItemsPerView;
        carousel.style.setProperty('--items-per-view', itemsPerView);
        index = index % count;
        rebuildClones();
      }
      render(false);
    }

    carousel.querySelector('.carousel-arrow.next').addEventListener('click', function () { next(); restart(); });
    carousel.querySelector('.carousel-arrow.prev').addEventListener('click', function () { prev(); restart(); });

    carousel.addEventListener('mouseenter', stop);
    carousel.addEventListener('mouseleave', start);
    carousel.addEventListener('focusin', stop);
    carousel.addEventListener('focusout', start);

    var touchStartX = null;
    track.addEventListener('touchstart', function (e) {
      touchStartX = e.touches[0].clientX;
      stop();
    }, { passive: true });
    track.addEventListener('touchend', function (e) {
      if (touchStartX === null) return;
      var delta = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(delta) > 40) { delta < 0 ? next() : prev(); }
      touchStartX = null;
      start();
    });

    var resizeTimer = null;
    window.addEventListener('resize', function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(setup, 150);
    });

    setup();
    start();
  }
})();
