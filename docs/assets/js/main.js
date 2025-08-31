/**
 * Legal Prejudice Analysis Documentation - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggle for mobile
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
    }
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        const isClickInsideSidebar = sidebar.contains(event.target);
        const isClickOnToggle = sidebarToggle.contains(event.target);
        
        if (!isClickInsideSidebar && !isClickOnToggle && sidebar.classList.contains('open')) {
            sidebar.classList.remove('open');
        }
    });
    
    // Submenu toggle
    const submenuItems = document.querySelectorAll('.has-submenu > .nav-link');
    
    submenuItems.forEach(function(item) {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const parent = this.parentElement;
            
            // Close all other open submenus
            const openItems = document.querySelectorAll('.has-submenu.open');
            openItems.forEach(function(openItem) {
                if (openItem !== parent) {
                    openItem.classList.remove('open');
                }
            });
            
            // Toggle current submenu
            parent.classList.toggle('open');
        });
    });
    
    // Auto-expand current page's parent menu
    const currentPageUrl = window.location.pathname;
    const currentLink = document.querySelector(`.nav-link[href="${currentPageUrl}"]`);
    
    if (currentLink) {
        currentLink.classList.add('active');
        
        // Find parent submenu if exists
        const parentSubmenu = currentLink.closest('.submenu');
        if (parentSubmenu) {
            const parentItem = parentSubmenu.closest('.has-submenu');
            parentItem.classList.add('open');
        }
    }
    
    // Print button functionality
    const printButton = document.getElementById('print-button');
    if (printButton) {
        printButton.addEventListener('click', function() {
            window.print();
        });
    }
    
    // Code highlighting is handled by Prism.js which is loaded separately
    
    // Handle anchor links with smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            
            // Skip if it's a submenu toggle
            if (this.parentElement.classList.contains('has-submenu')) {
                return;
            }
            
            if (targetId === '#') {
                e.preventDefault();
                return;
            }
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                e.preventDefault();
                
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update URL without page reload
                history.pushState(null, null, targetId);
            }
        });
    });
    
    // Handle external links
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        // Skip links that already have target attribute
        if (!link.getAttribute('target')) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
    
    // Add copy button to code blocks
    document.querySelectorAll('pre').forEach(block => {
        // Skip if already has copy button
        if (block.querySelector('.copy-button')) {
            return;
        }
        
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.title = 'Copy to clipboard';
        
        block.style.position = 'relative';
        block.appendChild(button);
        
        button.addEventListener('click', () => {
            const code = block.querySelector('code').innerText;
            navigator.clipboard.writeText(code).then(() => {
                button.innerHTML = '<i class="fas fa-check"></i>';
                button.classList.add('copied');
                
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                    button.classList.remove('copied');
                }, 2000);
            });
        });
    });
    
    // Add table of contents for long pages
    const headings = document.querySelectorAll('.content h2, .content h3');
    const contentElement = document.querySelector('.content');
    
    if (headings.length > 3 && contentElement) {
        const tocContainer = document.createElement('div');
        tocContainer.className = 'table-of-contents';
        tocContainer.innerHTML = '<h2>Table of Contents</h2><ul class="toc-list"></ul>';
        
        const tocList = tocContainer.querySelector('.toc-list');
        
        headings.forEach((heading, index) => {
            // Add ID to heading if it doesn't have one
            if (!heading.id) {
                heading.id = `heading-${index}`;
            }
            
            const listItem = document.createElement('li');
            listItem.className = heading.tagName.toLowerCase();
            
            const link = document.createElement('a');
            link.href = `#${heading.id}`;
            link.textContent = heading.textContent;
            
            listItem.appendChild(link);
            tocList.appendChild(listItem);
        });
        
        // Insert after first h1 or at the beginning
        const firstHeading = document.querySelector('.content h1');
        if (firstHeading) {
            firstHeading.after(tocContainer);
        } else {
            contentElement.prepend(tocContainer);
        }
    }
    
    // Handle responsive tables
    document.querySelectorAll('table').forEach(table => {
        if (!table.parentElement.classList.contains('table-responsive')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'table-responsive';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });
    
    // Add active class to current section based on scroll position
    function setActiveSection() {
        const sections = document.querySelectorAll('h2[id], h3[id]');
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (window.scrollY >= sectionTop - 100) {
                currentSection = section.getAttribute('id');
            }
        });
        
        if (currentSection) {
            // Remove active class from all TOC links
            document.querySelectorAll('.toc-list a').forEach(link => {
                link.classList.remove('active');
            });
            
            // Add active class to current section link
            const activeLink = document.querySelector(`.toc-list a[href="#${currentSection}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    }
    
    // Update active section on scroll
    window.addEventListener('scroll', setActiveSection);
    
    // Initialize active section
    setActiveSection();
});