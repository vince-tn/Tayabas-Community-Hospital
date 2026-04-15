from pathlib import Path
base = Path('/mnt/data/tchi-static')
assets = 'assets'

shared_head = '''
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f7faf7;
      --bg-soft: #eef4f0;
      --surface: rgba(255,255,255,0.92);
      --text: #32413b;
      --muted: #71837b;
      --heading: #31423d;
      --primary: #5f8f7e;
      --primary-deep: #486f62;
      --line: #dde6e0;
      --shadow: 0 18px 40px rgba(42, 61, 53, 0.08);
      --radius-xl: 32px;
      --radius-lg: 24px;
      --radius-md: 16px;
      --max: 1180px;
      --topbar-h: 34px;
      --nav-h: 82px;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background:
        radial-gradient(circle at left top, rgba(95, 143, 126, 0.08), transparent 24%),
        linear-gradient(180deg, #fbfcfb 0%, #f5f8f5 100%);
      color: var(--text);
    }

    img { max-width: 100%; display: block; }
    a { color: inherit; text-decoration: none; }
    button, input, select { font: inherit; }

    .container { width: min(calc(100% - 2rem), var(--max)); margin: 0 auto; }
    .section { padding: 88px 0; scroll-margin-top: calc(var(--topbar-h) + var(--nav-h) + 20px); }
    .section.alt { background: linear-gradient(180deg, rgba(255,255,255,0.5), rgba(238,244,240,0.8)); }
    .card {
      background: var(--surface);
      border: 1px solid rgba(72, 111, 98, 0.1);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow);
    }

    .kicker {
      display: inline-flex; align-items: center; min-height: 40px; padding: 0 1rem;
      border-radius: 999px; background: rgba(95, 143, 126, 0.1); color: var(--primary-deep);
      font-size: 0.76rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase;
      margin-bottom: 1rem;
    }
    .section-heading h2, .hero-title, .banner h2, .page-hero h1, .footer-brand strong {
      margin: 0; font-family: 'Cormorant Garamond', serif; color: var(--heading); letter-spacing: -0.03em; font-weight: 500;
    }
    .section-heading h2 { font-size: clamp(2.5rem, 4vw, 3.5rem); line-height: 1; }
    .section-heading p { margin: 0.75rem 0 0; color: var(--muted); max-width: 620px; line-height: 1.8; }
    .section-row { display: flex; align-items: end; justify-content: space-between; gap: 1rem; margin-bottom: 2rem; }

    .btn {
      display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
      min-height: 48px; padding: 0 1.2rem; border-radius: 12px; border: 1px solid transparent;
      font-size: 0.96rem; font-weight: 600; transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
      cursor: pointer;
    }
    .btn:hover { transform: translateY(-2px); }
    .btn-primary { background: var(--primary); color: #fff; box-shadow: 0 14px 28px rgba(95, 143, 126, 0.22); }
    .btn-secondary { background: #fff; color: var(--heading); border-color: var(--line); }
    .btn-text { color: var(--primary-deep); font-weight: 600; }

    .topbar {
      min-height: var(--topbar-h); display: flex; align-items: center; background: var(--primary);
      color: rgba(255,255,255,0.96); font-size: 0.82rem;
    }
    .topbar-row, .topbar-group { display: flex; align-items: center; gap: 1.2rem; }
    .topbar-row { justify-content: space-between; flex-wrap: wrap; }
    .topbar-item { display: inline-flex; align-items: center; gap: 0.42rem; white-space: nowrap; }
    .topbar-item svg { width: 14px; height: 14px; }

    .site-header {
      position: sticky; top: var(--topbar-h); z-index: 50; backdrop-filter: blur(12px);
      background: rgba(251,252,251,0.88); border-bottom: 1px solid rgba(72, 111, 98, 0.08);
    }
    .nav-wrap { min-height: var(--nav-h); display: flex; align-items: center; justify-content: space-between; gap: 1.2rem; position: relative; }
    .brand { display: flex; align-items: center; gap: 0.95rem; min-width: 0; }
    .brand img { width: 56px; height: 56px; object-fit: contain; }
    .brand-copy strong { display: block; font-size: 1.9rem; line-height: .95; }
    .brand-copy span { display: block; margin-top: .18rem; color: var(--primary-deep); font-size: 0.72rem; letter-spacing: .14em; text-transform: uppercase; font-weight: 600; }

    .nav-links { display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; }
    .nav-links a { position: relative; padding: 0.45rem 0; font-size: 0.95rem; font-weight: 500; color: var(--heading); }
    .nav-links a::after {
      content: ''; position: absolute; left: 0; right: 0; bottom: -0.15rem; height: 2px; background: var(--primary);
      transform: scaleX(0); transform-origin: left; transition: transform .2s ease;
    }
    .nav-links a:hover::after, .nav-links a.active::after { transform: scaleX(1); }
    .menu-toggle {
      display: none; width: 46px; height: 46px; border-radius: 12px; border: 1px solid var(--line); background: #fff;
      color: var(--primary-deep); cursor: pointer;
    }

    .hero { padding: 72px 0 86px; position: relative; overflow: hidden; }
    .hero::before {
      content: ''; position: absolute; inset: 0; background-image: radial-gradient(circle, rgba(95,143,126,.12) 1px, transparent 1px);
      background-size: 30px 30px; opacity: .14; pointer-events: none;
    }
    .hero-grid { position: relative; z-index: 1; display: grid; grid-template-columns: minmax(0,.95fr) minmax(0,1.05fr); gap: 3rem; align-items: center; }
    .hero-title { font-size: clamp(3.3rem, 6vw, 4.8rem); line-height: .92; max-width: 520px; }
    .hero-title span { display: block; color: var(--primary); }
    .hero-sub { margin: .65rem 0 0; font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-style: italic; color: var(--primary-deep); }
    .hero-actions { display: flex; flex-wrap: wrap; gap: .85rem; margin-top: 1.6rem; }
    .hero-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin-top: 2rem; padding-top: 1.6rem; border-top: 1px solid var(--line); max-width: 560px; }
    .stat strong { display: block; font-size: 1.08rem; color: var(--primary-deep); margin-bottom: .22rem; font-weight: 600; }
    .stat span { display: block; font-size: .93rem; line-height: 1.6; color: var(--muted); }
    .hero-media {
      position: relative; min-height: 520px; border-radius: 30px; overflow: hidden; box-shadow: var(--shadow); background: #dde6e0;
    }
    .hero-media img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
    .hero-media::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(21,38,33,0) 45%, rgba(21,38,33,.2) 100%); }

    .split-grid { display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1fr); gap: 1.2rem; align-items: stretch; }
    .about-copy { padding: 1.5rem; }
    .about-copy p { margin: 0; line-height: 1.9; color: var(--muted); }
    .about-copy p + p { margin-top: 1rem; }
    .vision-grid { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1rem; margin-top: 1rem; }
    .vision-card { padding: 1.2rem; border-radius: 18px; background: linear-gradient(180deg, #5f8f7e, #4d7769); color: #fff; box-shadow: 0 18px 32px rgba(95,143,126,.22); }
    .vision-card h3 { margin: 0 0 .55rem; font-size: 1.02rem; font-weight: 600; }
    .vision-card p, .vision-card li { margin: 0; line-height: 1.7; font-size: .95rem; color: rgba(255,255,255,.95); }
    .vision-card ul { margin: 0; padding-left: 1rem; display: grid; gap: .35rem; }
    .about-media { position: relative; min-height: 100%; overflow: hidden; border-radius: 24px; background: #dce5df; }
    .about-media img { width: 100%; height: 100%; min-height: 540px; object-fit: cover; }

    .grid-3 { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1rem; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 1rem; }
    .news-card, .service-card, .event-card, .mini-card { overflow: hidden; }
    .thumb { position: relative; aspect-ratio: 1.2 / .9; background: #dde6e0; overflow: hidden; }
    .thumb img { width: 100%; height: 100%; object-fit: cover; transition: transform .3s ease; }
    .news-card:hover .thumb img, .service-card:hover .thumb img, .event-card:hover .thumb img { transform: scale(1.04); }
    .thumb::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(20,34,30,0) 35%, rgba(20,34,30,.6) 100%); }
    .thumb-label { position: absolute; left: 1rem; bottom: .95rem; z-index: 1; color: #fff; font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; }
    .body { padding: 1.1rem 1.15rem 1.2rem; }
    .body h3 { margin: 0 0 .5rem; font-size: 1.08rem; color: var(--heading); font-weight: 600; }
    .body p, .mini-card p, .faq-answer p, .contact-info p, .contact-list li, .page-hero p { margin: 0; line-height: 1.75; color: var(--muted); }

    .services-layout { display: grid; grid-template-columns: minmax(0,1.06fr) minmax(0,.94fr); gap: 1rem; }
    .service-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 1rem; }
    .spotlight { padding: 1.5rem; border-radius: 24px; background: linear-gradient(180deg, #5f8f7e, #486f62); color: #fff; box-shadow: 0 22px 40px rgba(95,143,126,.22); }
    .spotlight h3 { margin: 0 0 .55rem; font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 500; }
    .spotlight p, .spotlight li { margin: 0; line-height: 1.78; color: rgba(255,255,255,.94); }
    .spotlight ul { margin: 1rem 0 0; padding-left: 1rem; display: grid; gap: .42rem; }

    .faq-wrap { display: grid; gap: .85rem; max-width: 900px; }
    .faq-item { overflow: hidden; }
    .faq-button {
      width: 100%; border: 0; background: transparent; padding: 1.1rem 1.2rem; display: flex; align-items: center; justify-content: space-between;
      gap: 1rem; text-align: left; font-weight: 600; color: var(--heading); cursor: pointer;
    }
    .faq-answer { max-height: 0; overflow: hidden; transition: max-height .28s ease; }
    .faq-answer-inner { padding: 0 1.2rem 1.2rem; }
    .faq-icon { font-size: 1.4rem; color: var(--primary); transition: transform .2s ease; }
    .faq-item.active .faq-icon { transform: rotate(45deg); }

    .banner { padding: 82px 0; background: var(--primary); color: rgba(255,255,255,.95); }
    .banner-inner { max-width: 880px; margin: 0 auto; text-align: center; }
    .banner h2 { color: #fff; font-size: clamp(2.3rem, 4vw, 3.3rem); line-height: 1.02; }
    .banner p { margin: 1rem auto 0; max-width: 650px; color: rgba(255,255,255,.92); line-height: 1.8; }
    .banner .hero-actions { justify-content: center; margin-top: 1.5rem; }

    .page-hero { padding: 68px 0 42px; }
    .page-hero h1 { font-size: clamp(3rem, 5vw, 4.4rem); line-height: .96; }
    .page-hero p { max-width: 680px; margin-top: .9rem; }
    .crumbs { display: inline-flex; gap: .5rem; color: var(--muted); font-size: .9rem; margin-bottom: 1rem; }

    .directory-layout { display: grid; grid-template-columns: minmax(0,.92fr) minmax(0,1.08fr); gap: 1rem; }
    .panel { padding: 1.35rem; }
    .field { display: flex; align-items: center; gap: .7rem; min-height: 56px; padding: 0 1rem; border-radius: 14px; border: 1px solid var(--line); background: #fff; }
    .field svg { width: 18px; height: 18px; color: var(--muted); flex-shrink: 0; }
    .field input, .field select { width: 100%; border: 0; outline: none; background: transparent; color: var(--heading); }
    .stack { display: grid; gap: .9rem; }
    .doctor-list { display: grid; gap: .75rem; margin-top: 1rem; }
    .doctor-item { width: 100%; text-align: left; border: 1px solid var(--line); background: #fff; border-radius: 14px; padding: 1rem; cursor: pointer; }
    .doctor-item strong { display: block; color: var(--heading); margin-bottom: .22rem; }
    .doctor-item span { display: block; color: var(--muted); font-size: .94rem; }
    .doctor-item.active { border-color: rgba(95,143,126,.45); box-shadow: var(--shadow); }
    .profile-header { display: grid; grid-template-columns: 190px minmax(0,1fr); gap: 1.2rem; align-items: center; }
    .profile-media { aspect-ratio: 1 / 1.06; border-radius: 20px; overflow: hidden; background: #dfe7e2; border: 1px solid rgba(72, 111, 98, 0.1); }
    .profile-media img { width: 100%; height: 100%; object-fit: cover; }
    .profile-header h2 { font-size: 2rem; }
    .profile-role { color: var(--primary-deep); font-weight: 600; }
    .data-grid { display: grid; gap: .8rem; margin-top: 1rem; }
    .data-row { display: grid; grid-template-columns: 180px minmax(0,1fr); gap: .9rem; padding-bottom: .8rem; border-bottom: 1px solid var(--line); }
    .data-row span { font-weight: 600; color: var(--heading); }

    .contact-grid { display: grid; grid-template-columns: 1.1fr .9fr .9fr; gap: 1rem; }
    .contact-card { padding: 1.25rem; }
    .contact-card h3 { margin: 0 0 .6rem; color: var(--heading); font-size: 1.1rem; }
    .contact-list { margin: 0; padding-left: 1rem; display: grid; gap: .45rem; }

    .footer { background: linear-gradient(180deg, #30473f, #263932); color: rgba(255,255,255,.9); padding: 58px 0 24px; }
    .footer-grid { display: grid; grid-template-columns: 1.15fr .8fr .95fr; gap: 2rem; padding-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,.12); }
    .footer-brand { display: flex; align-items: start; gap: 1rem; }
    .footer-brand img { width: 54px; height: 54px; object-fit: contain; }
    .footer-brand strong { color: #fff; display: block; font-size: 1.55rem; line-height: .96; margin-bottom: .45rem; }
    .footer h3 { margin: 0 0 .8rem; font-size: 1rem; color: #fff; }
    .footer p, .footer li { margin: 0; line-height: 1.75; color: rgba(255,255,255,.74); }
    .footer ul { margin: 0; padding: 0; list-style: none; display: grid; gap: .45rem; }
    .footer-bottom { padding-top: 1.1rem; text-align: center; color: rgba(255,255,255,.68); font-size: .9rem; }

    @media (max-width: 1080px) {
      .hero-grid, .split-grid, .services-layout, .directory-layout, .footer-grid, .contact-grid, .grid-3, .grid-4, .vision-grid { grid-template-columns: 1fr; }
      .service-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
      .profile-header { grid-template-columns: 1fr; }
      .about-media img { min-height: 420px; }
      .hero-media { min-height: 440px; }
    }
    @media (max-width: 920px) {
      .brand-copy strong { font-size: 1.45rem; }
      .brand-copy span { font-size: .68rem; }
      .menu-toggle { display: inline-grid; place-items: center; }
      .nav-links {
        position: absolute; left: 0; right: 0; top: calc(100% + .7rem); display: none; flex-direction: column; align-items: stretch;
        gap: .15rem; padding: .85rem; background: rgba(255,255,255,.98); border: 1px solid var(--line); border-radius: 18px; box-shadow: var(--shadow);
      }
      .nav-links.open { display: flex; }
      .hero-title { font-size: clamp(2.9rem, 9vw, 3.8rem); }
      .page-hero h1 { font-size: 3rem; }
    }
    @media (max-width: 760px) {
      :root { --topbar-h: auto; --nav-h: 74px; }
      .topbar { padding: .45rem 0; }
      .topbar-row, .topbar-group { justify-content: center; }
      .hero { padding: 46px 0 72px; }
      .hero-stats, .service-grid, .contact-grid { grid-template-columns: 1fr; }
      .hero-actions { flex-direction: column; align-items: stretch; }
      .section { padding: 74px 0; }
      .data-row { grid-template-columns: 1fr; gap: .35rem; }
      .profile-media { max-width: 250px; }
      .container { width: min(calc(100% - 1.2rem), var(--max)); }
    }
  </style>
'''

