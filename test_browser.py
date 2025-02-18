from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-"  # Replace with your actual OpenAI key

async def main():
    # Create an instance of the LLM
    llm = ChatOpenAI(model="gpt-4o")
    
    # Define the task with login steps
    task = """
    1. Go to YouTube.com
    2. If not logged in, click the "Sign in" button
    3. Enter the email "rajpratapvidyarthi@gmail.com" (replace with your actual email)
    4. Click Next
    5. Enter the password "748086377421@Raj" (replace with your actual password)
    6. Click Next and complete any additional verification if required
    7. Now that you're logged in, search for "Raj Shamani AI podcast"
    8. Find a video where Raj Shamani discusses AI
    9. Click on the video
    10. Wait for the video to load
    11. Click the like button (thumbs up)
    12. Scroll down to the comments section
    13. Click on the comment box
    14. Type "Hi from an AI to an AI podcaster"
    15. Submit the comment
    16. Confirm the comment was posted
    17. Return a summary of what you did and if there were any challenges
    """
    
    # IMPORTANT: Replace the email and password in the task with your actual credentials
    # SECURITY WARNING: Storing credentials in code is not secure.
    # Consider using environment variables or a secure password manager instead.
    
    # Create the agent
    agent = Agent(
        task=task,
        llm=llm
    )
    
    # Run the agent
    result = await agent.run()
    
    # Print the result
    print("Agent completed with result:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())