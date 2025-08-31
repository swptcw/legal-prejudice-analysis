# Setting Up Forms and Analytics for Your Legal Prejudice Analysis Landing Page

This guide will walk you through the process of setting up functional forms and analytics for your landing page at `legal-prejudice-analysis.com`.

## Table of Contents

1. [Setting Up the Newsletter Form](#setting-up-the-newsletter-form)
2. [Setting Up Google Analytics](#setting-up-google-analytics)
3. [Adding Contact Form Functionality](#adding-contact-form-functionality)
4. [Setting Up Event Tracking](#setting-up-event-tracking)
5. [Privacy Considerations](#privacy-considerations)

## Setting Up the Newsletter Form

Your landing page includes a newsletter subscription form. Here's how to make it functional:

### Option 1: Using Formspree (Simplest)

[Formspree](https://formspree.io/) is a simple solution that requires no backend:

1. Sign up for a free Formspree account
2. Create a new form
3. Update your newsletter form HTML:

```html
<form class="newsletter-form" action="https://formspree.io/f/your-form-id" method="POST">
    <input type="email" name="email" placeholder="Your email address" required>
    <button type="submit" class="btn btn-primary">Subscribe</button>
</form>
```

4. Test the form by submitting a subscription
5. Formspree will email you when someone subscribes

### Option 2: Using Mailchimp

For more advanced newsletter management:

1. Sign up for a [Mailchimp](https://mailchimp.com/) account
2. Create an audience for your subscribers
3. Generate an embedded form code
4. Replace your newsletter form with the Mailchimp code:

```html
<!-- Replace this with your Mailchimp form code -->
<div id="mc_embed_signup">
    <form action="https://yourdomain.us1.list-manage.com/subscribe/post?u=XXXXX&amp;id=XXXXX" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="newsletter-form validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
            <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="Your email address" required>
            <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
            <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_XXXXX_XXXXX" tabindex="-1" value=""></div>
            <button type="submit" name="subscribe" id="mc-embedded-subscribe" class="btn btn-primary">Subscribe</button>
        </div>
    </form>
</div>
```

5. Replace the `XXXXX` placeholders with your Mailchimp list ID and user ID

### Option 3: Using GitHub as a Backend

For a more integrated solution using your GitHub repository:

1. Create a GitHub Action workflow file at `.github/workflows/newsletter.yml`:

```yaml
name: Newsletter Subscription

on:
  issues:
    types: [opened]

jobs:
  process-subscription:
    if: contains(github.event.issue.title, '[NEWSLETTER]')
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        
      - name: Process subscription
        run: |
          EMAIL=$(echo "${{ github.event.issue.title }}" | sed 's/\[NEWSLETTER\] //')
          echo "New subscription: $EMAIL" >> subscribers.txt
          git config --global user.name "GitHub Action"
          git config --global user.email "action@github.com"
          git add subscribers.txt
          git commit -m "Add new subscriber: $EMAIL"
          git push
```

2. Update your newsletter form JavaScript:

```javascript
document.querySelector('.newsletter-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = this.querySelector('input[type="email"]').value.trim();
    if (!email) return;
    
    // Create an issue in your GitHub repository
    fetch('https://api.github.com/repos/yourusername/legal-prejudice-analysis/issues', {
        method: 'POST',
        headers: {
            'Authorization': 'token YOUR_GITHUB_TOKEN',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: `[NEWSLETTER] ${email}`,
            body: `New newsletter subscription from: ${email}`,
            labels: ['newsletter', 'subscription']
        })
    })
    .then(response => {
        if (response.ok) {
            alert('Thank you for subscribing!');
            this.reset();
        } else {
            alert('There was an error processing your subscription. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error processing your subscription. Please try again.');
    });
});
```

3. Replace `YOUR_GITHUB_TOKEN` with a personal access token with repo scope
4. **Important**: For security, use environment variables or a proper backend instead of embedding the token directly

## Setting Up Google Analytics

### Step 1: Create a Google Analytics Account

1. Go to [Google Analytics](https://analytics.google.com/)
2. Sign in with your Google account
3. Click "Start measuring"
4. Set up a new property:
   - Property name: "Legal Prejudice Analysis"
   - Reporting time zone: Your local time zone
   - Currency: Your preferred currency
5. Click "Create"

### Step 2: Set Up a Data Stream

1. In your new property, click "Data Streams"
2. Select "Web"
3. Enter your website URL: `https://legal-prejudice-analysis.com`
4. Enter a stream name: "Legal Prejudice Analysis Website"
5. Click "Create stream"

### Step 3: Add the Tracking Code to Your Website

1. After creating the stream, you'll see a Measurement ID (format: G-XXXXXXXX)
2. Add the following code to your website's `<head>` section:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXX');
</script>
```

3. Replace `G-XXXXXXXX` with your actual Measurement ID
4. Add this code to your `index.html` file just before the closing `</head>` tag

### Step 4: Verify Installation

1. Visit your website
2. Go to your Google Analytics account
3. Navigate to Reports > Realtime
4. You should see your visit recorded in real-time

## Adding Contact Form Functionality

Your landing page might benefit from a contact form. Here's how to add one:

### Step 1: Add the HTML Form

Add this code to your landing page where you want the contact form to appear:

```html
<section class="contact">
    <div class="container">
        <h2>Contact Us</h2>
        <p class="section-subtitle">Have questions about the Legal Prejudice Analysis system? Get in touch with our team.</p>
        
        <div class="contact-form-container">
            <form id="contact-form" class="contact-form">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label for="subject">Subject</label>
                    <input type="text" id="subject" name="subject" required>
                </div>
                
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" rows="5" required></textarea>
                </div>
                
                <button type="submit" class="btn btn-primary">Send Message</button>
            </form>
        </div>
    </div>
</section>
```

### Step 2: Add CSS Styles

Add these styles to your `styles.css` file:

```css
/* Contact Form Styles */
.contact {
    padding: var(--spacing-xl) 0;
    background-color: var(--white);
}

.contact-form-container {
    max-width: 600px;
    margin: 0 auto;
}

.contact-form {
    display: grid;
    gap: var(--spacing-md);
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
}

.form-group label {
    font-weight: 600;
    color: var(--dark-color);
}

.form-group input,
.form-group textarea {
    padding: 0.75rem;
    border: 1px solid var(--gray);
    border-radius: var(--border-radius-sm);
    font-family: var(--font-body);
    transition: border-color var(--transition-fast);
}

.form-group input:focus,
.form-group textarea:focus {
    border-color: var(--secondary-color);
    outline: none;
}

.contact-form .btn {
    justify-self: start;
}
```

### Step 3: Add JavaScript Functionality

Use Formspree for the contact form as well:

```javascript
// Add this to your main.js file
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        // Set the form action to your Formspree endpoint
        contactForm.setAttribute('action', 'https://formspree.io/f/your-form-id');
        contactForm.setAttribute('method', 'POST');
        
        contactForm.addEventListener('submit', function(e) {
            // You can add additional validation or processing here
            // For example, Google Analytics event tracking
            if (typeof gtag === 'function') {
                gtag('event', 'submit_form', {
                    'event_category': 'Contact',
                    'event_label': 'Contact Form Submission'
                });
            }
        });
    }
});
```

## Setting Up Event Tracking

Track important user interactions on your landing page:

### Step 1: Add Event Tracking Code

Add this to your `main.js` file:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Track button clicks
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            const buttonText = this.textContent.trim();
            const buttonHref = this.getAttribute('href');
            
            // Only track if Google Analytics is loaded
            if (typeof gtag === 'function') {
                gtag('event', 'button_click', {
                    'event_category': 'Engagement',
                    'event_label': buttonText,
                    'value': buttonHref
                });
            }
        });
    });
    
    // Track section visibility
    const sections = document.querySelectorAll('section[id]');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };
    
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && typeof gtag === 'function') {
                const sectionId = entry.target.getAttribute('id');
                gtag('event', 'section_view', {
                    'event_category': 'Engagement',
                    'event_label': sectionId
                });
                
                // Unobserve after first view to avoid duplicate events
                sectionObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        sectionObserver.observe(section);
    });
    
    // Track downloads
    document.querySelectorAll('a[href$=".pdf"], a[href$=".zip"], a[href$=".docx"]').forEach(link => {
        link.addEventListener('click', function() {
            const filePath = this.getAttribute('href');
            const fileName = filePath.split('/').pop();
            
            if (typeof gtag === 'function') {
                gtag('event', 'download', {
                    'event_category': 'Downloads',
                    'event_label': fileName,
                    'value': filePath
                });
            }
        });
    });
});
```

### Step 2: Set Up Custom Reports in Google Analytics

1. Go to your Google Analytics account
2. Navigate to Admin > Custom Definitions > Custom Metrics
3. Click "Create custom metrics" and set up metrics for:
   - Button clicks
   - Section views
   - Form submissions
   - Downloads

## Privacy Considerations

### Step 1: Create a Privacy Policy

Create a file named `privacy-policy.html` with content like:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Include your head content here -->
    <title>Privacy Policy - Legal Prejudice Analysis</title>
</head>
<body>
    <!-- Include your header here -->
    
    <section class="privacy-policy">
        <div class="container">
            <h1>Privacy Policy</h1>
            <p>Last updated: [Current Date]</p>
            
            <h2>1. Introduction</h2>
            <p>This Privacy Policy explains how Legal Prejudice Analysis ("we", "us", "our") collects, uses, and shares your information when you visit legal-prejudice-analysis.com.</p>
            
            <h2>2. Information We Collect</h2>
            <p>We collect information you provide directly to us, such as when you fill out a contact form or subscribe to our newsletter. This may include your name, email address, and any message content you provide.</p>
            <p>We also automatically collect certain information about your device, including information about your web browser, IP address, time zone, and some of the cookies installed on your device.</p>
            
            <h2>3. How We Use Your Information</h2>
            <p>We use the information we collect to:</p>
            <ul>
                <li>Respond to your inquiries and provide customer support</li>
                <li>Send you updates, newsletters, and marketing communications</li>
                <li>Improve our website and services</li>
                <li>Monitor and analyze trends, usage, and activities in connection with our website</li>
            </ul>
            
            <h2>4. Analytics</h2>
            <p>We use Google Analytics to help us understand how visitors use our site. Google Analytics uses cookies to collect information about your visit. You can learn more about how Google uses this information by visiting their Privacy & Terms site: <a href="https://policies.google.com/privacy" target="_blank">https://policies.google.com/privacy</a>.</p>
            
            <h2>5. Your Rights</h2>
            <p>Depending on your location, you may have certain rights regarding your personal information, such as the right to access, correct, or delete your personal information.</p>
            
            <h2>6. Changes to This Privacy Policy</h2>
            <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.</p>
            
            <h2>7. Contact Us</h2>
            <p>If you have any questions about this Privacy Policy, please contact us at [Your Contact Email].</p>
        </div>
    </section>
    
    <!-- Include your footer here -->
</body>
</html>
```

### Step 2: Add Cookie Consent Banner

Add this to your HTML:

```html
<div id="cookie-consent" class="cookie-banner">
    <div class="cookie-content">
        <p>This website uses cookies to ensure you get the best experience on our website.</p>
        <div class="cookie-buttons">
            <button id="cookie-accept" class="btn btn-primary">Accept</button>
            <a href="/privacy-policy.html" class="btn btn-secondary">Learn More</a>
        </div>
    </div>
</div>
```

Add this to your CSS:

```css
.cookie-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: var(--dark-color);
    color: var(--white);
    padding: var(--spacing-md);
    z-index: 1000;
    display: none;
}

.cookie-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.cookie-buttons {
    display: flex;
    gap: var(--spacing-sm);
}

@media (max-width: 768px) {
    .cookie-content {
        flex-direction: column;
        gap: var(--spacing-sm);
    }
}
```

Add this to your JavaScript:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const cookieConsent = document.getElementById('cookie-consent');
    const cookieAccept = document.getElementById('cookie-accept');
    
    // Check if user has already accepted cookies
    if (!localStorage.getItem('cookieConsent')) {
        cookieConsent.style.display = 'block';
    }
    
    cookieAccept.addEventListener('click', function() {
        localStorage.setItem('cookieConsent', 'true');
        cookieConsent.style.display = 'none';
    });
});
```

### Step 3: Update Your Analytics Code to Respect Cookie Consent

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Only load Google Analytics if user has consented
    if (localStorage.getItem('cookieConsent')) {
        // Google Analytics code here
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-XXXXXXXX');
    }
});
```

## Next Steps

After implementing these features:

1. **Test All Forms**: Submit test entries to ensure forms are working correctly
2. **Verify Analytics**: Check Google Analytics to ensure data is being collected
3. **Monitor Performance**: Use Google Analytics to track user engagement and conversion rates
4. **Optimize Based on Data**: Use the insights gained to improve your landing page