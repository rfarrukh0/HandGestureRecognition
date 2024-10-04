from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# initialize audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def adjust_volume(direction):
    # adjust volume based on direction (up or down)
    current_volume = volume.GetMasterVolumeLevelScalar()
    if direction == "up":
        volume.SetMasterVolumeLevelScalar(min(current_volume + 0.1, 1.0), None)
    elif direction == "down":
        volume.SetMasterVolumeLevelScalar(max(current_volume - 0.1, 0.0), None)