shared_script = '''
  <script>
    const menuToggle = document.getElementById('menuToggle');
    const primaryNav = document.getElementById('primaryNav');
    menuToggle?.addEventListener('click', () => {
      const isOpen = primaryNav.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', String(isOpen));
    });
    primaryNav?.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        primaryNav.classList.remove('open');
        menuToggle?.setAttribute('aria-expanded', 'false');
      });
    });
  </script>
'''


def topbar():
    return '''
  <div class="topbar">
    <div class="container topbar-row">
      <div class="topbar-group">
        <span class="topbar-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.11 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.89.33 1.76.62 2.6a2 2 0 0 1-.45 2.11L8 9.91a16 16 0 0 0 6.09 6.09l1.48-1.28a2 2 0 0 1 2.11-.45c.84.29 1.71.5 2.6.62A2 2 0 0 1 22 16.92z"/></svg>(042) 793-2216</span>
        <span class="topbar-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m4 6 8 6 8-6"/><rect x="3" y="5" width="18" height="14" rx="2"/></svg>administrative@tayabascommunityhospital.com</span>
      </div>
      <div class="topbar-group">
        <span class="topbar-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-6-5.33-6-11a6 6 0 1 1 12 0c0 5.67-6 11-6 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>Brgy. Wakas, Tayabas, Quezon, Philippines</span>
      </div>
    </div>
  </div>
'''


