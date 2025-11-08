#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NGL Message Automation System v9.0 - Professional Edition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  EDUCATIONAL PURPOSE ONLY
⚠️  This violates NGL's Terms of Service
⚠️  Use at your own risk
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import time
import requests
from random import choice as random_choice, randint
from datetime import datetime
import uuid
import os
import sys

# ============================================
# CONFIGURATION & CONSTANTS
# ============================================
VERSION = "9.0"
AUTHOR = "RIZKY STORE 04"
API_ENDPOINT = "https://ngl.link/api/submit"
NGL_BASE_URL = "https://ngl.link"

# Color codes for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# ============================================
# UTILITY FUNCTIONS
# ============================================
def clear_screen():
    """Clear terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")

def print_colored(text, color=Colors.END, bold=False):
    """Print colored text"""
    style = Colors.BOLD if bold else ""
    print(f"{style}{color}{text}{Colors.END}")

def print_banner():
    """Display application banner"""
    banner = f"""{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ███╗   ██╗ ██████╗ ██╗         ███████╗██████╗  █████╗ ███╗   ███╗
║   ████╗  ██║██╔════╝ ██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║
║   ██╔██╗ ██║██║  ███╗██║         ███████╗██████╔╝███████║██╔████╔██║
║   ██║╚██╗██║██║   ██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
║   ██║ ╚████║╚██████╔╝███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
║   ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
║                                                                    ║
║              PROFESSIONAL MESSAGE AUTOMATION SYSTEM                ║
║                       Version {VERSION} - Premium                        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
{Colors.END}"""
    print(banner)

def print_section_header(title, width=70):
    """Print section header"""
    print(f"\n{Colors.CYAN}{'═' * width}")
    print(f"║ {title.center(width - 4)} ║")
    print(f"{'═' * width}{Colors.END}\n")

def print_box(lines, width=70):
    """Print content in a box"""
    print(f"{Colors.BLUE}┌{'─' * (width - 2)}┐{Colors.END}")
    for line in lines:
        padding = width - len(line) - 4
        print(f"{Colors.BLUE}│{Colors.END} {line}{' ' * padding} {Colors.BLUE}│{Colors.END}")
    print(f"{Colors.BLUE}└{'─' * (width - 2)}┘{Colors.END}")

def print_divider(char='─', width=70):
    """Print divider line"""
    print(f"{Colors.BLUE}{char * width}{Colors.END}")

# ============================================
# CORE FUNCTIONS
# ============================================
def load_questions_from_file():
    """Load questions from external file"""
    try:
        with open("questions.txt", "r", encoding="utf-8") as f:
            questions = [line.strip() for line in f if line.strip()]
            if questions:
                return questions
    except FileNotFoundError:
        pass
    
    # Default questions if file not found
    return [
        "Hey! What's on your mind? 💭",
        "You're amazing! Keep shining! ✨",
        "How's your day going? 🌟",
        "Send me a message! I'd love to chat 📩",
        "You seem interesting! Tell me more 🤔",
        "What makes you happy? 😊",
        "What's your favorite thing to do? 🎯",
        "You're awesome! 🔥",
        "What's something you're proud of? 🏆",
        "Tell me something about yourself! 👋"
    ]

def extract_username(input_text):
    """Extract clean username from URL or text"""
    username = input_text.strip()
    
    # Remove common prefixes
    username = username.replace('https://', '').replace('http://', '')
    username = username.replace('ngl.link/', '')
    username = username.replace('@', '')
    username = username.split('/')[0]
    username = username.split('?')[0]
    
    return username.lower()

def send_ngl_message(username, message):
    """Send message to NGL account"""
    
    url = f"{NGL_BASE_URL}/{username}"
    
    payload = {
        "username": username,
        "question": message,
        "deviceId": str(uuid.uuid4()),
        "gameSlug": "",
        "referrer": ""
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": url,
        "Origin": NGL_BASE_URL,
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json"
    }
    
    try:
        response = requests.post(
            API_ENDPOINT,
            data=payload,
            headers=headers,
            timeout=15
        )
        
        return {
            'success': response.status_code == 200,
            'status_code': response.status_code,
            'response': response.text
        }
        
    except requests.exceptions.Timeout:
        return {'success': False, 'status_code': 0, 'error': 'Timeout'}
    except requests.exceptions.ConnectionError:
        return {'success': False, 'status_code': 0, 'error': 'Connection Error'}
    except Exception as e:
        return {'success': False, 'status_code': 0, 'error': str(e)}

# ============================================
# USER INTERFACE FUNCTIONS
# ============================================
def get_target_username():
    """Get and validate target username"""
    print_section_header("TARGET CONFIGURATION")
    
    print_box([
        "🎯 Enter the NGL username or profile link",
        "",
        "Accepted formats:",
        "  • username",
        "  • @username",
        "  • https://ngl.link/username"
    ])
    
    while True:
        username = input(f"\n{Colors.YELLOW}➤ Enter target: {Colors.END}").strip()
        
        if not username:
            print_colored("   ✗ Username cannot be empty!", Colors.RED)
            continue
        
        username = extract_username(username)
        
        if len(username) < 3:
            print_colored("   ✗ Username too short!", Colors.RED)
            continue
        
        print_colored(f"\n   ✓ Target verified: {username}", Colors.GREEN, bold=True)
        return username

def get_message_mode():
    """Select message delivery mode"""
    print_section_header("MESSAGE CONFIGURATION")
    
    print_box([
        "💬 SELECT MESSAGE MODE",
        "",
        "  [1] 🎲 RANDOM MODE",
        "      → Automatically select from question database",
        "      → {count} messages available",
        "",
        "  [2] ✏️  CUSTOM MODE",
        "      → Send your own specific message",
        "      → Perfect for targeted messaging"
    ])
    
    while True:
        mode = input(f"\n{Colors.YELLOW}➤ Select mode (1/2): {Colors.END}").strip()
        
        if mode == '1':
            questions = load_questions_from_file()
            print_colored(f"\n   ✓ Random mode activated", Colors.GREEN)
            print_colored(f"   📊 Database: {len(questions)} messages loaded", Colors.CYAN)
            return {'mode': 'random', 'questions': questions}
        
        elif mode == '2':
            message = input(f"\n{Colors.YELLOW}➤ Enter your message: {Colors.END}").strip()
            
            if not message:
                print_colored("   ✗ Message cannot be empty!", Colors.RED)
                continue
            
            if len(message) > 300:
                print_colored("   ⚠ Message too long! Trimming to 300 characters.", Colors.YELLOW)
                message = message[:300]
            
            print_colored(f"\n   ✓ Custom message set", Colors.GREEN)
            print_colored(f"   📝 Preview: '{message}'", Colors.CYAN)
            return {'mode': 'custom', 'message': message}
        
        else:
            print_colored("   ✗ Invalid choice! Please enter 1 or 2", Colors.RED)

def get_quantity():
    """Get message quantity"""
    print_section_header("DELIVERY QUANTITY")
    
    print_box([
        "📦 SET MESSAGE QUANTITY",
        "",
        "  [0] ♾️  UNLIMITED MODE",
        "      → Continuous delivery until manually stopped",
        "      → Use CTRL+C to stop",
        "",
        "  [1-999] 📊 BATCH MODE",
        "      → Send specific number of messages",
        "      → Recommended: 10-50 messages"
    ])
    
    while True:
        qty_input = input(f"\n{Colors.YELLOW}➤ Enter quantity (0 for unlimited): {Colors.END}").strip()
        
        try:
            quantity = int(qty_input)
            
            if quantity < 0:
                print_colored("   ✗ Please enter 0 or positive number!", Colors.RED)
                continue
            
            if quantity == 0:
                print_colored("\n   ✓ Unlimited mode activated", Colors.GREEN)
                print_colored("   ⚠ Press CTRL+C anytime to stop", Colors.YELLOW)
            else:
                print_colored(f"\n   ✓ Batch mode: {quantity} messages scheduled", Colors.GREEN)
            
            return quantity
            
        except ValueError:
            print_colored("   ✗ Please enter a valid number!", Colors.RED)

def get_timing_strategy():
    """Get delivery timing strategy"""
    print_section_header("TIMING STRATEGY")
    
    print_box([
        "⏰ SELECT DELIVERY TIMING",
        "",
        "  [1] ⚡ FAST DELIVERY (2-4 seconds)",
        "      → Quick message bursts",
        "      → Higher detection risk",
        "",
        "  [2] 🚶 NORMAL PACE (4-8 seconds)",
        "      → Balanced delivery speed",
        "      → Recommended for most cases",
        "",
        "  [3] 🛡️  SAFE MODE (8-15 seconds)",
        "      → Slow and steady approach",
        "      → Lowest detection risk"
    ])
    
    timing_profiles = {
        '1': {'name': 'FAST', 'range': (2, 4), 'emoji': '⚡'},
        '2': {'name': 'NORMAL', 'range': (4, 8), 'emoji': '🚶'},
        '3': {'name': 'SAFE', 'range': (8, 15), 'emoji': '🛡️'}
    }
    
    while True:
        timing = input(f"\n{Colors.YELLOW}➤ Select timing (1/2/3): {Colors.END}").strip()
        
        if timing in timing_profiles:
            profile = timing_profiles[timing]
            print_colored(f"\n   ✓ {profile['emoji']} {profile['name']} MODE selected", Colors.GREEN)
            print_colored(f"   ⏱️  Delay: {profile['range'][0]}-{profile['range'][1]} seconds", Colors.CYAN)
            return profile['range']
        else:
            print_colored("   ✗ Invalid choice! Please enter 1, 2, or 3", Colors.RED)

def show_mission_summary(target, message_config, quantity, timing):
    """Display mission summary before execution"""
    print_section_header("MISSION BRIEFING")
    
    mode_text = "RANDOM 🎲" if message_config['mode'] == 'random' else "CUSTOM ✏️"
    qty_text = "UNLIMITED ♾️" if quantity == 0 else f"{quantity} MESSAGES"
    
    summary_lines = [
        "📋 OPERATION OVERVIEW",
        "",
        f"🎯 TARGET         : {target}",
        f"📝 MESSAGE MODE   : {mode_text}",
    ]
    
    if message_config['mode'] == 'custom':
        summary_lines.append(f"💌 MESSAGE        : {message_config['message'][:50]}...")
    else:
        summary_lines.append(f"📊 DATABASE       : {len(message_config['questions'])} messages")
    
    summary_lines.extend([
        f"📦 QUANTITY       : {qty_text}",
        f"⏱️  TIMING         : {timing[0]}-{timing[1]} seconds",
        "",
        "⚠️  Ready to initiate operation"
    ])
    
    print_box(summary_lines)
    
    confirm = input(f"\n{Colors.YELLOW}{Colors.BOLD}➤ Launch operation? (y/n): {Colors.END}").lower().strip()
    return confirm == 'y'

def execute_mission(target, message_config, quantity, timing):
    """Execute the message delivery mission"""
    print_section_header("OPERATION IN PROGRESS")
    
    print_colored("🚀 Initiating message delivery system...", Colors.CYAN, bold=True)
    print_colored("⚠️  Press CTRL+C to abort operation\n", Colors.YELLOW)
    print_divider()
    
    sent = 0
    failed = 0
    consecutive_failures = 0
    
    try:
        while quantity == 0 or sent < quantity:
            # Select message
            if message_config['mode'] == 'custom':
                message = message_config['message']
            else:
                message = random_choice(message_config['questions'])
            
            # Progress indicator
            if quantity > 0:
                progress = (sent / quantity) * 100
                print(f"\n{Colors.CYAN}[{progress:5.1f}%]{Colors.END} Sending message #{sent + 1}/{quantity}...")
            else:
                print(f"\n{Colors.CYAN}[∞]{Colors.END} Sending message #{sent + 1}...")
            
            # Send message
            result = send_ngl_message(target, message)
            
            if result['success']:
                sent += 1
                consecutive_failures = 0
                timestamp = datetime.now().strftime("%H:%M:%S")
                print_colored(f"✓ [{timestamp}] SUCCESS #{sent:03d}", Colors.GREEN)
                print_colored(f"  └─ Message: {message[:60]}...", Colors.CYAN)
                
            else:
                failed += 1
                consecutive_failures += 1
                print_colored(f"✗ FAILED (Status: {result.get('status_code', 'N/A')})", Colors.RED)
                print_colored(f"  └─ Total failures: {failed}", Colors.YELLOW)
                
                # Check for critical failure threshold
                if consecutive_failures >= 3:
                    print_colored("\n🚨 CRITICAL: Multiple consecutive failures!", Colors.RED, bold=True)
                    print_colored("🛑 Emergency abort initiated!", Colors.RED)
                    break
                
                print_colored("⏳ Retrying in 10 seconds...", Colors.YELLOW)
                time.sleep(10)
                continue
            
            # Delay between messages
            if quantity == 0 or sent < quantity:
                delay = randint(timing[0], timing[1])
                print_colored(f"⏱️  Next delivery in {delay} seconds...", Colors.BLUE)
                time.sleep(delay)
                
    except KeyboardInterrupt:
        print_colored("\n\n🛑 Operation manually terminated by user!", Colors.YELLOW, bold=True)
    
    return sent, failed

def show_mission_report(target, sent, failed):
    """Display final mission report"""
    print_section_header("MISSION COMPLETE")
    
    total = sent + failed
    success_rate = (sent / total * 100) if total > 0 else 0
    
    # Determine mission status
    if sent == 0:
        status = "❌ FAILED"
        status_color = Colors.RED
    elif success_rate >= 90:
        status = "✓ EXCELLENT"
        status_color = Colors.GREEN
    elif success_rate >= 70:
        status = "✓ SUCCESS"
        status_color = Colors.GREEN
    elif success_rate >= 50:
        status = "⚠ PARTIAL"
        status_color = Colors.YELLOW
    else:
        status = "✗ POOR"
        status_color = Colors.RED
    
    report_lines = [
        "📊 PERFORMANCE METRICS",
        "",
        f"✓ Successful Deliveries : {sent}",
        f"✗ Failed Attempts       : {failed}",
        f"📈 Success Rate         : {success_rate:.1f}%",
        f"🎯 Mission Status       : {status}",
        "",
        f"Target: {target}",
        f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ]
    
    print_box(report_lines)
    
    # Print status with color
    print(f"\n{status_color}{Colors.BOLD}MISSION STATUS: {status}{Colors.END}\n")

def show_credits():
    """Display credits and footer"""
    print_divider('═')
    print_colored("🏆 PROFESSIONAL AUTOMATION SERVICES", Colors.CYAN, bold=True)
    print_colored(f"   Version {VERSION} - Premium Edition", Colors.BLUE)
    print_colored(f"   Developed by {AUTHOR}", Colors.BLUE)
    print_divider('═')
    print()

# ============================================
# MAIN PROGRAM
# ============================================
def main():
    """Main program entry point"""
    clear_screen()
    print_banner()
    
    # Warning notice
    print_box([
        "⚠️  IMPORTANT DISCLAIMER",
        "",
        "This tool is for EDUCATIONAL PURPOSES ONLY",
        "Using this tool violates NGL's Terms of Service",
        "The developer is NOT responsible for any misuse",
        "Use at your own risk and responsibility"
    ])
    
    proceed = input(f"\n{Colors.YELLOW}➤ Do you understand and agree? (y/n): {Colors.END}").lower()
    if proceed != 'y':
        print_colored("\n✗ Operation cancelled by user", Colors.RED)
        return
    
    try:
        # Step 1: Get target
        target = get_target_username()
        
        # Step 2: Get message configuration
        message_config = get_message_mode()
        
        # Step 3: Get quantity
        quantity = get_quantity()
        
        # Step 4: Get timing strategy
        timing = get_timing_strategy()
        
        # Step 5: Confirm operation
        if not show_mission_summary(target, message_config, quantity, timing):
            print_colored("\n✗ Operation cancelled by user", Colors.RED)
            return
        
        # Step 6: Execute mission
        sent, failed = execute_mission(target, message_config, quantity, timing)
        
        # Step 7: Show results
        show_mission_report(target, sent, failed)
        
    except KeyboardInterrupt:
        print_colored("\n\n✗ Program interrupted by user", Colors.YELLOW)
    except Exception as e:
        print_colored(f"\n✗ Unexpected error: {str(e)}", Colors.RED)
    finally:
        show_credits()

if __name__ == "__main__":
    main()