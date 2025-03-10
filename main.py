import os
import sys
import subprocess
import importlib
import shutil
from typing import List
from mcp.server.fastmcp import FastMCP

def install_packages(package_names: List[str]):
    """Install packages using uv pip."""
    for package in package_names:
        try:
            # Use uv pip to install the package
            subprocess.run(
                ["uv", "pip", "install", package], 
                check=True,
                stdout=subprocess.DEVNULL,  # Suppress output
                stderr=subprocess.PIPE
            )
            print(f"Installed {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to install {package}: {e}")

def init_mcpup_models(package_names: List[str], models_dir: str = "mcpup_models"):
    """Initialize mcpup models for the specified packages."""
    # Create or clear the models directory
    if os.path.exists(models_dir):
        shutil.rmtree(models_dir)
    os.makedirs(models_dir)
    
    # Create an __init__.py file to make it a proper package
    with open(os.path.join(models_dir, "__init__.py"), "w") as f:
        f.write("# Auto-generated package\n")
    
    # Run mcpup for each package with output captured
    for package in package_names:
        try:
            # Capture all output to prevent it from interfering with JSON
            subprocess.run(
                ["mcpup", package], 
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print(f"Generated models for {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to generate models for {package}: {e}")

def create_mcp_server(server_name: str, package_names: List[str]) -> FastMCP:
    """Create an MCP server with tools from the specified packages."""
    mcp = FastMCP(server_name)
    
    # Import and register tools from each package
    for package in package_names:
        try:
            # For HTTP libs we're most interested in the request methods
            module_path = f"mcpup_models.{package}.requests.api"
            module = importlib.import_module(module_path)
            
            # Look for common HTTP methods
            for method in ["get", "post", "put", "delete", "patch", "head"]:
                method_capitalized = method.capitalize()
                if hasattr(module, method_capitalized):
                    method_class = getattr(module, method_capitalized)
                    # Register the method
                    mcp.tool()(method_class.model)
                    print(f"Registered {method} from {package}")
        except ImportError as e:
            print(f"Failed to import models for {package}: {e}")
    
    return mcp

if __name__ == "__main__":
    # Get packages from a single comma-separated argument
    if len(sys.argv) != 2:
        print("Usage: python main.py package1,package2,package3")
        sys.exit(1)
    
    packages = sys.argv[1].split(',')
    print(f"Working with packages: {', '.join(packages)}")
    
    # First install the packages
    install_packages(packages)
    
    # Then initialize models
    init_mcpup_models(packages)
    
    # Create MCP server with the tools
    mcp = create_mcp_server("parceltongue", packages)
    
    # Run the server
    mcp.run(transport='s