def header(active='home'):
    links = [
        ('index.cleaner.html#home', 'Home', 'home'),
        ('index.cleaner.html#about', 'About Us', 'about'),
        ('index.cleaner.html#services', 'Services', 'services'),
        ('index.cleaner.html#faqs', 'FAQs', 'faqs'),
        ('index.cleaner.html#news', "What's New", 'news'),
        ('index.cleaner.html#activities', 'Activities & Events', 'activities'),
        ('hmo.html', 'HMO', 'hmo'),
        ('doctors.html', "Doctor's Directory", 'doctors'),
        ('contact.html', 'Contact Us', 'contact'),
    ]
    nav = []
    for href, label, key in links:
        cls = ' class="active"' if key == active else ''
        nav.append(f'<a href="{href}"{cls}>{label}</a>')
    nav_html = '\n        '.join(nav)
    return f'''
  <header class="site-header">
    <div class="container nav-wrap">
      <a class="brand" href="index.cleaner.html#home" aria-label="Tayabas Community Hospital homepage">
        <img src="{assets}/tchi_logo.png" alt="Tayabas Community Hospital logo" />
        <div class="brand-copy">
          <strong>Tayabas Community</strong>
          <span>Hospital, Inc. • We serve. We care.</span>
        </div>
      </a>
      <button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Toggle navigation">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
      </button>
      <nav class="nav-links" id="primaryNav">
        {nav_html}
      </nav>
    </div>
  </header>
'''


