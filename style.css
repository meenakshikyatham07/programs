:root {
  --bg: #fffaf3;
  --bg-strong: #fff4e3;
  --surface: #ffffff;
  --surface-alt: #f5ede4;
  --primary: #c75d2c;
  --primary-dark: #9d3d18;
  --accent: #f5b15b;
  --text: #1d1b1a;
  --muted: #5e4f46;
  --line: rgba(29, 27, 26, 0.1);
  --shadow: 0 18px 35px rgba(52, 34, 24, 0.12);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Inter", sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}

img {
  max-width: 100%;
  display: block;
}

a {
  text-decoration: none;
  color: inherit;
}

button,
input,
select {
  font: inherit;
}

.container {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(255, 250, 243, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 78px;
  gap: 16px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.brand-mark {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--primary), var(--accent));
  color: #fff;
  font-size: 0.9rem;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 28px;
  color: var(--muted);
  font-weight: 500;
}

.nav-links a {
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: var(--primary);
}

.nav-button,
.primary-btn,
.secondary-btn,
.filter-btn {
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}

.nav-button,
.primary-btn {
  background: linear-gradient(135deg, var(--primary), #e57d44);
  color: #fff;
  border-radius: 999px;
  padding: 0.9rem 1.5rem;
  box-shadow: 0 14px 25px rgba(199, 93, 44, 0.28);
  font-weight: 600;
}

.primary-btn:hover,
.secondary-btn:hover,
.nav-button:hover,
.filter-btn:hover {
  transform: translateY(-2px);
}

.secondary-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: transparent;
  border: 1px solid rgba(29, 27, 26, 0.12);
  padding: 0.9rem 1.5rem;
  color: var(--text);
  font-weight: 600;
}

.hero {
  padding: 72px 0 48px;
}

.hero-inner {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 48px;
}

.eyebrow {
  display: inline-block;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.73rem;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 14px;
}

.eyebrow.accent {
  color: var(--primary);
}

h1,
h2,
h3 {
  font-family: "Playfair Display", serif;
  line-height: 1.08;
}

h1 {
  font-size: clamp(2.8rem, 5vw, 5rem);
  margin-bottom: 16px;
  max-width: 620px;
}

h2 {
  font-size: clamp(2.2rem, 3vw, 3.3rem);
  margin-bottom: 16px;
}

.hero-text,
.about-content p,
.contact-copy p,
.menu-copy p {
  color: var(--muted);
  font-size: 1.06rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 26px;
}

.hero-highlights {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-top: 26px;
  list-style: none;
  color: var(--text);
  font-weight: 600;
}

.hero-highlights li {
  position: relative;
  padding-left: 18px;
}

.hero-highlights li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: var(--primary);
}

.hero-visual {
  position: relative;
  min-height: 560px;
  display: grid;
  place-items: center;
}

.dish-card.large {
  width: min(480px, 100%);
  border-radius: 30px;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.dish-card.large img {
  width: 100%;
  height: 600px;
  object-fit: cover;
}

.floating-card {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(29, 27, 26, 0.06);
  border-radius: 16px;
  padding: 1rem 1.1rem;
  box-shadow: var(--shadow);
}

.floating-card span {
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.card-one {
  left: 10px;
  bottom: 80px;
}

.card-two {
  right: 30px;
  top: 40px;
}

.features {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 22px;
  padding: 36px 0 14px;
}

.feature-item {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 30px 24px;
  box-shadow: 0 10px 28px rgba(44, 31, 23, 0.04);
}

.icon {
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  background: var(--bg-strong);
  border-radius: 14px;
  font-size: 1.7rem;
  margin-bottom: 18px;
}

.feature-item h3 {
  margin-bottom: 10px;
  font-size: 1.7rem;
}

.menu-section,
.about-section,
.testimonial-section,
.contact-section {
  padding: 96px 0;
}

.section-heading {
  margin-bottom: 30px;
}

.section-heading.center {
  text-align: center;
}

.menu-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 26px;
}

.filter-btn {
  background: #fff;
  color: var(--text);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 0.7rem 1.1rem;
  font-weight: 600;
}

.filter-btn.active {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.menu-item {
  background: var(--surface);
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid var(--line);
  box-shadow: 0 14px 28px rgba(41, 27, 21, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.menu-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 30px rgba(41, 27, 21, 0.1);
}

.menu-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.menu-copy {
  padding: 22px 18px 24px;
}

.menu-topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 8px;
}

.menu-topline h3 {
  font-size: 1.5rem;
}

.menu-topline span {
  color: var(--primary);
  font-weight: 700;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 46px;
}

.about-image img {
  width: 100%;
  height: 540px;
  object-fit: cover;
  border-radius: 26px;
  box-shadow: var(--shadow);
}

.about-points {
  list-style: none;
  margin-top: 22px;
  display: grid;
  gap: 12px;
  font-weight: 600;
}

.about-points li::before {
  content: "✓";
  color: var(--primary);
  margin-right: 10px;
}

.testimonial-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 22px;
}

blockquote {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 28px 24px;
  color: var(--text);
  box-shadow: 0 12px 24px rgba(51, 35, 25, 0.04);
  font-size: 1.03rem;
}

blockquote footer {
  margin-top: 18px;
  color: var(--primary);
  font-weight: 700;
}

.contact-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  background: linear-gradient(135deg, #fff5ea, #fffdf9);
  border-radius: 30px;
  border: 1px solid var(--line);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.contact-copy,
.reservation-form {
  padding: 42px;
}

.contact-details {
  display: grid;
  gap: 10px;
  margin-top: 20px;
  color: var(--muted);
  font-weight: 500;
}

.reservation-form {
  display: grid;
  gap: 18px;
  background: rgba(255, 255, 255, 0.4);
}

.reservation-form label {
  display: grid;
  gap: 8px;
  font-weight: 600;
}

.reservation-form input,
.reservation-form select {
  width: 100%;
  border: 1px solid rgba(29, 27, 26, 0.12);
  border-radius: 12px;
  padding: 0.85rem 1rem;
  background: #fff;
}

.full-width {
  width: 100%;
  margin-top: 10px;
}

.site-footer {
  border-top: 1px solid var(--line);
  background: #fff;
}

.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 76px;
  gap: 16px;
  color: var(--muted);
}

.socials {
  display: flex;
  gap: 16px;
}

@media (max-width: 900px) {
  .hero-inner,
  .about-grid,
  .contact-box,
  .menu-grid,
  .testimonial-grid,
  .features {
    grid-template-columns: 1fr;
  }

  .nav-links {
    display: none;
  }

  .hero-visual {
    min-height: 420px;
  }

  .dish-card.large img {
    height: 440px;
  }
}

@media (max-width: 540px) {
  .navbar {
    padding: 12px 0;
  }

  .nav-button,
  .primary-btn,
  .secondary-btn {
    width: 100%;
  }

  .hero-actions {
    flex-direction: column;
  }

  .contact-copy,
  .reservation-form {
    padding: 28px 22px;
  }

  .footer-inner {
    flex-direction: column;
    justify-content: center;
    padding: 18px 0;
  }
}
