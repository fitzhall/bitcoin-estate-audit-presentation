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
    
    # Special handling for different titles
    if '100K_500K' in filename:
        return 'Bitcoin Estate Planning for $100K-$500K'
    elif '500K_1M' in filename:
        return 'Bitcoin Estate Planning for $500K-$1M'
    elif '1M_2M' in filename:
        return 'Bitcoin Estate Planning for $1M-$2M'
    elif '2M_5M' in filename:
        return 'Bitcoin Estate Planning for $2M-$5M'
    elif '5M_10M' in filename:
        return 'Bitcoin Estate Planning for $5M-$10M'
    elif '10M_Plus' in filename:
        return 'Bitcoin Estate Planning for $10M+'
    elif 'Inheritance' in filename:
        return 'Bitcoin Inheritance Planning'
    elif 'Business_Owner' in filename:
        return 'Business Owner Bitcoin Estate Planning'
    elif 'Young_Professional' in filename:
        return 'Young Professional Bitcoin Estate Planning'
    elif 'Retirement' in filename:
        return 'Retirement Bitcoin Estate Planning'
    
    return name

def create_wealth_url(title):
    """Create URL-friendly version of title"""
    url = title.lower()
    url = re.sub(r'[^\w\s-]', '', url)
    url = re.sub(r'[-\s]+', '-', url)
    return url

def create_wealth_page_template(title, content):
    """Create a full HTML page for a wealth guide"""
    url_title = create_wealth_url(title)
    
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Complete Guide | Firm6102</title>
    <meta name="description" content="Expert guidance on {title}. Discover strategies, tax optimization, trust structures, and professional planning for your specific wealth level.">
    
    <!-- SEO Meta Tags -->
    <meta property="og:title" content="{title} - Complete Guide">
    <meta property="og:description" content="Comprehensive guide to {title} with expert strategies, real case studies, and actionable implementation plans.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://firm6102.com/wealth/{url_title}/">
    
    <!-- Schema.org Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}: Complete Guide",
      "description": "Comprehensive guide to {title} including strategies, trust structures, and professional guidance.",
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
      "datePublished": "2025-01-13",
      "dateModified": "2025-01-13"
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
                    <a href="/keep-protocol/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">KEEP Protocol</a>
                    <a href="/learn/" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Learn</a>
                    <a href="/contact" class="text-gray-700 hover:text-bitcoin-gold transition-colors">Contact</a>
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
                <a href="/wealth/" class="text-gray-500 hover:text-bitcoin-gold">Wealth Guides</a>
                <span class="mx-2 text-gray-400">/</span>
                <span class="text-deep-navy font-semibold">{title}</span>
            </nav>
        </div>
    </div>

    <!-- Article Header -->
    <header class="hero-gradient py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <div class="text-bitcoin-gold font-semibold mb-4">WEALTH-SPECIFIC GUIDE</div>
                <h1 class="text-4xl md:text-5xl font-display font-bold text-white mb-6">
                    {title}
                </h1>
                <p class="text-xl text-gray-300 max-w-3xl mx-auto">
                    Expert strategies, real case studies, and actionable guidance for securing your Bitcoin wealth
                </p>
                <div class="flex items-center justify-center space-x-6 text-gray-400 text-sm mt-6">
                    <span>By Firm6102 Experts</span>
                    <span>•</span>
                    <span>25 min read</span>
                    <span>•</span>
                    <span>Last updated: January 2025</span>
                </div>
            </div>
        </div>
    </header>

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
                    </div>
                </aside>
                
                <!-- Main Content -->
                <div class="lg:col-span-3 prose prose-lg max-w-none">
                    {content}
                    
                    <!-- CTA Section -->
                    <div class="mt-16 p-8 bg-gradient-to-r from-deep-navy to-charcoal text-white rounded-2xl">
                        <h3 class="text-2xl font-display font-bold mb-4 text-white">Ready to Secure Your Bitcoin Legacy?</h3>
                        <p class="mb-6 text-gray-200">Our experts specialize in Bitcoin estate planning for your specific wealth level. Get personalized guidance tailored to your unique situation.</p>
                        <div class="flex flex-col sm:flex-row gap-4">
                            <a href="/consultation" class="inline-block px-8 py-3 bg-bitcoin-gold text-white font-semibold rounded-lg hover:bg-orange-600 transition-colors text-center">
                                Schedule a Consultation
                            </a>
                            <a href="/wealth/" class="inline-block px-8 py-3 bg-transparent text-white font-semibold rounded-lg border-2 border-white hover:bg-white hover:text-deep-navy transition-colors text-center">
                                Explore Other Wealth Levels
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </article>

    <!-- Related Wealth Guides -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-display font-bold text-deep-navy mb-8 text-center">Explore Other Wealth Guides</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <a href="/wealth/bitcoin-estate-planning-for-100k-500k/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">$100K-$500K</h3>
                    <p class="text-gray-600">Starting your Bitcoin wealth journey with smart estate planning.</p>
                </a>
                <a href="/wealth/bitcoin-estate-planning-for-1m-2m/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">$1M-$2M</h3>
                    <p class="text-gray-600">Advanced strategies for serious Bitcoin wealth protection.</p>
                </a>
                <a href="/wealth/bitcoin-estate-planning-for-5m-10m/" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">$5M-$10M</h3>
                    <p class="text-gray-600">Elite dynasty planning for multi-generational wealth.</p>
                </a>
            </div>
            <div class="text-center mt-8">
                <a href="/wealth/" class="inline-block px-8 py-3 bg-bitcoin-gold text-white font-semibold rounded-lg hover:bg-orange-600 transition-colors">
                    View All Wealth Guides
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
                    <h4 class="font-semibold mb-4">Learn More</h4>
                    <ul class="space-y-2 text-gray-400 text-sm">
                        <li><a href="/about" class="hover:text-bitcoin-gold transition-colors">About Us</a></li>
                        <li><a href="/states/" class="hover:text-bitcoin-gold transition-colors">State Guides</a></li>
                        <li><a href="/wealth/" class="hover:text-bitcoin-gold transition-colors">Wealth Guides</a></li>
                        <li><a href="/learn/" class="hover:text-bitcoin-gold transition-colors">Knowledge Center</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-semibold mb-4">Legal</h4>
                    <ul class="space-y-2 text-gray-400 text-sm">
                        <li><a href="/privacy" class="hover:text-bitcoin-gold transition-colors">Privacy Policy</a></li>
                        <li><a href="/terms" class="hover:text-bitcoin-gold transition-colors">Terms of Service</a></li>
                        <li><a href="/disclaimer" class="hover:text-bitcoin-gold transition-colors">Disclaimer</a></li>
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

