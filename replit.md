# Legal Boolean Search Builder

## Overview
A web-based tool that helps users create precise legal search strings for Boolean searches in legal databases like Westlaw, Lexis, and Bloomberg Law. The application guides users through building structured search queries with concepts, synonyms, and proper Boolean operators.

## Current State
Successfully imported and configured for Replit environment:
- ✅ Static HTML application serving on port 5000
- ✅ Python HTTP server setup
- ✅ Workflow configured and running
- ✅ Deployment configuration complete
- ✅ Cache control headers for Replit iframe compatibility

## Recent Changes (September 18, 2025)
- Renamed `frontend` file to `index.html` for conventional web serving
- Created Python HTTP server (`server.py`) with proper cache control headers
- Set up workflow configuration for frontend server on port 5000
- Configured deployment settings for autoscale deployment target
- Added .gitignore for Python project

## Project Architecture
- **Frontend**: Single-page HTML application with embedded JavaScript and Tailwind CSS
- **Server**: Python 3.11 HTTP server serving static content
- **Port Configuration**: Frontend on 0.0.0.0:5000 (required for Replit environment)

## Technology Stack
- HTML5 with embedded JavaScript
- Tailwind CSS (via CDN)
- Python 3.11 HTTP server
- No backend database required (purely frontend logic)

## Features
- Interactive concept grouping with OR logic
- Boolean connector selection (AND, /p, /s)
- Truncation helper with automatic prefix detection
- Phrase search suggestions with proximity operators
- Real-time search string generation
- Copy to clipboard functionality
- Review checklist for search validation

## User Preferences
None specified yet.

## Next Steps
- Project is ready for use and deployment
- Consider migrating from CDN to local Tailwind CSS for production use
- Monitor for any user feedback or feature requests