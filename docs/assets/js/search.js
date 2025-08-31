/**
 * Legal Prejudice Analysis Documentation - Search Functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const searchResults = document.getElementById('search-results');
    
    // Search index - this would normally be generated from all documentation pages
    // For now, we'll create a simple index with sample data
    const searchIndex = [
        {
            title: 'Legal Prejudice Analysis Framework',
            url: 'framework/index.html',
            content: 'The foundational component that establishes definitions, standards, and methodology based on statutory provisions (28 U.S.C. §§ 455, 144) and key Supreme Court precedents.'
        },
        {
            title: 'Legal Standards for Prejudice',
            url: 'framework/legal-standards.html',
            content: 'Detailed analysis of statutory provisions including 28 U.S.C. §§ 455, 144 and their interpretation in judicial proceedings.'
        },
        {
            title: 'Key Supreme Court Precedents',
            url: 'framework/precedents.html',
            content: 'Analysis of key Supreme Court cases including Liteky v. United States and Caperton v. A.T. Massey Coal Co. that establish standards for judicial prejudice.'
        },
        {
            title: 'Evaluation Methodology',
            url: 'framework/methodology.html',
            content: 'Structured approach to evaluating potential prejudice in legal proceedings, including factor identification and assessment.'
        },
        {
            title: 'Risk Analysis Overview',
            url: 'risk-analysis/index.html',
            content: 'The quantitative component that provides methods for evaluating the likelihood and impact of prejudicial factors.'
        },
        {
            title: 'Quantitative Methods',
            url: 'risk-analysis/quantitative-methods.html',
            content: 'Statistical and mathematical approaches to quantifying prejudice risk, including likelihood ratio analysis and Monte Carlo simulations.'
        },
        {
            title: 'Probability Analysis',
            url: 'risk-analysis/probability.html',
            content: 'Bayesian probability framework for updating prejudice assessments as new evidence emerges.'
        },
        {
            title: 'Risk Matrices',
            url: 'risk-analysis/risk-matrices.html',
            content: 'Visual tools for mapping prejudice factors based on likelihood and impact, with categorization into risk levels.'
        },
        {
            title: 'Practical Implementation Guide',
            url: 'practical-guide/index.html',
            content: 'The implementation component that offers worksheets, checklists, and decision matrices for immediate application in legal practice.'
        },
        {
            title: '48-hour Triage Protocol',
            url: 'practical-guide/triage-protocol.html',
            content: 'Step-by-step process for rapidly assessing potential prejudice within the critical 48-hour window after discovery.'
        },
        {
            title: 'Strategic Response Options',
            url: 'practical-guide/response-options.html',
            content: 'Detailed strategies for responding to different types and levels of potential prejudice, with decision frameworks.'
        },
        {
            title: 'Documentation Templates',
            url: 'practical-guide/templates.html',
            content: 'Ready-to-use templates for documenting prejudice concerns, tracking incidents, and preparing formal submissions.'
        },
        {
            title: 'Case Studies Overview',
            url: 'case-studies/index.html',
            content: 'The applied component that demonstrates the framework in action through detailed analysis of example scenarios.'
        },
        {
            title: 'Case Study 1: Relationship-Based Prejudice',
            url: 'case-studies/case1.html',
            content: 'Analysis of a case involving potential prejudice based on prior relationships between judge and litigants.'
        },
        {
            title: 'Case Study 2: Conduct-Based Prejudice',
            url: 'case-studies/case2.html',
            content: 'Examination of a case involving potential prejudice based on judicial conduct during proceedings.'
        },
        {
            title: 'Common Prejudice Patterns',
            url: 'case-studies/patterns.html',
            content: 'Identification of recurring patterns in prejudice cases and effective response strategies.'
        },
        {
            title: 'API Documentation',
            url: 'api/index.html',
            content: 'Overview of the Legal Prejudice Analysis API for integrating the framework into software systems.'
        },
        {
            title: 'Authentication',
            url: 'api/authentication.html',
            content: 'Methods for authenticating with the API, including API keys and OAuth implementation.'
        },
        {
            title: 'API Endpoints',
            url: 'api/endpoints.html',
            content: 'Comprehensive listing of all API endpoints with request and response formats.'
        },
        {
            title: 'Webhooks',
            url: 'api/webhooks.html',
            content: 'Implementation guide for webhook integration to receive real-time notifications of prejudice assessments.'
        },
        {
            title: 'Integration Overview',
            url: 'integration/index.html',
            content: 'Guide to integrating the Legal Prejudice Analysis framework with existing legal practice systems.'
        },
        {
            title: 'Clio Integration',
            url: 'integration/clio.html',
            content: 'Step-by-step guide for integrating with the Clio case management system.'
        },
        {
            title: 'Practice Panther Integration',
            url: 'integration/practice-panther.html',
            content: 'Implementation guide for connecting with Practice Panther practice management software.'
        },
        {
            title: 'Custom Integrations',
            url: 'integration/custom.html',
            content: 'Framework for developing custom integrations with proprietary or specialized legal software.'
        }
    ];
    
    // Function to perform search
    function performSearch(query) {
        // Clear previous results
        searchResults.innerHTML = '';
        
        if (!query.trim()) {
            searchResults.style.display = 'none';
            return;
        }
        
        // Convert query to lowercase for case-insensitive matching
        const lowerQuery = query.toLowerCase();
        
        // Filter search index
        const results = searchIndex.filter(item => {
            return (
                item.title.toLowerCase().includes(lowerQuery) ||
                item.content.toLowerCase().includes(lowerQuery)
            );
        });
        
        // Display results
        if (results.length > 0) {
            results.forEach(result => {
                const resultItem = document.createElement('div');
                resultItem.className = 'search-result-item';
                
                const resultLink = document.createElement('a');
                resultLink.href = result.url;
                resultLink.innerHTML = `<strong>${result.title}</strong>`;
                
                const resultContent = document.createElement('p');
                
                // Create a snippet with highlighted query
                let snippet = result.content;
                if (snippet.length > 150) {
                    // Find the position of the query in the content
                    const queryPosition = result.content.toLowerCase().indexOf(lowerQuery);
                    
                    // Create a snippet around the query
                    const startPos = Math.max(0, queryPosition - 60);
                    const endPos = Math.min(result.content.length, queryPosition + 90);
                    
                    snippet = '...' + result.content.substring(startPos, endPos) + '...';
                }
                
                // Highlight the query in the snippet
                const highlightedSnippet = snippet.replace(
                    new RegExp(query, 'gi'),
                    match => `<mark>${match}</mark>`
                );
                
                resultContent.innerHTML = highlightedSnippet;
                
                resultItem.appendChild(resultLink);
                resultItem.appendChild(resultContent);
                searchResults.appendChild(resultItem);
            });
            
            searchResults.style.display = 'block';
        } else {
            const noResults = document.createElement('div');
            noResults.className = 'search-result-item';
            noResults.textContent = 'No results found.';
            searchResults.appendChild(noResults);
            searchResults.style.display = 'block';
        }
    }
    
    // Search input event handler
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            performSearch(this.value);
        });
        
        // Handle Enter key
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                performSearch(this.value);
            }
        });
    }
    
    // Search button event handler
    if (searchButton) {
        searchButton.addEventListener('click', function() {
            performSearch(searchInput.value);
        });
    }
    
    // Close search results when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInsideSearch = searchInput.contains(event.target) || 
                                   searchButton.contains(event.target) || 
                                   searchResults.contains(event.target);
        
        if (!isClickInsideSearch && searchResults.style.display === 'block') {
            searchResults.style.display = 'none';
        }
    });
    
    // Initialize search if URL has search parameter
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('search');
    
    if (searchQuery && searchInput) {
        searchInput.value = searchQuery;
        performSearch(searchQuery);
    }
});