def process_wealth_files():
    """Process all wealth markdown files and create HTML pages"""
    content_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/Website Content/Firm6102_Content_Batches 2/Batch2_Asset_Sizes"
    output_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/website/wealth"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files
    wealth_files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    wealth_files.sort()  # Sort to maintain order
    
    processed_pages = []
    
    for wealth_file in wealth_files:
        # Extract title
        title = extract_title_from_filename(wealth_file)
        url_title = create_wealth_url(title)
        
        # Create wealth directory
        page_dir = os.path.join(output_dir, url_title)
        os.makedirs(page_dir, exist_ok=True)
        
        # Read markdown file
        input_path = os.path.join(content_dir, wealth_file)
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
            full_page = create_wealth_page_template(title, html_content)
            
            # Write output
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_page)
            
            processed_pages.append({
                'title': title,
                'url': url_title,
                'file': wealth_file
            })
            
            print(f"✓ Created {title} page at wealth/{url_title}/")
            
        except Exception as e:
            print(f"✗ Error processing {wealth_file}: {str(e)}")
    
    return processed_pages

if __name__ == "__main__":
    print("Converting wealth guide files to HTML...")
    processed = process_wealth_files()
    print(f"\nConversion complete! Processed {len(processed)} wealth guides.")
    print("\nProcessed pages:")
    for page in processed:
        print(f"  - {page['title']}: /wealth/{page['url']}/")