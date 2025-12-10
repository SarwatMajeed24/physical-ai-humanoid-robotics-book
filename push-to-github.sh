#!/bin/bash
# Create repo on GitHub if not exists
gh repo create SarwatMajeed24/physical-ai-humanoid-robotics-book --public --description "Open-source course book on Physical AI & Humanoid Robotics" --disable-issues --disable-wiki

# Add remote and push
git remote set-url origin https://github.com/SarwatMajeed24/physical-ai-humanoid-robotics-book.git
git branch -M main
git push -u origin main