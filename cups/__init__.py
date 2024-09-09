"""
cups_setup Package

This package contains scripts and utilities for setting up and configuring
CUPS and CUPS-PDF for printing PowerPoint files to PDF.

Modules:
- installer: Handles package installation.
- printer: Manages printer configuration and setup.
- config: Contains configuration-related functions.
- cups-utils: Provides utility functions for the package.
"""

from .installer import is_package_installed, install_packages
from .printer import configure_cups_pdf, add_cups_pdf_printer, restart_cups
from .config import needs_setup, update_timestamp
