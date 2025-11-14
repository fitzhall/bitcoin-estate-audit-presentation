#!/usr/bin/env python3
import os
import re
import markdown
import html

def convert_markdown_to_html_content(markdown_text):
    """Convert markdown to HTML while preserving structure"""
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br', 'extra'])
    html_content = md.convert(markdown_text)
    
    # Add Bootstrap classes to tables
    html_content = html_content.replace('<table>', '<table class="table-auto w-full mb-8 border-collapse">')
    html_content = html_content.replace('<th>', '<th class="border px-4 py-2 bg-gray-100 font-semibold text-left">')
    html_content = html_content.replace('<td>', '<td class="border px-4 py-2">')
    
    # Add styling to blockquotes
    html_content = html_content.replace('<blockquote>', '<blockquote class="border-l-4 border-bitcoin-gold pl-4 italic my-6 text-gray-700">')
    
    # Style code blocks
    html_content = html_content.replace('<code>', '<code class="bg-gray-100 px-2 py-1 rounded text-sm">')
    
    # Add IDs to headers for navigation
    def add_header_ids(match):
        level = match.group(1)
        content = match.group(2)
        # Create ID from header text
        header_id = re.sub(r'[^\w\s-]', '', content.lower())
        header_id = re.sub(r'[-\s]+', '-', header_id)
        return f'<h{level} id="{header_id}" class="scroll-mt-20">{content}</h{level}>'
    
    html_content = re.sub(r'<h(\d)>(.*?)</h\1>', add_header_ids, html_content)
    
    return html_content

def extract_title_from_filename(filename):
    """Extract title from filename"""
    # Remove number prefix and file extension
    name = re.sub(r'^\d+_', '', filename)
    name = re.sub(r'\.md$', '', name)
    name = name.replace('_', ' ')
    
    # Map filenames to proper titles
    title_map = {
        'Bitcoin Estate Planning Assessment Checklist': 'Bitcoin Estate Planning Assessment Checklist',
        'Bitcoin Security Implementation Framework': 'Bitcoin Security Implementation Framework',
        'Bitcoin Estate Planning Document Templates': 'Bitcoin Estate Planning Document Templates',
        'Bitcoin Tax Planning Compliance Toolkit': 'Bitcoin Tax Planning & Compliance Toolkit',
        'Bitcoin Family Education Training Program': 'Bitcoin Family Education & Training Program',
        'Bitcoin Professional Coordination Framework': 'Bitcoin Professional Coordination Framework',
        'Bitcoin Emergency Response Disaster Recovery Procedures': 'Bitcoin Emergency Response & Disaster Recovery',
        'Bitcoin Performance Monitoring Optimization System': 'Bitcoin Performance Monitoring & Optimization',
        'Bitcoin Client Onboarding Assessment Procedures': 'Bitcoin Client Onboarding & Assessment',
        'Bitcoin Implementation Roadmap Project Management System': 'Bitcoin Implementation Roadmap & Project Management'
    }
    
    for key, value in title_map.items():
        if key in name:
            return value
    
    return name

def create_tool_url(title):
    """Create URL-friendly version of title"""
    url = title.lower()
    url = re.sub(r'[^\w\s-]', '', url)
    url = re.sub(r'[-\s]+', '-', url)
    return url

