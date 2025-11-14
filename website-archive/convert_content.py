#!/usr/bin/env python3
import os
import re
import markdown
import html

def convert_markdown_to_html_content(markdown_text):
    """Convert markdown to HTML while preserving structure"""
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
    html_content = md.convert(markdown_text)
    
    # Add Bootstrap classes to tables
    html_content = html_content.replace('<table>', '<table class="table-auto w-full mb-8">')
    
    # Add styling to blockquotes
    html_content = html_content.replace('<blockquote>', '<blockquote class="border-l-4 border-bitcoin-gold pl-4 italic my-6">')
    
    # Style code blocks
    html_content = html_content.replace('<code>', '<code class="bg-gray-100 px-2 py-1 rounded text-sm">')
    
    # Add IDs to headers for navigation
    def add_header_ids(match):
        level = match.group(1)
        content = match.group(2)
        # Create ID from header text
        header_id = re.sub(r'[^\w\s-]', '', content.lower())
        header_id = re.sub(r'[-\s]+', '-', header_id)
        return f'<h{level} id="{header_id}">{content}</h{level}>'
    
    html_content = re.sub(r'<h(\d)>(.*?)</h\1>', add_header_ids, html_content)
    
    return html_content

def create_article_template(title, description, content, read_time="30 min"):
    """Create a full HTML page for an article"""
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Firm6102</title>
    <meta name="description" content="{description}">
    
    <!-- SEO Meta Tags -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    
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
                    }},
                    typography: {{
                        DEFAULT: {{
                            css: {{
                                color: '#2c3e50',
                                h1: {{
                                    color: '#1a2332',
                                    fontFamily: 'Playfair Display, Georgia, serif',
                                    fontWeight: '700',
                                }},
                                h2: {{
                                    color: '#1a2332',
                                    fontFamily: 'Playfair Display, Georgia, serif',
                                    fontWeight: '600',
                                    marginTop: '3rem',
                                    marginBottom: '1.5rem',
                                }},
                                h3: {{
                                    color: '#1a2332',
                                    fontWeight: '600',
                                    marginTop: '2rem',
                                    marginBottom: '1rem',
                                }},
                                a: {{
                                    color: '#f7931a',
                                    textDecoration: 'none',
                                    '&:hover': {{
                                        color: '#d97d00',
                                    }},
                                }},
                                blockquote: {{
                                    borderLeftColor: '#f7931a',
                                    fontStyle: 'italic',
                                }},
                                'ul > li::before': {{
                                    backgroundColor: '#f7931a',
                                }},
                            }},
                        }},
                    }},
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
        }}
        .prose h3 {{
            margin-top: 2rem;
            margin-bottom: 1rem;
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

    <!-- Article Header -->
    <header class="hero-gradient pt-24 pb-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <div class="text-bitcoin-gold font-semibold mb-4">COMPREHENSIVE GUIDE</div>
                <h1 class="text-4xl md:text-5xl font-display font-bold text-white mb-6">
                    {title}
                </h1>
                <div class="flex items-center justify-center space-x-6 text-gray-400 text-sm">
                    <span>By Firm6102 Experts</span>
                    <span>•</span>
                    <span>{read_time} read</span>
                    <span>•</span>
                    <span>Last updated: January 2025</span>
                </div>
            </div>
        </div>
    </header>

    <!-- Article Content -->
    <article class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="prose prose-lg max-w-none">
                {content}
                
                <div class="mt-16 p-8 bg-gradient-to-r from-deep-navy to-charcoal text-white rounded-2xl">
                    <h3 class="text-2xl font-display font-bold mb-4 text-white">Ready to Implement These Strategies?</h3>
                    <p class="mb-6 text-gray-200">Our experts can guide you through implementing these strategies for your specific situation.</p>
                    <a href="/consultation" class="inline-block px-8 py-3 bg-bitcoin-gold text-white font-semibold rounded-lg hover:bg-orange-600 transition-colors">
                        Schedule a Consultation
                    </a>
                </div>
            </div>
        </div>
    </article>

    <!-- Related Articles -->
    <section class="py-16 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-display font-bold text-deep-navy mb-8 text-center">Related Guides</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <a href="/learn/executive-order-6102" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">Executive Order 6102: Bitcoin Lessons</h3>
                    <p class="text-gray-600">Learn from history's most significant wealth confiscation.</p>
                </a>
                <a href="/learn/bitcoin-estate-planning" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">Bitcoin Estate Planning Guide</h3>
                    <p class="text-gray-600">Strategies for multi-generational wealth transfer.</p>
                </a>
                <a href="/learn/keep-protocol-standards" class="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow">
                    <h3 class="text-xl font-semibold text-deep-navy mb-2">KEEP Protocol Standards</h3>
                    <p class="text-gray-600">Professional certification framework.</p>
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
                        <li><a href="/learn/" class="hover:text-bitcoin-gold transition-colors">Knowledge Center</a></li>
                        <li><a href="/consultation" class="hover:text-bitcoin-gold transition-colors">Schedule Consultation</a></li>
                        <li><a href="/contact" class="hover:text-bitcoin-gold transition-colors">Contact</a></li>
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
</body>
</html>'''
    
    return template.format(
        title=html.escape(title),
        description=html.escape(description),
        content=content,
        read_time=read_time
    )

def process_content_files():
    """Process all markdown files and create HTML pages"""
    content_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/Website Content/Firm6102_Programmatic_Content/Phase1_Foundation_Content"
    output_dir = "/Users/fitzhall/projects/Bitcoin Sites/Firm 6102/website/learn"
    
    articles = [
        {
            "file": "01_Bitcoin_Sovereignty_Complete_Guide.md",
            "output": "bitcoin-sovereignty-guide.html",
            "title": "The Complete Guide to Bitcoin Sovereignty",
            "description": "Master Bitcoin sovereignty with comprehensive guidance on self-custody, legal frameworks, estate planning, and wealth protection strategies.",
            "read_time": "45 min"
        },
        {
            "file": "02_Executive_Order_6102_Bitcoin_Lessons.md",
            "output": "executive-order-6102.html",
            "title": "Executive Order 6102: Bitcoin Lessons from Gold Confiscation",
            "description": "Learn from history's most significant wealth confiscation event and discover how Bitcoin provides unprecedented protection against government overreach.",
            "read_time": "35 min"
        },
        {
            "file": "03_KEEP_Protocol_Professional_Standards.md",
            "output": "keep-protocol-standards.html",
            "title": "KEEP Protocol: Professional Standards Framework",
            "description": "The industry's comprehensive certification and standards framework for Bitcoin estate planning professionals and institutional implementation.",
            "read_time": "30 min"
        },
        {
            "file": "04_Bitcoin_Estate_Planning_Complete_Guide.md",
            "output": "bitcoin-estate-planning.html",
            "title": "The Definitive Bitcoin Estate Planning Guide",
            "description": "Comprehensive strategies for structuring, securing, and transferring Bitcoin wealth across generations with legal certainty and technical security.",
            "read_time": "40 min"
        },
        {
            "file": "05_Government_Confiscation_History_Bitcoin_Protection.md",
            "output": "government-confiscation-history.html",
            "title": "Government Confiscation: History and Bitcoin Protection",
            "description": "Complete historical analysis of wealth confiscation from ancient Rome to modern times, and how Bitcoin's design prevents government seizure.",
            "read_time": "45 min"
        }
    ]
    
    for article in articles:
        # Read markdown file
        input_path = os.path.join(content_dir, article["file"])
        output_path = os.path.join(output_dir, article["output"])
        
        print(f"Processing {article['file']}...")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Skip table of contents if present
            markdown_content = re.sub(r'## Table of Contents.*?(?=##)', '', markdown_content, flags=re.DOTALL)
            
            # Convert to HTML
            html_content = convert_markdown_to_html_content(markdown_content)
            
            # Create full page
            full_page = create_article_template(
                title=article["title"],
                description=article["description"],
                content=html_content,
                read_time=article["read_time"]
            )
            
            # Write output
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_page)
            
            print(f"✓ Created {article['output']}")
            
        except Exception as e:
            print(f"✗ Error processing {article['file']}: {str(e)}")

if __name__ == "__main__":
    print("Converting content files to HTML...")
    process_content_files()
    print("\nConversion complete!")