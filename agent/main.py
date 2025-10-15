import asyncio
import sys
import os
from src.agent import get_job_postings

async def main():
    """
    Main entry point for the job crawler agent.
    """
    print("🚀 Starting Job Crawler Agent...")
    print("=" * 50)
    
    # Default configuration
    default_website = "https://www.indeed.com"
    default_job_count = 5
    
    # Get user input or use defaults
    if len(sys.argv) > 1:
        website = sys.argv[1]
    else:
        website = input(f"Enter job website URL (default: {default_website}): ").strip()
        if not website:
            website = default_website
    
    if len(sys.argv) > 2:
        try:
            job_count = int(sys.argv[2])
        except ValueError:
            print("⚠️  Invalid job count, using default value.")
            job_count = default_job_count
    else:
        job_count_input = input(f"Enter number of jobs to extract (default: {default_job_count}): ").strip()
        if job_count_input.isdigit():
            job_count = int(job_count_input)
        else:
            job_count = default_job_count
    
    print(f"\n🎯 Target Website: {website}")
    print(f"📊 Jobs to Extract: {job_count}")
    print("\n🔄 Starting job extraction...")
    
    try:
        # Run the job extraction
        results = await get_job_postings(website, job_count)
        
        print("\n✅ Job extraction completed!")
        print("=" * 50)
        print("📋 RESULTS:")
        print("=" * 50)
        print(results)
        
        # Optionally save results to file
        save_to_file = input("\n💾 Save results to file? (y/N): ").strip().lower()
        if save_to_file in ['y', 'yes']:
            filename = f"job_results_{website.replace('https://', '').replace('http://', '').replace('/', '_').replace('.', '_')}.txt"
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Job Extraction Results\n")
                    f.write(f"Website: {website}\n")
                    f.write(f"Date: {asyncio.get_event_loop().time()}\n")
                    f.write("=" * 50 + "\n")
                    # Ensure results is converted to string
                    if isinstance(results, str):
                        f.write(results)
                    else:
                        f.write(str(results))
                print(f"✅ Results saved to: {filename}")
            except Exception as file_error:
                print(f"⚠️  Failed to save file: {str(file_error)}")
                print("   Results are still displayed above.")
        
    except Exception as e:
        print(f"\n❌ Error occurred during job extraction:")
        print(f"   {str(e)}")
        print("\n🔧 Please check:")
        print("   - Your internet connection")
        print("   - The website URL is valid")
        print("   - Your OpenAI API key is configured")
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