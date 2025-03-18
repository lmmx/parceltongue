import sys
import subprocess
from mcp.server.fastmcp import FastMCP


def install_packages(package_names: list[str]):
    """Install packages using uv pip."""
    for package in package_names:
        try:
            subprocess.run(
                ["uv", "pip", "install", package],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            print(f"Installed {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to install {package}: {e}")


def init_mcpup_models(package_names: list[str]):
    """Initialize mcpup models for the specified packages."""
    # Run mcpup for each package with output captured
    for package in package_names:
        try:
            subprocess.run(
                ["mcpup", package],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            print(f"Generated models for {package}")
        except subprocess.SubprocessError as e:
            print(f"Failed to generate models for {package}: {e}")


def create_mcp_server(server_name: str, package_names: list[str]) -> FastMCP:
    """Create an MCP server with tools from the specified packages."""
    mcp = FastMCP(server_name)

    # Hardcoded registration for known packages
    for package in package_names:
        if package == "requests":
            try:
                # Try to import the requests API module
                from mcpup_models.requests.api import (
                    Get,
                    Post,
                    Put,
                    Delete,
                    Head,
                    Options,
                    Patch,
                )

                # Register each HTTP method
                for method_class in [Get, Post, Put, Delete, Head, Options, Patch]:
                    try:
                        mcp.tool()(method_class.model)
                        print(f"Registered {method_class.__name__} from requests")
                    except Exception as e:
                        print(f"Could not register {method_class.__name__}: {e}")
            except ImportError as e:
                print(f"Failed to import requests models: {e}")

        elif package == "httpx":
            try:
                # Try to import the httpx API module
                from mcpup_models.httpx.api import (
                    Get,
                    Post,
                    Put,
                    Delete,
                    Head,
                    Options,
                    Patch,
                )

                # Register each HTTP method
                for method_class in [Get, Post, Put, Delete, Head, Options, Patch]:
                    try:
                        mcp.tool()(method_class.model)
                        print(f"Registered {method_class.__name__} from httpx")
                    except Exception as e:
                        print(f"Could not register {method_class.__name__}: {e}")
            except ImportError as e:
                print(f"Failed to import httpx models: {e}")

    return mcp


if __name__ == "__main__":
    # Get packages from a single comma-separated argument
    if len(sys.argv) != 2:
        print("Usage: python main.py package1,package2,package3")
        sys.exit(1)

    packages = sys.argv[1].split(",")
    print(f"Working with packages: {', '.join(packages)}")

    # First install the packages
    install_packages(packages)

    # Then initialize models
    init_mcpup_models(packages)

    # Create MCP server with the tools
    mcp = create_mcp_server("parceltongue", packages)

    # Run the server
    mcp.run(transport="stdio")
