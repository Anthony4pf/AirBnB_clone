#!/usr/bin/env python3
"""Initialization module for this package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
