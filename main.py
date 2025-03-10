import os
import sys
import subprocess
import importlib
import glob
from typing import List
from mcp.server.fastmcp import FastMCP

def install_packages(package_names: List[str]):
    """Install packages using uv pip."""
    for package in package_names:
        try:
            subprocess.run(
                ["uv", "pip", "install", package], 
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print(f"Installed {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to install {package}: {e}")

def init_mcpup_models(package_names: List[str], models_dir: str = "mcpup_models"):
    """Initialize mcpup models for the specified packages."""
    # Create the models directory if it doesn't exist
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    # Create an __init__.py file to make it a proper package
    with open(os.path.join(models_dir, "__init__.py"), "w") as f:
        f.write("# Auto-generated package\n")
    
    # Run mcpup for each package with output captured
    for package in package_names:
        try:
            subprocess.run(
                ["mcpup", package], 
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print(f"Generated models for {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to generate models for {package}: {e}")

def find_model_modules(package_name, base_dir="mcpup_models"):
    """Find all modules containing models for a package."""
    package_dir = os.path.join(base_dir, package_name)
    model_files = []
    
    # Find all models.py files in the package directory
    for root, dirs, files in os.walk(package_dir):
        if "models.py" in files:
            # Convert file path to module path
            rel_path = os.path.relpath(root, os.path.dirname(base_dir))
            module_path = rel_path.replace(os.sep, ".")
            model_files.append(module_path)
            
        # Also look for api.py files which might contain models
        if "api.py" in files:
            rel_path = os.path.relpath(root, os.path.dirname(base_dir))
            module_path = rel_path.replace(os.sep, ".")
            model_files.append(f"{module_path}.api")
    
    return model_files

def create_mcp_server(server_name: str, package_names: List[str]) -> FastMCP:
    """Create an MCP server with tools from the specified packages."""
    mcp = FastMCP(server_name)
    
    # Register tools from each package
    for package in package_names:
        try:
            # Find all modules with models
            module_paths = find_model_modules(package)
            print(f"Found modules for {package}: {module_paths}")
            
            for module_path in module_paths:
                try:
                    module = importlib.import_module(module_path)
                    
                    # Find model classes (usually PascalCase versions of functions)
                    for attr_name in dir(module):
                        if attr_name.startswith('_'):
                            continue
                        
                        attr = getattr(module, attr_name)
                        # Check if it has a model attribute
                        if hasattr(attr, 'model') and callable(attr.model):
                            try:
                                mcp.tool()(attr.model)
                                print(f"Registered {attr_name} from {module_path}")
                            except Exception as e:
                                print(f"Could not register {attr_name}: {e}")
                except ImportError as e:
                    print(f"Could not import {module_path}: {e}")
        except Exception as e:
            print(f"Error processing {package}: {e}")
    
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
    mcp.run(transport='stdio')