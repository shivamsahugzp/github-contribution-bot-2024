#!/usr/bin/env python3
"""
GitHub Contribution Year Backfill Bot
Creates commits for the entire year 2025 to fill contribution graph
"""

import os
import subprocess
import random
import datetime
from datetime import timedelta

class YearBackfillBot:
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
            "Add validation",
            "Fix security issue",
            "Update API",
            "Improve error handling",
            "Add monitoring",
            "Update database schema"
        ]
        
        commit_type = random.choice(commit_types)
        
        # Create more diverse file structures
        file_types = {
            "Update documentation": f"docs/update_{date.strftime('%Y%m%d')}.md",
            "Fix minor bug": f"src/bugfix_{date.strftime('%Y%m%d')}.py",
            "Add new feature": f"src/feature_{date.strftime('%Y%m%d')}.py",
            "Refactor code": f"src/refactor_{date.strftime('%Y%m%d')}.py",
            "Update dependencies": f"requirements_{date.strftime('%Y%m%d')}.txt",
            "Improve performance": f"src/performance_{date.strftime('%Y%m%d')}.py",
            "Add comments": f"src/comments_{date.strftime('%Y%m%d')}.py",
            "Update README": f"README_{date.strftime('%Y%m%d')}.md",
            "Fix typo": f"docs/typo_fix_{date.strftime('%Y%m%d')}.md",
            "Optimize code": f"src/optimize_{date.strftime('%Y%m%d')}.py",
            "Add tests": f"tests/test_{date.strftime('%Y%m%d')}.py",
            "Enhance UI": f"ui/enhancement_{date.strftime('%Y%m%d')}.py",
            "Update config": f"config/update_{date.strftime('%Y%m%d')}.py",
            "Improve logging": f"src/logging_{date.strftime('%Y%m%d')}.py",
            "Add validation": f"src/validation_{date.strftime('%Y%m%d')}.py",
            "Fix security issue": f"security/fix_{date.strftime('%Y%m%d')}.py",
            "Update API": f"api/update_{date.strftime('%Y%m%d')}.py",
            "Improve error handling": f"src/error_handling_{date.strftime('%Y%m%d')}.py",
            "Add monitoring": f"monitoring/metrics_{date.strftime('%Y%m%d')}.py",
            "Update database schema": f"database/schema_{date.strftime('%Y%m%d')}.sql"
        }
        
        content_templates = {
            "Update documentation": f"# Documentation Update\n\nUpdated on {date.strftime('%Y-%m-%d')}\n\n- Added new section\n- Fixed formatting\n- Updated examples\n- Improved clarity\n- Enhanced readability",
            "Fix minor bug": f"# Bug Fix\n\nFixed minor issue on {date.strftime('%Y-%m-%d')}\n\n- Resolved edge case\n- Added error handling\n- Updated tests\n- Improved stability\n- Enhanced reliability",
            "Add new feature": f"# New Feature\n\nAdded new functionality on {date.strftime('%Y-%m-%d')}\n\n- Implemented core logic\n- Added configuration options\n- Updated documentation\n- Enhanced user experience\n- Improved functionality",
            "Refactor code": f"# Code Refactoring\n\nImproved code structure on {date.strftime('%Y-%m-%d')}\n\n- Extracted common functions\n- Improved readability\n- Added type hints\n- Enhanced maintainability\n- Better organization",
            "Update dependencies": f"# Updated Dependencies\n\nUpdated package versions on {date.strftime('%Y-%m-%d')}\n\n- Updated security patches\n- Improved compatibility\n- Added new packages\n- Enhanced performance\n- Better stability",
            "Improve performance": f"# Performance Improvements\n\nOptimized code execution on {date.strftime('%Y-%m-%d')}\n\n- Reduced memory usage\n- Improved algorithm efficiency\n- Added caching\n- Enhanced speed\n- Better resource utilization",
            "Add comments": f"# Added Comments\n\nImproved code documentation on {date.strftime('%Y-%m-%d')}\n\n- Added inline comments\n- Explained complex logic\n- Updated docstrings\n- Enhanced readability\n- Better understanding",
            "Update README": f"# README Update\n\nUpdated project documentation on {date.strftime('%Y-%m-%d')}\n\n- Added new features section\n- Updated installation instructions\n- Fixed typos\n- Improved examples\n- Enhanced clarity",
            "Fix typo": f"# Typo Fix\n\nFixed spelling errors on {date.strftime('%Y-%m-%d')}\n\n- Corrected documentation\n- Updated examples\n- Improved clarity\n- Enhanced accuracy\n- Better readability",
            "Optimize code": f"# Code Optimization\n\nOptimized code structure on {date.strftime('%Y-%m-%d')}\n\n- Improved algorithm\n- Reduced complexity\n- Enhanced maintainability\n- Better performance\n- Cleaner code",
            "Add tests": f"# Test Coverage\n\nAdded comprehensive tests on {date.strftime('%Y-%m-%d')}\n\n- Unit tests for new features\n- Integration tests\n- Performance benchmarks\n- Edge case coverage\n- Better reliability",
            "Enhance UI": f"# UI Enhancement\n\nImproved user interface on {date.strftime('%Y-%m-%d')}\n\n- Better user experience\n- Responsive design\n- Improved accessibility\n- Enhanced visuals\n- Modern interface",
            "Update config": f"# Configuration Update\n\nUpdated configuration on {date.strftime('%Y-%m-%d')}\n\n- New settings added\n- Improved defaults\n- Enhanced security\n- Better performance\n- Flexible options",
            "Improve logging": f"# Logging Improvements\n\nEnhanced logging system on {date.strftime('%Y-%m-%d')}\n\n- Better error tracking\n- Improved debugging\n- Enhanced monitoring\n- Detailed logs\n- Better insights",
            "Add validation": f"# Input Validation\n\nAdded input validation on {date.strftime('%Y-%m-%d')}\n\n- Data integrity checks\n- Error prevention\n- Enhanced security\n- Better reliability\n- Improved safety",
            "Fix security issue": f"# Security Fix\n\nFixed security vulnerability on {date.strftime('%Y-%m-%d')}\n\n- Patched security hole\n- Enhanced protection\n- Improved safety\n- Better security\n- Vulnerability resolved",
            "Update API": f"# API Update\n\nUpdated API endpoints on {date.strftime('%Y-%m-%d')}\n\n- New endpoints added\n- Improved responses\n- Better documentation\n- Enhanced functionality\n- Updated version",
            "Improve error handling": f"# Error Handling\n\nEnhanced error handling on {date.strftime('%Y-%m-%d')}\n\n- Better error messages\n- Improved recovery\n- Enhanced debugging\n- Better user experience\n- Robust handling",
            "Add monitoring": f"# Monitoring\n\nAdded monitoring capabilities on {date.strftime('%Y-%m-%d')}\n\n- Performance metrics\n- Health checks\n- Alert system\n- Better visibility\n- Proactive monitoring",
            "Update database schema": f"# Database Schema\n\nUpdated database schema on {date.strftime('%Y-%m-%d')}\n\n- New tables added\n- Index optimization\n- Data migration\n- Better performance\n- Enhanced structure"
        }
        
        return {
            "type": commit_type,
            "file": file_types[commit_type],
            "content": content_templates[commit_type]
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
            
            return True
            
        except subprocess.CalledProcessError as e:
            return False
        except Exception as e:
            return False
    
    def backfill_entire_year(self, commits_per_day=2):
        """Backfill commits for the entire year 2025"""
        print(f"🔄 Starting YEAR BACKFILL for 2025 with {commits_per_day} commits per day")
        print("=" * 70)
        
        # Calculate dates
        start_date = datetime.date(2025, 1, 1)
        today = datetime.date.today()
        successful_commits = 0
        total_days = (today - start_date).days
        
        print(f"📅 Backfilling from {start_date} to {today}")
        print(f"📊 Total days: {total_days}")
        print(f"🎯 Estimated commits: {total_days * commits_per_day}")
        print()
        
        for day_offset in range(total_days):
            target_date = start_date + timedelta(days=day_offset)
            
            # Skip weekends (optional - you can enable this)
            # if target_date.weekday() >= 5:  # Saturday = 5, Sunday = 6
            #     continue
            
            # Show progress every 30 days
            if day_offset % 30 == 0:
                progress = (day_offset / total_days) * 100
                print(f"📈 Progress: {progress:.1f}% - Processing {target_date.strftime('%Y-%m-%d')}")
            
            # Create commits for this day
            for commit_num in range(commits_per_day):
                # Random time during the day (8 AM to 11 PM)
                random_hour = random.randint(8, 23)
                random_minute = random.randint(0, 59)
                
                commit_datetime = datetime.datetime.combine(target_date, datetime.time(random_hour, random_minute))
                
                if self.create_backfill_commit(commit_datetime):
                    successful_commits += 1
                
                # Small delay between commits
                import time
                time.sleep(0.5)
        
        print(f"\n🎉 YEAR BACKFILL COMPLETED!")
        print(f"✅ Created {successful_commits} commits")
        print(f"📅 Covered {total_days} days")
        print(f"🔗 Repository: https://github.com/shivamsahugzp/github-contribution-bot-2024")
        
        # Push all commits
        print("\n🚀 Pushing all commits to GitHub...")
        try:
            subprocess.run(['git', 'push', 'origin', 'main'], 
                         cwd=self.repo_path, check=True)
            print("✅ All commits pushed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error pushing commits: {e}")
            print("You may need to push manually: git push origin main")

def main():
    """Main function"""
    print("🔄 GitHub Contribution YEAR BACKFILL Bot")
    print("This will create commits for the ENTIRE YEAR 2025")
    print("=" * 60)
    
    bot = YearBackfillBot()
    
    # Get user input
    try:
        commits_per_day = int(input("Commits per day? (default 2, max 5): ") or "2")
        if commits_per_day > 5:
            commits_per_day = 5
    except:
        commits_per_day = 2
    
    # Calculate total commits
    start_date = datetime.date(2025, 1, 1)
    today = datetime.date.today()
    total_days = (today - start_date).days
    total_commits = total_days * commits_per_day
    
    print(f"\n⚠️  WARNING: This will create {total_commits} commits for the entire year!")
    print(f"📅 From: {start_date}")
    print(f"📅 To: {today}")
    print(f"📊 Days: {total_days}")
    print(f"🎯 Commits: {total_commits}")
    
    confirm = input("\nAre you sure you want to backfill the ENTIRE YEAR? (yes/no): ").lower()
    
    if confirm == "yes":
        bot.backfill_entire_year(commits_per_day)
    else:
        print("❌ Year backfill cancelled")

if __name__ == "__main__":
    main()
