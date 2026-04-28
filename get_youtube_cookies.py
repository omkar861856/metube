import subprocess
import sys
import platform
import os

def get_cookies():
    print("Attempting to extract YouTube cookies from your browser...")
    print("You may be prompted for your system password to access browser cookies (e.g., Chrome Safe Storage).")
    print("Please grant permission if prompted.\n")
    
    # Try common browsers in order of popularity
    browsers = ["chrome", "firefox", "safari", "edge", "opera", "brave"]
    
    output_file = "cookies.txt"
    
    for browser in browsers:
        print(f"Trying to extract from {browser}...")
        try:
            # Run yt-dlp to extract cookies for youtube.com
            # We use uv run python -m yt_dlp to ensure we use the project's yt-dlp
            result = subprocess.run(
                ["uv", "run", "python", "-m", "yt_dlp", "--cookies-from-browser", browser, "--cookies", output_file, "https://www.youtube.com", "--skip-download"],
                capture_output=True,
                text=True
            )
            
            # yt-dlp might return 1 if it can't download a specific video, but still extract cookies successfully.
            # So we check if the file was created and has youtube.com cookies.
            if os.path.exists(output_file):
                with open(output_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "# Netscape HTTP Cookie File" in content and "youtube.com" in content:
                        print(f"\n✅ Successfully extracted YouTube cookies from {browser}!")
                        print(f"Cookies saved to: {os.path.abspath(output_file)}")
                        print("You can now use these cookies for high-quality downloads in MeTube.")
                        return True
                    
        except Exception as e:
            print(f"Error trying {browser}: {e}")
            
    print("\n❌ Failed to extract cookies from any known browser.")
    print("Please make sure:")
    print("1. You are logged into YouTube in one of your installed browsers.")
    print("2. You granted the necessary permissions when prompted.")
    print("3. Your browser is supported (Chrome, Firefox, Safari, Edge, Opera, Brave).")
    return False

if __name__ == "__main__":
    get_cookies()
