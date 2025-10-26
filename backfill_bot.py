#!/usr/bin/env python3
"""
GitHub Contribution Backfill Bot
Creates commits with past dates to fill contribution graph
"""

import os
import subprocess
import random
import datetime
from datetime import timedelta

class GitHubBackfillBot:
    def __init__(self):
        self.repo_path = "/Users/shivamsahu/Documents/Projects/github-contribution-bot"
        self.github_token = os.getenv("GITHUB_TOKEN", "")
        
    def generate_commit_content(self, date):
        """Generate realistic commit content for a specific date"""
        commit_types = [
            "Update documentation",
            "Fix minor bug",
            "Add new feature",
            "Refactor code",
            "Update dependencies",
            "Improve performance",
            "Add comments",
            "Update README",
            "Fix typo",
            "Optimize code",
            "Add tests",
            "Enhance UI",
            "Update config",
            "Improve logging",
            "Add validation"
        ]
        
        commit_type = random.choice(commit_types)
        
        content_templates = {
            "Update documentation": {
                "file": f"docs/update_{date.strftime('%Y%m%d')}.md",
                "content": f"# Documentation Update\n\nUpdated on {date.strftime('%Y-%m-%d')}\n\n- Added new section\n- Fixed formatting\n- Updated examples\n- Improved clarity"
            },
            "Fix minor bug": {
                "file": f"src/bugfix_{date.strftime('%Y%m%d')}.py",
                "content": f"# Bug Fix\n\nFixed minor issue on {date.strftime('%Y-%m-%d')}\n\n- Resolved edge case\n- Added error handling\n- Updated tests\n- Improved stability"
            },
            "Add new feature": {
                "file": f"src/feature_{date.strftime('%Y%m%d')}.py",
                "content": f"# New Feature\n\nAdded new functionality on {date.strftime('%Y-%m-%d')}\n\n- Implemented core logic\n- Added configuration options\n- Updated documentation\n- Enhanced user experience"
            },
            "Refactor code": {
                "file": f"src/refactor_{date.strftime('%Y%m%d')}.py",
                "content": f"# Code Refactoring\n\nImproved code structure on {date.strftime('%Y-%m-%d')}\n\n- Extracted common functions\n- Improved readability\n- Added type hints\n- Enhanced maintainability"
            },
            "Update dependencies": {
                "file": f"requirements_{date.strftime('%Y%m%d')}.txt",
                "content": f"# Updated Dependencies\n\nUpdated package versions on {date.strftime('%Y-%m-%d')}\n\n- Updated security patches\n- Improved compatibility\n- Added new packages\n- Enhanced performance"
            },
            "Improve performance": {
                "file": f"src/performance_{date.strftime('%Y%m%d')}.py",
                "content": f"# Performance Improvements\n\nOptimized code execution on {date.strftime('%Y-%m-%d')}\n\n- Reduced memory usage\n- Improved algorithm efficiency\n- Added caching\n- Enhanced speed"
            },
            "Add comments": {
                "file": f"src/comments_{date.strftime('%Y%m%d')}.py",
                "content": f"# Added Comments\n\nImproved code documentation on {date.strftime('%Y-%m-%d')}\n\n- Added inline comments\n- Explained complex logic\n- Updated docstrings\n- Enhanced readability"
            },
            "Update README": {
                "file": f"README_{date.strftime('%Y%m%d')}.md",
                "content": f"# README Update\n\nUpdated project documentation on {date.strftime('%Y-%m-%d')}\n\n- Added new features section\n- Updated installation instructions\n- Fixed typos\n- Improved examples"
            },
            "Fix typo": {
                "file": f"docs/typo_fix_{date.strftime('%Y%m%d')}.md",
                "content": f"# Typo Fix\n\nFixed spelling errors on {date.strftime('%Y-%m-%d')}\n\n- Corrected documentation\n- Updated examples\n- Improved clarity\n- Enhanced accuracy"
            },
            "Optimize code": {
                "file": f"src/optimize_{date.strftime('%Y%m%d')}.py",
                "content": f"# Code Optimization\n\nOptimized code structure on {date.strftime('%Y-%m-%d')}\n\n- Improved algorithm\n- Reduced complexity\n- Enhanced maintainability\n- Better performance"
            },
            "Add tests": {
                "file": f"tests/test_{date.strftime('%Y%m%d')}.py",
                "content": f"# Test Coverage\n\nAdded comprehensive tests on {date.strftime('%Y-%m-%d')}\n\n- Unit tests for new features\n- Integration tests\n- Performance benchmarks\n- Edge case coverage"
            },
            "Enhance UI": {
                "file": f"ui/enhancement_{date.strftime('%Y%m%d')}.py",
                "content": f"# UI Enhancement\n\nImproved user interface on {date.strftime('%Y-%m-%d')}\n\n- Better user experience\n- Responsive design\n- Improved accessibility\n- Enhanced visuals"
            },
            "Update config": {
                "file": f"config/update_{date.strftime('%Y%m%d')}.py",
                "content": f"# Configuration Update\n\nUpdated configuration on {date.strftime('%Y-%m-%d')}\n\n- New settings added\n- Improved defaults\n- Enhanced security\n- Better performance"
            },
            "Improve logging": {
                "file": f"src/logging_{date.strftime('%Y%m%d')}.py",
                "content": f"# Logging Improvements\n\nEnhanced logging system on {date.strftime('%Y-%m-%d')}\n\n- Better error tracking\n- Improved debugging\n- Enhanced monitoring\n- Detailed logs"
            },
            "Add validation": {
                "file": f"src/validation_{date.strftime('%Y%m%d')}.py",
                "content": f"# Input Validation\n\nAdded input validation on {date.strftime('%Y-%m-%d')}\n\n- Data integrity checks\n- Error prevention\n- Enhanced security\n- Better reliability"
            }
        }
        
        return {
            "type": commit_type,
            "file": content_templates[commit_type]["file"],
            "content": content_templates[commit_type]["content"]
        }
    
    def create_backfill_commit(self, target_date):
        """Create a commit with a specific past date"""
        try:
            # Generate commit content
            commit_data = self.generate_commit_content(target_date)
            
            # Ensure directory exists
            file_dir = os.path.dirname(os.path.join(self.repo_path, commit_data["file"]))
            if file_dir and not os.path.exists(file_dir):
                os.makedirs(file_dir, exist_ok=True)
            
            # Write content to file
            file_path = os.path.join(self.repo_path, commit_data["file"])
            with open(file_path, 'w') as f:
                f.write(commit_data["content"])
            
            # Add file to git
            subprocess.run(['git', 'add', commit_data["file"]], 
                         cwd=self.repo_path, check=True)
            
            # Create commit with specific date
            commit_message = f"{commit_data['type']} - {target_date.strftime('%Y-%m-%d %H:%M')}"
            
            # Set environment variables for commit date
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = target_date.strftime('%Y-%m-%d %H:%M:%S')
            env['GIT_COMMITTER_DATE'] = target_date.strftime('%Y-%m-%d %H:%M:%S')
            
            subprocess.run(['git', 'commit', '-m', commit_message], 
                         cwd=self.repo_path, check=True, env=env)
            
            print(f"✅ Created backfill commit: {commit_message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error creating backfill commit: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False
    
    def backfill_past_days(self, days_back=30, commits_per_day=2):
        """Backfill commits for past days"""
        print(f"🔄 Starting backfill for {days_back} days with {commits_per_day} commits per day")
        print("=" * 60)
        
        # Calculate dates
        today = datetime.date.today()
        successful_commits = 0
        
        for day_offset in range(1, days_back + 1):
            target_date = today - timedelta(days=day_offset)
            
            # Skip weekends if desired (optional)
            if target_date.weekday() >= 5:  # Saturday = 5, Sunday = 6
                continue
            
            print(f"\n📅 Backfilling {target_date.strftime('%Y-%m-%d')} ({target_date.strftime('%A')})")
            
            # Create commits for this day
            for commit_num in range(commits_per_day):
                # Random time during the day (9 AM to 10 PM)
                random_hour = random.randint(9, 22)
                random_minute = random.randint(0, 59)
                
                commit_datetime = datetime.datetime.combine(target_date, datetime.time(random_hour, random_minute))
                
                print(f"  🔄 Creating commit {commit_num + 1}/{commits_per_day} for {commit_datetime.strftime('%H:%M')}")
                
                if self.create_backfill_commit(commit_datetime):
                    successful_commits += 1
                
                # Small delay between commits
                import time
                time.sleep(2)
        
        print(f"\n🎉 Backfill completed! Created {successful_commits} commits")
        
        # Push all commits
        print("🚀 Pushing all commits to GitHub...")
        try:
            subprocess.run(['git', 'push', 'origin', 'main'], 
                         cwd=self.repo_path, check=True)
            print("✅ All commits pushed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error pushing commits: {e}")
            print("You may need to push manually: git push origin main")

def main():
    """Main function"""
    print("🔄 GitHub Contribution Backfill Bot")
    print("This will create commits with past dates to fill your contribution graph")
    print()
    
    bot = GitHubBackfillBot()
    
    # Get user input
    try:
        days_back = int(input("How many days back to fill? (default 30): ") or "30")
        commits_per_day = int(input("Commits per day? (default 2): ") or "2")
    except:
        days_back = 30
        commits_per_day = 2
    
    print(f"\n⚠️  WARNING: This will create {days_back * commits_per_day} commits with past dates")
    confirm = input("Are you sure you want to continue? (yes/no): ").lower()
    
    if confirm == "yes":
        bot.backfill_past_days(days_back, commits_per_day)
    else:
        print("❌ Backfill cancelled")

if __name__ == "__main__":
    main()
