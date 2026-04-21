# Github Repo Scanner

## Why I Built This?

As a 2nd-year Computer Programming student at George Brown College, I wanted honest feedback on my portfolio before entering the job market.

**My Questions:**
- Can I get hired as a junior developer with these projects?
- What's my current skill level?
- What should I improve next?
- Are there any red flags in my code?

**The Problem:** When I paste my GitHub profile link to AI tools like Claude, they cannot read the code files directly.

**The Solution:** This tool generates raw file URLs that AI can actually access and analyze.
Instead of manually clicking the "Raw" button for every single file and copying the URLs, I decided to build this small tool to automate the process.

## What It Does?

This script:
- Takes a GitHub username
- Lists all repositories for that user
- Allows you to select a repository and branch
- Generates raw file URLs for all files in that repository


## Example:
**Then I paste raw file URLs into Claude.ai and ask:**
> *"Review my ASP.NET Core project. Can I get hired as a junior .NET developer in Toronto? What's missing from my portfolio?"*

### Usage

```
python scanner.py
```

Enter your GitHub username, select a repo, select a branch, and get all raw file URLs

### Why Python?

This is a simple automation script - perfect use case for Python.

## Technologies

- Python 3.14
- GitHub REST API
- `requests` library

## Future Plans
Building **GitHubRepoScannerWeb** (C# web version):
- ASP.NET Core MVC
- Web interface
- Anthropic Claude API integration
- Automatic portfolio analysis reports