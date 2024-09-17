from core import HackingToolsCollection
from tools import AnonSurfTools
from tools import DDOSTools
from tools import ExploitFrameworkTools
from tools import ForensicTools
from tools import InformationGatheringTools
from tools import OtherTools
from tools import PayloadCreatorTools
from tools import PhishingAttackTools
from tools import PostExploitationTools
from tools import RemoteAdministrationTools
from tools import ReverseEngineeringTools
from tools import SqlInjectionTools
from tools import SteganographyTools
from tools import ToolManager
from tools import WebAttackTools
from tools import WirelessAttackTools
from tools import WordlistGeneratorTools
from tools import XSSAttackTools
import time
import os
from platform import system
from cybersec import Main

all_tools = [
    AnonSurfTools(),        
    InformationGatheringTools(),
    WordlistGeneratorTools(), 
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]

class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = "/home/cybersec.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                Main()
    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        time.sleep(2)