def footer():
    return f'''
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="{assets}/tchi_logo.png" alt="Tayabas Community Hospital logo" />
          <div>
            <strong>Tayabas Community Hospital, Inc.</strong>
            <p>Dedicated to serving the community through accessible health care, compassionate support, and a patient-centered online experience.</p>
          </div>
        </div>
        <div>
          <h3>Quick Links</h3>
          <ul>
            <li><a href="index.cleaner.html#about">About Us</a></li>
            <li><a href="index.cleaner.html#services">Services</a></li>
            <li><a href="doctors.html">Doctor's Directory</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div>
          <h3>Contact</h3>
          <ul>
            <li>Brgy. Wakas, Tayabas, Quezon</li>
            <li>(042) 793-2216</li>
            <li>administrative@tayabascommunityhospital.com</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">© 2026 Tayabas Community Hospital, Inc. All rights reserved.</div>
    </div>
  </footer>
'''

home = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Tayabas Community Hospital, Inc.</title>
  <meta name="description" content="Static hospital website based on the provided Tayabas Community Hospital draft, redesigned with a cleaner multi-page layout." />
{shared_head}
</head>
<body>
{topbar()}
{header('home')}

  <main id="home">
    <!-- HERO -->
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="kicker">Healthcare for the community</div>
          <h1 class="hero-title">Tayabas Community <span>Hospital, Inc.</span></h1>
          <p class="hero-sub">“We serve. We care.”</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="contact.html">Contact Us</a>
            <a class="btn btn-secondary" href="#services">View Services</a>
          </div>
          <div class="hero-stats">
            <div class="stat"><strong>1976</strong><span>Operating since June 1</span></div>
            <div class="stat"><strong>24/7</strong><span>Community support mindset</span></div>
            <div class="stat"><strong>Brgy. Wakas</strong><span>Tayabas City location</span></div>
          </div>
        </div>
        <div class="hero-media">
          <img src="{assets}/tchi_hero_clean.jpg" alt="Tayabas Community Hospital interior reception area" />
        </div>
      </div>
    </section>

    <!-- ABOUT -->
    <section class="section alt" id="about">
      <div class="container">
        <div class="section-row">
          <div class="section-heading">
            <div class="kicker">About Us</div>
            <h2>Service, compassion, and commitment</h2>
            <p>The homepage only introduces the hospital briefly. The core history, vision, mission, and values are kept clean and readable instead of feeling crowded.</p>
          </div>
          <a class="btn-text" href="about.html" style="display:none;">View more</a>
        </div>
        <div class="split-grid">
          <div>
            <div class="about-copy card">
              <p>The Tayabas Community Hospital, Inc. was founded on May 1974 and started its operation on June 1, 1976, governed by the Board of Directors with Dr. Avelino Aguerra Obispo as the Chairman and Medical Director.</p>
              <p>The Tayabas Community Hospital, Inc. is located at Brgy. Wakas and was founded on May 31, 1976 by Dr. Avelino A. Obispo, the Chairman of the Board and Medical Director. It consists only of a main building which then followed by a three storey Annex Building.</p>
            </div>
            <div class="vision-grid">
              <article class="vision-card"><h3>Vision</h3><p>The Tayabas Community Hospital, Inc. is committed to render total quality health care delivery system to all through effective and efficient service.</p></article>
              <article class="vision-card"><h3>Mission</h3><p>The Tayabas Community Hospital, Inc. ensures utmost health care in serving and caring for the sick with competence, compassion and commitment.</p></article>
              <article class="vision-card"><h3>Core Values</h3><ul><li>Teamwork</li><li>Compassion</li><li>Human Dignity</li><li>Integrity</li></ul></article>
            </div>
          </div>
          <div class="about-media card"><img src="{assets}/tchi_about.jpg" alt="Exterior view of Tayabas Community Hospital" /></div>
        </div>
      </div>
    </section>

    <!-- SERVICES -->
    <section class="section" id="services">
      <div class="container">
        <div class="section-row">
          <div class="section-heading">
            <div class="kicker">Services</div>
            <h2>Core hospital services</h2>
            <p>The homepage shows the major service groups from the draft, while the dedicated HMO and doctor pages are separated into their own screens.</p>
          </div>
          <a class="btn btn-secondary" href="#services">View All Services</a>
        </div>
        <div class="services-layout">
          <div class="service-grid">
            <article class="service-card card"><div class="thumb"><img src="https://images.pexels.com/photos/7089401/pexels-photo-7089401.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Laboratory service" /><div class="thumb-label">Laboratory</div></div></article>
            <article class="service-card card"><div class="thumb"><img src="https://images.pexels.com/photos/305568/pexels-photo-305568.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Diagnostic imaging" /><div class="thumb-label">Diagnostic Imaging</div></div></article>
            <article class="service-card card"><div class="thumb"><img src="https://images.pexels.com/photos/139398/hall-hospital-interior-design-139398.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Pharmacy" /><div class="thumb-label">Pharmacy</div></div></article>
            <article class="service-card card"><div class="thumb"><img src="https://images.pexels.com/photos/236380/pexels-photo-236380.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Hemodialysis" /><div class="thumb-label">Hemodialysis</div></div></article>
          </div>
          <aside class="spotlight">
            <h3>Heart Station</h3>
            <p>Kept separate because the draft specifically lists the tests under this service.</p>
            <ul>
              <li>Stress Test</li>
              <li>ECG</li>
              <li>2D Echo</li>
              <li>Venous Duplex Scan</li>
            </ul>
          </aside>
        </div>
      </div>
    </section>

    <!-- NEWS -->
    <section class="section alt" id="news">
      <div class="container">
        <div class="section-row">
          <div class="section-heading">
            <div class="kicker">What's New</div>
            <h2>Hospital updates</h2>
            <p>This follows the screenshot's cleaner card presentation while keeping the three categories from the PDF draft.</p>
          </div>
        </div>
        <div class="grid-3">
          <article class="news-card card"><div class="thumb"><img src="https://images.pexels.com/photos/8460157/pexels-photo-8460157.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Advisories" /><div class="thumb-label">Advisories</div></div><div class="body"><h3>Important announcements</h3><p>Use this area for hospital reminders, notices, adjusted schedules, and patient advisories.</p></div></article>
          <article class="news-card card"><div class="thumb"><img src="https://images.pexels.com/photos/6823569/pexels-photo-6823569.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Featured service" /><div class="thumb-label">Featured Service</div></div><div class="body"><h3>Highlighted care offerings</h3><p>A cleaner way to spotlight a department or procedure without overloading the homepage.</p></div></article>
          <article class="news-card card"><div class="thumb"><img src="https://images.pexels.com/photos/6129119/pexels-photo-6129119.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Promos and packages" /><div class="thumb-label">Promos and Packages</div></div><div class="body"><h3>Future health packages</h3><p>Ready for promos, package bundles, or preventive care campaigns later on.</p></div></article>
        </div>
      </div>
    </section>

    <!-- ACTIVITIES -->
    <section class="section" id="activities">
      <div class="container">
        <div class="section-row">
          <div class="section-heading">
            <div class="kicker">Activities & Events</div>
            <h2>Community highlights</h2>
            <p>The activity titles below are taken from the draft and styled more like the cleaner reference design.</p>
          </div>
        </div>
        <div class="grid-3">
          <article class="event-card card"><div class="thumb"><img src="https://images.pexels.com/photos/7551615/pexels-photo-7551615.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Founding anniversary event" /><div class="thumb-label">TCHI Celebrates 47th Founding Anniversary</div></div><div class="body"><h3>Founding anniversary</h3><p>A polished card layout for milestone events, recaps, and hospital celebrations.</p></div></article>
          <article class="event-card card"><div class="thumb"><img src="https://images.pexels.com/photos/5998472/pexels-photo-5998472.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Admin department event" /><div class="thumb-label">Admin Department is the Champ!</div></div><div class="body"><h3>Department recognition</h3><p>Perfect for internal highlights and team achievements without making the page feel heavy.</p></div></article>
          <article class="event-card card"><div class="thumb"><img src="https://images.pexels.com/photos/7088524/pexels-photo-7088524.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Kamustahan event" /><div class="thumb-label">Employees Joins 2022 Kamustahan</div></div><div class="body"><h3>Community gathering</h3><p>Works well for photo-driven moments and staff community engagement posts.</p></div></article>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section alt" id="faqs">
      <div class="container">
        <div class="section-row">
          <div class="section-heading">
            <div class="kicker">FAQs</div>
            <h2>Quick answers for visitors</h2>
            <p>Only the draft's questions are kept here, but the delivery is cleaner and more minimal.</p>
          </div>
        </div>
        <div class="faq-wrap">
          <article class="faq-item card active"><button class="faq-button" type="button"><span>When is the visiting hours?</span><span class="faq-icon">+</span></button><div class="faq-answer" style="max-height:180px;"><div class="faq-answer-inner"><p>Visiting hours starts from 8:00 am until 8:00 pm only.</p></div></div></article>
          <article class="faq-item card"><button class="faq-button" type="button"><span>Do you accept credit card?</span><span class="faq-icon">+</span></button><div class="faq-answer"><div class="faq-answer-inner"><p>Please confirm the latest payment method details directly with the hospital before visiting.</p></div></div></article>
          <article class="faq-item card"><button class="faq-button" type="button"><span>Are children below 8 years old allowed to visit a patient?</span><span class="faq-icon">+</span></button><div class="faq-answer"><div class="faq-answer-inner"><p>Please confirm current visitor restrictions and safety protocols with the hospital before planning a visit.</p></div></div></article>
        </div>
      </div>
    </section>

    <section class="banner">
      <div class="container banner-inner">
        <h2>Need hospital information quickly?</h2>
        <p>For HMO information, doctor directory lookup, or department numbers, use the dedicated pages from the navigation for a cleaner browsing flow.</p>
        <div class="hero-actions">
          <a class="btn btn-secondary" href="doctors.html">Doctor's Directory</a>
          <a class="btn btn-secondary" href="contact.html">Contact Us</a>
        </div>
      </div>
    </section>
  </main>

