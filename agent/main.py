import asyncio
import sys
import os
from src.agent_factory import create_agent, get_supported_websites

async def main():
    """
    Main entry point for the job crawler agent.
    """
    print("🚀 Starting Job Crawler Agent...")
    print("=" * 50)
    
    # Check if all required parameters are provided
    if len(sys.argv) != 4:
        print("❌ Error: All parameters are required!")
        print("Usage: python main.py <website_url> <job_count> <search_term>")
        print("Example: python main.py \"https://itviec.com\" 5 \"python developer\"")
        print(f"Supported websites: {', '.join(get_supported_websites())}")
        return 1
    
    # Get parameters from command line
    website = sys.argv[1]
    
    try:
        job_count = int(sys.argv[2])
    except ValueError:
        print("❌ Error: Job count must be a valid integer!")
        return 1
    
    search_term = sys.argv[3]
    
    # Get the appropriate agent for the website
    agent = create_agent(website, search_term, job_count)
    if not agent:
        print(f"❌ Error: No agent found for website: {website}")
        print(f"Supported websites: {', '.join(get_supported_websites())}")
        return 1
    
    print(f"\n🎯 Target Website: {website}")
    print(f"📊 Jobs to Extract: {job_count}")
    print(f"🔍 Search Term: {search_term}")
    print(f"🤖 Using Agent: {agent.__class__.__name__}")
    print("\n🔄 Starting job extraction...")
    
    try:
        # Run the job extraction
        results = await agent.get_job_postings()
        
        print("\n✅ Job extraction completed!")
        print("=" * 50)
        print("📋 RESULTS:")
        print("=" * 50)
        print(results)
        
        # Save results to file
        filename = "result.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Job Extraction Results\n")
                f.write(f"Website: {website}\n")
                f.write(f"Search Term: {search_term}\n")
                f.write(f"Date: {asyncio.get_event_loop().time()}\n")
                f.write("=" * 50 + "\n")
                # Ensure results is converted to string
                if isinstance(results, str):
                    f.write(results)
                else:
                    f.write(str(results))
            print(f"\n✅ Results saved to: {filename}")
        except Exception as file_error:
            print(f"\n⚠️  Failed to save file: {str(file_error)}")
            print("   Results are still displayed above.")
        
    except Exception as e:
        print(f"\n❌ Error occurred during job extraction:")
        print(f"   {str(e)}")
        print("\n🔧 Please check:")
        print("   - Your internet connection")
        print("   - The website URL is valid and supported")
        print("   - Your OpenAI API key is configured")
        print(f"   - Supported websites: {', '.join(get_supported_websites())}")
        return 1
    
    return 0

def check_environment():
    """
    Check if the environment is properly configured.
    """
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found.")
        print("   Make sure to configure your OpenAI API key and other settings.")
    
    # Check if src directory exists
    if not os.path.exists('src'):
        print("❌ Error: src directory not found.")
        print("   Make sure you're running this from the project root directory.")
        return False
    
    return True

if __name__ == "__main__":
    print("🤖 Job Crawler Agent")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Run the main function
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⏹️  Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)