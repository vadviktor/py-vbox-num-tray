import os
from time import sleep

from infi.systray import SysTrayIcon
from virtualbox import VirtualBox
from virtualbox.library import MachineState

run = True


def on_quit_callback(systray):
    global run
    run = False


def running_vagrant_boxes():
    vbox = VirtualBox()
    return [vm.name for vm in vbox.machines if vm.state == MachineState(5)]


if __name__ == "__main__":
    scriptDirectory = os.path.dirname(os.path.realpath(__file__))

    with SysTrayIcon(
            icon=os.path.join(scriptDirectory, "0.ico"),
            hover_text="No box running.",
            on_quit=on_quit_callback
    ) as systray:
        while run:
            vms = running_vagrant_boxes()
            systray.update(
                icon=os.path.join(scriptDirectory, f"{len(vms)}.ico"),
                hover_text="\n".join(vms),
            )
            sleep(5)