{footer()}
  <script>
    document.querySelectorAll('.faq-item').forEach(item => {{
      const button = item.querySelector('.faq-button');
      const answer = item.querySelector('.faq-answer');
      button.addEventListener('click', () => {{
        const open = item.classList.contains('active');
        document.querySelectorAll('.faq-item').forEach(other => {{ other.classList.remove('active'); other.querySelector('.faq-answer').style.maxHeight = '0px'; }});
        if (!open) {{ item.classList.add('active'); answer.style.maxHeight = answer.scrollHeight + 'px'; }}
      }});
    }});
  </script>
{shared_script}
</body>
</html>'''

hmo = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>HMO | Tayabas Community Hospital, Inc.</title>
{shared_head}
</head>
<body>
{topbar()}
{header('hmo')}
  <main>
    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="index.cleaner.html">Home</a> / <span>HMO</span></div>
        <h1>HMO partners and affiliated doctors</h1>
        <p>This page keeps the HMO content separate from the homepage, which better matches the cleaner reference layout while still using the names shown in the draft.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="grid-3">
          <article class="mini-card card"><div class="body"><h3>Intellicare</h3><p>Included based on the HMO page direction shown in the draft.</p></div></article>
          <article class="mini-card card"><div class="body"><h3>Maxicare</h3><p>Can later be expanded with coverage notes and department-specific reminders.</p></div></article>
          <article class="mini-card card"><div class="body"><h3>MediCard</h3><p>Presented in a simpler way so the page feels clean rather than crowded.</p></div></article>
        </div>
      </div>
    </section>
    <section class="section alt">
      <div class="container">
        <div class="section-heading">
          <div class="kicker">Doctors Listed in Draft</div>
          <h2>Affiliated doctors shown in the outline</h2>
          <p>The PDF shows these doctors on the HMO page.</p>
        </div>
        <div class="grid-4" style="margin-top:2rem;">
          <article class="mini-card card"><div class="body"><h3>Dra. Samantha O. Mortos</h3><p>Cardiologist</p></div></article>
          <article class="mini-card card"><div class="body"><h3>Dr. Aldrin C. Nadres</h3><p>Family Medicine</p></div></article>
          <article class="mini-card card"><div class="body"><h3>Dr. Kristoffer M. Mortos</h3><p>General Surgeon</p></div></article>
          <article class="mini-card card"><div class="body"><h3>Dr. Emmanuel B. Yap</h3><p>General Surgeon</p></div></article>
        </div>
      </div>
    </section>
  </main>
{footer()}
{shared_script}
</body>
</html>'''

