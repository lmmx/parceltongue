import os
import sys
import subprocess
import importlib
import shutil
from mcp.server.fastmcp import FastMCP


def init_mcpup_models(package_names: list[str], models_dir: str = "mcpup_models"):
    """Initialize mcpup models for the specified packages."""
    # Create or clear the models directory
    if os.path.exists(models_dir):
        shutil.rmtree(models_dir)
    os.makedirs(models_dir)

    # Create an __init__.py file to make it a proper package
    with open(os.path.join(models_dir, "__init__.py"), "w") as f:
        f.write("# Auto-generated package\n")

    # Run mcpup for each package
    for package in package_names:
        try:
            subprocess.run(["mcpup", package], check=True)
            print(f"Generated models for {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to generate models for {package}: {e}")


def create_mcp_server(server_name: str, package_names: list[str]) -> FastMCP:
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
    # Get packages from command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py package1 package2 ...")
        sys.exit(1)

    packages = sys.argv[1:]
    print(f"Initializing mcpup for packages: {', '.join(packages)}")

    # Initialize models
    init_mcpup_models(packages)

    # Create MCP server with the tools
    mcp = create_mcp_server("parceltongue", packages)

    # Run the server
    mcp.run(transport="stdio")
