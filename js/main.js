/**
 * Legal Prejudice Analysis Landing Page JavaScript
 * Version: 1.0.0
 */

document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect
    const header = document.querySelector('.header');
    const scrollThreshold = 50;
    
    function handleScroll() {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
    
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check initial state
    
    // Mobile menu toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileMenuToggle && mainNav) {
        mobileMenuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    // Close mobile menu if open
                    if (mainNav && mainNav.classList.contains('active')) {
                        mainNav.classList.remove('active');
                        document.body.classList.remove('menu-open');
                    }
                    
                    // Calculate header height for offset
                    const headerHeight = header.offsetHeight;
                    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            if (email) {
                // Here you would typically send this to your backend
                // For now, we'll just show an alert
                alert(`Thank you for subscribing with ${email}! You'll receive updates about Legal Prejudice Analysis.`);
                emailInput.value = '';
            }
        });
    }
    
    // Create placeholder images if needed
    document.querySelectorAll('img[src="assets/logo.png"], img[src="assets/logo-white.png"]').forEach(img => {
        if (!img.complete || img.naturalHeight === 0) {
            createPlaceholderLogo(img);
        }
    });
    
    // Function to create placeholder logos
    function createPlaceholderLogo(img) {
        const isWhite = img.src.includes('logo-white.png');
        const canvas = document.createElement('canvas');
        canvas.width = 200;
        canvas.height = 50;
        
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = isWhite ? '#ffffff' : '#2c3e50';
        ctx.font = 'bold 24px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('LPA', canvas.width / 2, canvas.height / 2);
        
        img.src = canvas.toDataURL();
    }
    
    // Create placeholder for hero image if needed
    const heroImage = document.querySelector('.hero-image img');
    if (heroImage && (!heroImage.complete || heroImage.naturalHeight === 0)) {
        const canvas = document.createElement('canvas');
        canvas.width = 600;
        canvas.height = 400;
        
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = '#3498db';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 32px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('Legal Prejudice Analysis', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = '24px Arial';
        ctx.fillText('Dashboard Preview', canvas.width / 2, canvas.height / 2 + 20);
        
        heroImage.src = canvas.toDataURL();
    }
    
    // Create placeholders for feature images if needed
    document.querySelectorAll('.feature img').forEach((img, index) => {
        if (!img.complete || img.naturalHeight === 0) {
            const canvas = document.createElement('canvas');
            canvas.width = 400;
            canvas.height = 200;
            
            const ctx = canvas.getContext('2d');
            
            // Create different colored backgrounds for each feature
            const colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#1abc9c'];
            ctx.fillStyle = colors[index % colors.length];
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Add feature name
            const featureNames = [
                'Legal Framework',
                'Risk Analysis',
                'Practical Guide',
                'Risk Calculator',
                'API Integration',
                'Case Studies'
            ];
            
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 24px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(featureNames[index % featureNames.length], canvas.width / 2, canvas.height / 2);
            
            img.src = canvas.toDataURL();
        }
    });
});