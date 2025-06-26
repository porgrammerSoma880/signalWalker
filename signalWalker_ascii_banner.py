


"""
SignalWalker ASCII Banner Generator
Inspired by Alan Walker's electronic vibes
"""           






def print_banner():
    """function to print the SignalWalker ASCII banner with styling"""
    
    # Color codes for terminal
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    banner = f"""
{CYAN}{BOLD}
███████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██╗     ██╗    ██╗ █████╗ ██╗     ██╗  ██╗███████╗██████╗ 
██╔════╝██║██╔════╝ ████╗  ██║██╔══██╗██║     ██║    ██║██╔══██╗██║     ██║ ██╔╝██╔════╝██╔══██╗
███████╗██║██║  ███╗██╔██╗ ██║███████║██║     ██║ █╗ ██║███████║██║     █████╔╝ █████╗  ██████╔╝
╚════██║██║██║   ██║██║╚██╗██║██╔══██║██║     ██║███╗██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║██║╚██████╔╝██║ ╚████║██║  ██║███████╗╚███╔███╔╝██║  ██║███████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{RESET}

{YELLOW}                           ⚡ Walking Through Digital Signals ⚡{RESET}
{MAGENTA}                           🎧 Where Music Meets Technology 🎧{RESET}
{GREEN}                               ~ Track • Trace • Discover ~{RESET}

{BLUE}═══════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
{CYAN}                             🔍 Phone Number Location Tracker 🔍{RESET}
{BLUE}═══════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
"""
    
    #finally, print the banner on the terminal
    print(banner)






#starting the program by running the main test
if __name__=="__main__":
    print_banner()



    