doctors = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Doctor's Directory | Tayabas Community Hospital, Inc.</title>
{shared_head}
</head>
<body>
{topbar()}
{header('doctors')}
  <main>
    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="index.cleaner.html">Home</a> / <span>Doctor's Directory</span></div>
        <h1>Doctor's Directory</h1>
        <p>The draft showed a separate directory and profile page. This version keeps that idea by moving the directory into its own dedicated page.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="container directory-layout">
        <div class="panel card">
          <div class="stack">
            <label class="field"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path></svg><input id="doctorSearch" type="text" placeholder="Doctor's Name" /></label>
            <label class="field"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 5h18M6 12h12M10 19h4"></path></svg><select id="specialtyFilter"><option value="all">Specialization</option><option value="Cardiology">Cardiology</option><option value="Family Medicine">Family Medicine</option><option value="General Surgery">General Surgery</option></select></label>
          </div>
          <div class="doctor-list" id="doctorList"></div>
        </div>
        <div class="panel card">
          <div class="profile-header">
            <div class="profile-media"><img src="https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=900" alt="Doctor profile visual" /></div>
            <div>
              <h2 id="previewName">Dra. Samantha O. Mortos</h2>
              <div class="profile-role" id="previewSpecialty">Cardiology</div>
              <p style="margin-top:.8rem;">This preview follows the separate doctor profile direction shown in the PDF.</p>
              <div class="hero-actions" style="margin-top:1rem;"><a class="btn btn-secondary" id="profileLink" href="doctor-profile.html?doctor=samantha">Open profile page</a></div>
            </div>
          </div>
          <div class="data-grid">
            <div class="data-row"><span>Name</span><div id="previewNameRow">Dra. Samantha O. Mortos</div></div>
            <div class="data-row"><span>Specialization</span><div id="previewSpecialtyRow">Cardiology</div></div>
            <div class="data-row"><span>Contact Number</span><div id="previewContact">Please inquire at the hospital contact desk</div></div>
            <div class="data-row"><span>Clinic Hours</span><div id="previewHours">Schedule available upon inquiry</div></div>
            <div class="data-row"><span>HMO Affiliation</span><div id="previewHmo">Intellicare, MediCard</div></div>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer()}
  <script>
    const doctors = [
      {{ slug: 'samantha', name: 'Dra. Samantha O. Mortos', specialty: 'Cardiology', contact: 'Please inquire at the hospital contact desk', clinicHours: 'Schedule available upon inquiry', hmo: 'Intellicare, MediCard' }},
      {{ slug: 'aldrin', name: 'Dr. Aldrin C. Nadres', specialty: 'Family Medicine', contact: 'Please inquire at the hospital contact desk', clinicHours: 'Schedule available upon inquiry', hmo: 'Maxicare' }},
      {{ slug: 'kristoffer', name: 'Dr. Kristoffer M. Mortos', specialty: 'General Surgery', contact: 'Please inquire at the hospital contact desk', clinicHours: 'Schedule available upon inquiry', hmo: 'Intellicare, Maxicare' }},
      {{ slug: 'emmanuel', name: 'Dr. Emmanuel B. Yap', specialty: 'General Surgery', contact: 'Please inquire at the hospital contact desk', clinicHours: 'Schedule available upon inquiry', hmo: 'MediCard' }}
    ];
    const doctorList = document.getElementById('doctorList');
    const searchInput = document.getElementById('doctorSearch');
    const specialtyFilter = document.getElementById('specialtyFilter');
    const previewName = document.getElementById('previewName');
    const previewSpecialty = document.getElementById('previewSpecialty');
    const previewNameRow = document.getElementById('previewNameRow');
    const previewSpecialtyRow = document.getElementById('previewSpecialtyRow');
    const previewContact = document.getElementById('previewContact');
    const previewHours = document.getElementById('previewHours');
    const previewHmo = document.getElementById('previewHmo');
    const profileLink = document.getElementById('profileLink');

    function updatePreview(doctor) {{
      previewName.textContent = doctor.name;
      previewSpecialty.textContent = doctor.specialty;
      previewNameRow.textContent = doctor.name;
      previewSpecialtyRow.textContent = doctor.specialty;
      previewContact.textContent = doctor.contact;
      previewHours.textContent = doctor.clinicHours;
      previewHmo.textContent = doctor.hmo;
      profileLink.href = 'doctor-profile.html?doctor=' + doctor.slug;
    }}

    function renderDoctors(activeSlug = 'samantha') {{
      const term = searchInput.value.trim().toLowerCase();
      const specialty = specialtyFilter.value;
      const filtered = doctors.filter(d => d.name.toLowerCase().includes(term) && (specialty === 'all' || d.specialty === specialty));
      doctorList.innerHTML = '';
      const active = filtered.find(d => d.slug === activeSlug) || filtered[0] || doctors[0];
      updatePreview(active);
      filtered.forEach(doctor => {{
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'doctor-item' + (doctor.slug === active.slug ? ' active' : '');
        btn.innerHTML = `<strong>${{doctor.name}}</strong><span>${{doctor.specialty}}</span>`;
        btn.addEventListener('click', () => {{ updatePreview(doctor); document.querySelectorAll('.doctor-item').forEach(el => el.classList.remove('active')); btn.classList.add('active'); }});
        doctorList.appendChild(btn);
      }});
    }}
    renderDoctors();
    searchInput.addEventListener('input', () => renderDoctors());
    specialtyFilter.addEventListener('change', () => renderDoctors());
  </script>
{shared_script}
</body>
</html>'''

profile = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Doctor Profile | Tayabas Community Hospital, Inc.</title>
{shared_head}
</head>
<body>
{topbar()}
{header('doctors')}
  <main>
    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="index.cleaner.html">Home</a> / <a href="doctors.html">Doctor's Directory</a> / <span>Doctor Profile</span></div>
        <h1>Doctor Profile</h1>
        <p>This page follows the separate “Doctors’ Profile” page shown in the PDF, instead of squeezing the full profile into the homepage.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="container">
        <div class="panel card">
          <div class="profile-header">
            <div class="profile-media"><img src="https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=900" alt="Doctor profile visual" /></div>
            <div>
              <h2 id="name">Dra. Samantha O. Mortos</h2>
              <div class="profile-role" id="specialty">Cardiology</div>
              <p style="margin-top:.8rem;">A cleaner version of the draft's profile layout with dedicated rows for the same core details.</p>
            </div>
          </div>
          <div class="data-grid">
            <div class="data-row"><span>Name</span><div id="nameRow">Dra. Samantha O. Mortos</div></div>
            <div class="data-row"><span>Specialization</span><div id="specialtyRow">Cardiology</div></div>
            <div class="data-row"><span>Contact Number</span><div id="contact">Please inquire at the hospital contact desk</div></div>
            <div class="data-row"><span>Clinic Hours</span><div id="hours">Schedule available upon inquiry</div></div>
            <div class="data-row"><span>HMO Affiliation</span><div id="hmo">Intellicare, MediCard</div></div>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer()}
  <script>
    const data = {{
      samantha: {{ name: 'Dra. Samantha O. Mortos', specialty: 'Cardiology', contact: 'Please inquire at the hospital contact desk', hours: 'Schedule available upon inquiry', hmo: 'Intellicare, MediCard' }},
      aldrin: {{ name: 'Dr. Aldrin C. Nadres', specialty: 'Family Medicine', contact: 'Please inquire at the hospital contact desk', hours: 'Schedule available upon inquiry', hmo: 'Maxicare' }},
      kristoffer: {{ name: 'Dr. Kristoffer M. Mortos', specialty: 'General Surgery', contact: 'Please inquire at the hospital contact desk', hours: 'Schedule available upon inquiry', hmo: 'Intellicare, Maxicare' }},
      emmanuel: {{ name: 'Dr. Emmanuel B. Yap', specialty: 'General Surgery', contact: 'Please inquire at the hospital contact desk', hours: 'Schedule available upon inquiry', hmo: 'MediCard' }}
    }};
    const slug = new URLSearchParams(window.location.search).get('doctor') || 'samantha';
    const doctor = data[slug] || data.samantha;
    document.getElementById('name').textContent = doctor.name;
    document.getElementById('specialty').textContent = doctor.specialty;
    document.getElementById('nameRow').textContent = doctor.name;
    document.getElementById('specialtyRow').textContent = doctor.specialty;
    document.getElementById('contact').textContent = doctor.contact;
    document.getElementById('hours').textContent = doctor.hours;
    document.getElementById('hmo').textContent = doctor.hmo;
  </script>
{shared_script}
</body>
</html>'''

