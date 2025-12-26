#!/usr/bin/env python3
"""
AMD Activity Booster - GitHub Action
Generates daily activity logs with AI quotes
"""

import os
import random
from datetime import datetime


AI_QUOTES = [
    "AI is the new electricity. - Andrew Ng",
    "The question of whether a computer can think is no more interesting than the question of whether a submarine can swim. - Edsger Dijkstra",
    "Artificial intelligence is the future, not only for Russia but for all of mankind. - Vladimir Putin",
    "Success in creating AI would be the biggest event in human history. - Stephen Hawking",
    "Machine learning is the last invention that humanity will ever need to make. - Nick Bostrom",
    "AI is not going to replace humans, but humans with AI are going to replace humans without AI. - Karim Lakhani",
    "The real question is, when will we draft an artificial intelligence bill of rights? - Gray Scott",
    "Automation is no longer just a problem for those working in manufacturing. - Moshe Vardi",
    "The key to artificial intelligence has always been the representation. - Jeff Hawkins",
    "AI doesn't have to be evil to destroy humanity. - Elon Musk",
    "The development of full artificial intelligence could spell the end of the human race. - Stephen Hawking",
    "By far, the greatest danger of Artificial Intelligence is that people conclude too early that they understand it. - Eliezer Yudkowsky",
    "Artificial intelligence will reach human levels by around 2029. - Ray Kurzweil",
    "Before we work on artificial intelligence why don't we do something about natural stupidity? - Steve Polyak",
    "The sad thing about artificial intelligence is that it lacks artifice and therefore intelligence. - Jean Baudrillard",
    "I visualize a time when we will be to robots what dogs are to humans. - Claude Shannon",
    "Machine intelligence is the last invention that humanity will ever need to make. - Nick Bostrom",
    "Some people call this artificial intelligence, but the reality is this technology will enhance us. - Ginni Rometty",
    "The question of whether machines can think is about as relevant as whether submarines can swim. - Edsger Dijkstra",
    "Artificial intelligence is growing up fast, as are robots whose facial expressions can elicit empathy. - Diane Ackerman"
]

TECH_QUOTES = [
    "Code is like humor. When you have to explain it, it's bad. - Cory House",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
    "In order to be irreplaceable, one must always be different. - Coco Chanel",
    "Knowledge is power. - Francis Bacon",
    "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away. - Antoine de Saint-Exupery",
    "Ruby is rubbish! PHP is phpantastic! - Nikita Popov",
    "The best error message is the one that never shows up. - Thomas Fuchs",
    "The most disastrous thing that you can ever learn is your first programming language. - Alan Kay",
    "Walking on water and developing software from a specification are easy if both are frozen. - Edward V Berard"
]

MOTIVATIONAL_QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Stay hungry. Stay foolish. - Steve Jobs",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "The only impossible journey is the one you never begin. - Tony Robbins"
]


def get_random_quote():
    """Select a random quote from all categories"""
    all_quotes = AI_QUOTES + TECH_QUOTES + MOTIVATIONAL_QUOTES
    return random.choice(all_quotes)


def generate_activity_log():
    """Generate activity log content"""
    current_time = datetime.utcnow()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    date_formatted = current_time.strftime("%B %d, %Y")
    
    quote = get_random_quote()
    
    content = f"""
---

## 🤖 System Active: {timestamp}

**Date:** {date_formatted}

> **Daily Quote:**  
> *{quote}*

**Status:** ✅ Operational  
**Automation:** Active  
**Next Update:** +24 hours

"""
    return content


def main():
    """Main execution"""
    activity_file = os.getenv('ACTIVITY_FILE', 'activity_log.md')
    
    # Create file if it doesn't exist
    if not os.path.exists(activity_file):
        with open(activity_file, 'w', encoding='utf-8') as f:
            f.write(f"# 📊 Activity Log\n\n")
            f.write("**Automated daily updates powered by AMD Activity Booster**\n\n")
            f.write("This file is automatically updated to keep the repository active.\n")
    
    # Append new activity
    new_content = generate_activity_log()
    
    with open(activity_file, 'a', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Activity log updated: {activity_file}")


if __name__ == "__main__":
    main()