def create_tool_page_template(title, content):
    """Create a full HTML page for a tool/template"""
    url_title = create_tool_url(title)
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Bitcoin Estate Planning Tools | Firm6102</title>
    <meta name="description" content="Professional {title}. Comprehensive tools, templates, and frameworks for Bitcoin estate planning implementation. Ready-to-use resources for professionals and families.">
    
    <!-- SEO Meta Tags -->
    <meta property="og:title" content="{title} - Professional Tools">
    <meta property="og:description" content="Complete {title} with ready-to-use templates, checklists, and implementation frameworks for Bitcoin estate planning.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://firm6102.com/tools/{url_title}/">
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}: Professional Tools & Templates",
      "description": "Comprehensive {title} including templates, checklists, and implementation frameworks.",
      "author": {{
        "@type": "Organization",
        "name": "Firm6102"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Firm6102",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://firm6102.com/images/logo.png"
        }}
      }},
      "datePublished": "2025-01-14",
      "dateModified": "2025-01-14"
    }}
    </script>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Custom Tailwind Config -->
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'deep-navy': '#1a2332',
                        'bitcoin-gold': '#f7931a',
                        'charcoal': '#2c3e50',
                        'light-gray': '#f8f9fa',
                        'accent-silver': '#95a5a6'
                    }},
                    fontFamily: {{
                        'display': ['Playfair Display', 'Georgia', 'serif'],
                        'sans': ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif']
                    }}
                }}
            }}
        }}
    </script>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;600;700;900&display=swap" rel="stylesheet">
    
    <!-- Custom Styles -->
    <style>
        .hero-gradient {{
            background: linear-gradient(135deg, #1a2332 0%, #2c3e50 100%);
        }}
        .nav-blur {{
            backdrop-filter: blur(10px);
            background-color: rgba(255, 255, 255, 0.9);
        }}
        .prose h2 {{
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            font-size: 2rem;
            font-weight: 700;
            color: #1a2332;
            font-family: 'Playfair Display', Georgia, serif;
        }}
        .prose h3 {{
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
            font-weight: 600;
            color: #1a2332;
        }}
        .prose ul {{
            list-style-type: disc;
            padding-left: 1.5rem;
        }}
        .prose ol {{
            list-style-type: decimal;
            padding-left: 1.5rem;
        }}
        .prose li {{
            margin-bottom: 0.5rem;
        }}
        .prose p {{
            margin-bottom: 1.25rem;
            line-height: 1.8;
        }}
        .prose strong {{
            font-weight: 600;
            color: #1a2332;
        }}
        .toc-link {{
            transition: all 0.2s ease;
        }}
        .toc-link:hover {{
            color: #f7931a;
            padding-left: 0.5rem;
        }}
        .tool-box {{
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}
        .checklist-item {{
            display: flex;
            align-items: start;
            margin-bottom: 0.75rem;
        }}
        .checklist-item input[type="checkbox"] {{
            margin-right: 0.75rem;
            margin-top: 0.25rem;
        }}
    </style>
</head>
<body class="font-sans text-charcoal">
    <!-- Navigation -->
    <nav class="fixed top-0 left-0 right-0 z-50 nav-blur border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <a href="/" class="text-2xl font-bold text-deep-navy">
                        FIRM<span class="text-bitcoin-gold">6102</span>
                    </a>
                </div>
                
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/about" class="text-gray-700 hover:text-bitcoin-gold transition-colors">About</a>
                    <a href="/services/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Services</a>
                    <a href="/states/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">State Guides</a>
                    <a href="/wealth/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Wealth Guides</a>
                    <a href="/professionals/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">For Professionals</a>
                    <a href="/tools/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Tools & Templates</a>
                    <a href="/keep-protocol/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">KEEP Protocol</a>
                    <a href="/learn/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Learn</a>
                    <a href="/consultation" class="ml-4 px-6 py-2 bg-bitcoin-gold text-white rounded-lg hover:bg-orange-600 transition-colors">
                        Schedule Consultation
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="pt-20 pb-4 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <nav class="text-sm">
                <a href="/" class="text-gray-500 hover:text-bitcoin-gold">Home</a>
                <span class="mx-2 text-gray-400">/</span>
                <a href="/tools/" class="text-gray-500 hover:text-bitcoin-gold">Tools & Templates</a>
                <span class="mx-2 text-gray-400">/</span>
                <span class="text-deep-navy font-semibold">{title}</span>
            </nav>
        </div>
    </div>

    <!-- Article Header -->
    <header class="hero-gradient py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <div class="text-bitcoin-gold font-semibold mb-4">PROFESSIONAL TOOLS</div>
                <h1 class="text-4xl md:text-5xl font-display font-bold text-white mb-6">
                    {title}
                </h1>
                <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                    Ready-to-use tools, templates, and frameworks for Bitcoin estate planning implementation
                </p>
                <div class="flex items-center justify-center space-x-6 text-gray-400 text-sm mt-6">
                    <span>By Firm6102 Experts</span>
                    <span>•</span>
                    <span>Professional Grade</span>
                    <span>•</span>
                    <span>Last updated: January 2025</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Download CTA -->
    <div class="bg-bitcoin-gold text-white py-4">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="font-semibold">Download complete templates and tools as PDF • Available for Firm6102 clients</p>
        </div>
    </div>

    <!-- Article Content -->
    <article class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-4 gap-12">
                <!-- Table of Contents Sidebar -->
                <aside class="lg:col-span-1">
                    <div class="sticky top-24">
                        <h3 class="text-lg font-semibold text-deep-navy mb-4">Table of Contents</h3>
                        <nav class="space-y-2 text-sm" id="table-of-contents">
                            <!-- TOC will be populated by JavaScript -->
                        </nav>
                        
                        <!-- Quick Actions -->
                        <div class="mt-8 p-4 bg-gray-100 rounded-lg">
                            <h4 class="font-semibold text-deep-navy mb-3">Quick Actions</h4>
                            <a href="/consultation" class="block w-full py-2 px-4 bg-bitcoin-gold text-white text-center rounded hover:bg-orange-600 transition-colors mb-2">
                                Get Professional Help
                            </a>
                            <a href="/tools/" class="block w-full py-2 px-4 bg-deep-navy text-white text-center rounded hover:bg-charcoal transition-colors">
                                View All Tools
                            </a>
                        </div>
                    </div>
                </aside>
                
                <!-- Main Content -->
                <div class="lg:col-span-3 prose prose-lg max-w-none">
                    {content}
                    
                    <!-- CTA Section -->
                    <div class="mt-16 p-8 bg-gradient-to-r from-deep-navy to-charcoal text-white rounded-2xl">
                        <h3 class="text-2xl font-display font-bold mb-4 text-white">Need Professional Implementation?</h3>
                        <p class="mb-6 text-gray-200">Our experts can help you implement these tools and templates for your specific Bitcoin estate planning needs.</p>
                        <div class="flex flex-col sm:flex-row gap-4">
                            <a href="/consultation" class="inline-block px-8 py-3 bg-bitcoin-gold text-white font-semibold rounded-lg hover:bg-orange-600 transition-colors text-center">
                                Schedule Consultation
                            </a>
                            <a href="/tools/" class="inline-block px-8 py-3 bg-transparent text-white font-semibold rounded-lg border-2 border-white hover:bg-white hover:text-deep-navy transition-colors text-center">
                                Explore More Tools
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </article>

    <!-- Related Tools -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-display font-bold text-deep-navy mb-8 text-center">Related Tools & Templates</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <a href="/tools/bitcoin-estate-planning-assessment-checklist/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">Assessment Checklist</h3>
                    <p class="text-gray-600">Comprehensive evaluation framework for Bitcoin estate planning.</p>
                </a>
                <a href="/tools/bitcoin-security-implementation-framework/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">Security Framework</h3>
                    <p class="text-gray-600">Multi-signature and hardware wallet implementation guides.</p>
                </a>
                <a href="/tools/bitcoin-estate-planning-document-templates/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">Document Templates</h3>
                    <p class="text-gray-600">Complete legal document templates for Bitcoin estate planning.</p>
                </a>
            </div>
            <div class="text-center mt-8">
                <a href="/tools/" class="inline-block px-8 py-3 bg-bitcoin-gold text-white font-semibold rounded-lg hover:bg-orange-600 transition-colors">
                    View All Tools & Templates
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-deep-navy text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8 mb-8">
                <div class="md:col-span-1">
                    <div class="text-2xl font-bold mb-4">
                        FIRM<span class="text-bitcoin-gold">6102</span>
                    </div>
                    <p class="text-gray-400 text-sm">
                        Architects of Sovereign Wealth in the Digital Age
                    </p>
                </div>
                
                <div>
                    <h4 class="font-semibold mb-4">Services</h4>
                    <ul class="space-y-2 text-gray-400 text-sm">
                        <li><a href="/services/bitcoin-estate-planning" class="hover:text-bitcoin-gold transition-colors">Estate Planning</a></li>
                        <li><a href="/keep-protocol/" class="hover:text-bitcoin-gold transition-colors">KEEP Protocol</a></li>
                        <li><a href="/services/family-office" class="hover:text-bitcoin-gold transition-colors">Family Office</a></li>
                        <li><a href="/services/corporate-treasury" class="hover:text-bitcoin-gold transition-colors">Corporate Treasury</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-semibold mb-4">Resources</h4>
                    <ul class="space-y-2 text-gray-400 text-sm">
                        <li><a href="/states/" class="hover:text-bitcoin-gold transition-colors">State Guides</a></li>
                        <li><a href="/wealth/" class="hover:text-bitcoin-gold transition-colors">Wealth Guides</a></li>
                        <li><a href="/professionals/" class="hover:text-bitcoin-gold transition-colors">For Professionals</a></li>
                        <li><a href="/tools/" class="hover:text-bitcoin-gold transition-colors">Tools & Templates</a></li>
                        <li><a href="/learn/" class="hover:text-bitcoin-gold transition-colors">Knowledge Center</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-semibold mb-4">Company</h4>
                    <ul class="space-y-2 text-gray-400 text-sm">
                        <li><a href="/about" class="hover:text-bitcoin-gold transition-colors">About Us</a></li>
                        <li><a href="/contact" class="hover:text-bitcoin-gold transition-colors">Contact</a></li>
                        <li><a href="/privacy" class="hover:text-bitcoin-gold transition-colors">Privacy Policy</a></li>
                        <li><a href="/terms" class="hover:text-bitcoin-gold transition-colors">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-700 pt-8 text-center text-gray-400 text-sm">
                <p>&copy; 2025 Firm6102. All rights reserved. | Professional Bitcoin Estate Planning Services</p>
            </div>
        </div>
    </footer>
    
    <!-- Table of Contents Script -->
    <script>
        // Generate table of contents
        document.addEventListener('DOMContentLoaded', function() {{
            const toc = document.getElementById('table-of-contents');
            const headings = document.querySelectorAll('.prose h2');
            
            headings.forEach(heading => {{
                const link = document.createElement('a');
                link.href = '#' + heading.id;
                link.textContent = heading.textContent;
                link.className = 'block py-1 text-gray-600 hover:text-bitcoin-gold toc-link';
                
                // Smooth scroll
                link.addEventListener('click', function(e) {{
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {{
                        target.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }});
                
                toc.appendChild(link);
            }});
            
            // Highlight active section
            const observer = new IntersectionObserver(entries => {{
                entries.forEach(entry => {{
                    const id = entry.target.getAttribute('id');
                    const link = document.querySelector(`a[href="#${{id}}"]`);
                    if (link) {{
                        if (entry.isIntersecting) {{
                            link.classList.add('text-bitcoin-gold', 'font-semibold');
                            link.classList.remove('text-gray-600');
                        }} else {{
                            link.classList.remove('text-bitcoin-gold', 'font-semibold');
                            link.classList.add('text-gray-600');
                        }}
                    }}
                }});
            }}, {{ rootMargin: '-100px 0px -70% 0px' }});
            
            headings.forEach(heading => observer.observe(heading));
        }});
    </script>
</body>
</html>'''
    
    return template.format(
        title=title,
        url_title=url_title,
        content=content
    )

def process_tool_files():
    """Process all tool/template markdown files and create HTML pages"""
    content_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/Website Content/Firm6102_Content_Batches 4/Batch4_Tools_Templates"
    output_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/website/tools"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files
    tool_files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    tool_files.sort()  # Sort to maintain order
    
    processed_pages = []
    
    for tool_file in tool_files:
        # Extract title
        title = extract_title_from_filename(tool_file)
        url_title = create_tool_url(title)
        
        # Create tool directory
        page_dir = os.path.join(output_dir, url_title)
        os.makedirs(page_dir, exist_ok=True)
        
        # Read markdown file
        input_path = os.path.join(content_dir, tool_file)
        output_path = os.path.join(page_dir, "index.html")
        
        print(f"Processing {title}...")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Remove the title (first # heading) as it's in the template
            markdown_content = re.sub(r'^#[^#].*?\n', '', markdown_content, count=1)
            
            # Convert to HTML
            html_content = convert_markdown_to_html_content(markdown_content)
            
            # Create full page
            full_page = create_tool_page_template(title, html_content)
            
            # Write output
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_page)
            
            processed_pages.append({
                'title': title,
                'url': url_title,
                'file': tool_file
            })
            
            print(f"✓ Created {title} page at tools/{url_title}/")
            
        except Exception as e:
            print(f"✗ Error processing {tool_file}: {str(e)}")
    
    return processed_pages

if __name__ == "__main__":
    print("Converting tool and template files to HTML...")
    processed = process_tool_files()
    print(f"\nConversion complete! Processed {len(processed)} tools and templates.")
    print("\nProcessed pages:")
    for page in processed:
        print(f"  - {page['title']}: /tools/{page['url']}/")