contact = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Contact Us | Tayabas Community Hospital, Inc.</title>
{shared_head}
</head>
<body>
{topbar()}
{header('contact')}
  <main>
    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="index.cleaner.html">Home</a> / <span>Contact Us</span></div>
        <h1>Contact Us</h1>
        <p>The contact page stays separate to keep the homepage lighter, while still using the landline, email, and department placeholders from the draft.</p>
      </div>
    </section>
    <section class="section alt">
      <div class="container contact-grid">
        <article class="contact-card card"><div class="contact-info"><h3>Main Contact</h3><p><strong style="color:var(--heading)">Landline:</strong> (042) 793-2216</p><p><strong style="color:var(--heading)">Email Address:</strong> administrative@tayabascommunityhospital.com</p><p><strong style="color:var(--heading)">Location:</strong> Brgy. Wakas, Tayabas, Quezon, Philippines</p></div></article>
        <article class="contact-card card"><h3>Department Numbers</h3><ul class="contact-list"><li>ER : 09xx xxxxxxx</li><li>Admitting : 09xx xxxxxxx</li><li>Laboratory : 09xx xxxxxxx</li></ul></article>
        <article class="contact-card card"><h3>More Lines</h3><ul class="contact-list"><li>Diagnostic Imaging : 09xx xxxxxxx</li><li>Hemodialysis : 09xx xxxxxxx</li><li>Medical Arts Building : 09xx xxxxxxx</li></ul></article>
      </div>
    </section>
  </main>
{footer()}
{shared_script}
</body>
</html>'''

(base / 'index.cleaner.html').write_text(home, encoding='utf-8')
(base / 'hmo.html').write_text(hmo, encoding='utf-8')
(base / 'doctors.html').write_text(doctors, encoding='utf-8')
(base / 'doctor-profile.html').write_text(profile, encoding='utf-8')
(base / 'contact.html').write_text(contact, encoding='utf-8')

