import re
import os

file_path = 'd:/Downloads/profile-system (1)/README.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<NAME>': 'Zaki',
    '&lt;NAME&gt;': 'Zaki',
    '<TAGLINE>': 'Software Developer',
    '&lt;TAGLINE&gt;': 'Software Developer',
    '<CURRENT_PROJECT>': 'an awesome CLI tool',
    '&lt;CURRENT_PROJECT&gt;': 'an awesome CLI tool',
    '<CURRENT_LEARNING>': 'System Design',
    '&lt;CURRENT_LEARNING&gt;': 'System Design',
    '<CURRENT_EXPERIMENT>': 'Local LLMs',
    '&lt;CURRENT_EXPERIMENT&gt;': 'Local LLMs',
    '<CURRENT_SHIPPING>': 'v2.0 of my profile',
    '&lt;CURRENT_SHIPPING&gt;': 'v2.0 of my profile',
    '<USERNAME>': 'Zaki086',
    '&lt;USERNAME&gt;': 'Zaki086',
    '<CURRENT_ROLE>': 'Engineer',
    '&lt;CURRENT_ROLE&gt;': 'Engineer',
    '<PROJECT_1_NAME>': 'Terminal Dashboard',
    '&lt;PROJECT_1_NAME&gt;': 'Terminal Dashboard',
    '<PROJECT_1_DESCRIPTION>': 'A terminal inspired GitHub profile',
    '&lt;PROJECT_1_DESCRIPTION&gt;': 'A terminal inspired GitHub profile',
    '<TECH_1>': 'TypeScript',
    '&lt;TECH_1&gt;': 'TypeScript',
    '<TECH_2>': 'React',
    '&lt;TECH_2&gt;': 'React',
    '<TECH_3>': 'Python',
    '&lt;TECH_3&gt;': 'Python',
    '<REPO_1>': 'Zaki086',
    '&lt;REPO_1&gt;': 'Zaki086',
    '<DEMO_1_URL>': 'https://github.com/Zaki086',
    '&lt;DEMO_1_URL&gt;': 'https://github.com/Zaki086',
    '<PROJECT_2_NAME>': 'System Monitor',
    '&lt;PROJECT_2_NAME&gt;': 'System Monitor',
    '<PROJECT_2_DESCRIPTION>': 'Real-time performance tracking',
    '&lt;PROJECT_2_DESCRIPTION&gt;': 'Real-time performance tracking',
    '<REPO_2>': 'sys-mon',
    '&lt;REPO_2&gt;': 'sys-mon',
    '<DEMO_2_URL>': 'https://github.com/Zaki086',
    '&lt;DEMO_2_URL&gt;': 'https://github.com/Zaki086',
    '<PROJECT_3_NAME>': 'AI Agent',
    '&lt;PROJECT_3_NAME&gt;': 'AI Agent',
    '<PROJECT_3_DESCRIPTION>': 'Automated coding assistant',
    '&lt;PROJECT_3_DESCRIPTION&gt;': 'Automated coding assistant',
    '<REPO_3>': 'ai-agent',
    '&lt;REPO_3&gt;': 'ai-agent',
    '<DEMO_3_URL>': 'https://github.com/Zaki086',
    '&lt;DEMO_3_URL&gt;': 'https://github.com/Zaki086',
    '<PROJECT_4_NAME>': 'Portfolio',
    '&lt;PROJECT_4_NAME&gt;': 'Portfolio',
    '<PROJECT_4_DESCRIPTION>': 'My personal portfolio site',
    '&lt;PROJECT_4_DESCRIPTION&gt;': 'My personal portfolio site',
    '<REPO_4>': 'portfolio',
    '&lt;REPO_4&gt;': 'portfolio',
    '<DEMO_4_URL>': 'https://github.com/Zaki086',
    '&lt;DEMO_4_URL&gt;': 'https://github.com/Zaki086',
    '<PORTFOLIO_URL>': 'https://github.com/Zaki086',
    '&lt;PORTFOLIO_URL&gt;': 'https://github.com/Zaki086',
    '<LINKEDIN_HANDLE>': 'zaki',
    '&lt;LINKEDIN_HANDLE&gt;': 'zaki',
    '<TWITTER_HANDLE>': 'zaki086',
    '&lt;TWITTER_HANDLE&gt;': 'zaki086',
    '<EMAIL>': 'contact@example.com',
    '&lt;EMAIL&gt;': 'contact@example.com'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
