# software installation

## WM8960 Audio HAT
First, enable I2C:
* `sudo raspi-config`
* Interface Options
* I2C
* Yes

To install the audio driver, run:
```sh
sudo apt update && sudo apt install -y git
git clone https://github.com/waveshare/WM8960-Audio-HAT
cd WM-8960-Audio-HAT
sudo ./install.sh
sudo reboot
```

You can check that your device is working properly with `aplay -l`:
```sh
pi@pialarm:~ $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: vc4hdmi [vc4-hdmi], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: wm8960soundcard [wm8960-soundcard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

You should find the `wm8960soundcard` device listed here.

If it is not present, there is an issue with the waveshare driver on newer kernel modules. Try this:
```sh
# cd WM-8960-Audio-HAT
sudo ./uninstall.sh
sudo reboot
# ---
cd WM-8960-Audio-HAT
nano wn8960-soundcard.dts
```
Then, find this section, and replace `i2c1` with `i2c0`:
```
    fragment@2 {
                target = <&i2c0>;   # <--- HERE! Yours will be i2c1 by default.
                __overlay__ {
                        #address-cells = <1>;
                        #size-cells = <0>;
                        status = "okay";

                        wm8960: wm8960{
                                compatible = "wlf,wm8960";
                                reg = <0x1a>;
                                #sound-dai-cells = <0>;
                                AVDD-supply = <&vdd_5v0_reg>;
                                DVDD-supply = <&vdd_3v3_reg>;
                        };
                };
    };
```
And reboot, then retry.

## SPI Display

### Wiring

| TFT   | Board     | GPIO   | Pin # | Notes            |
| ----- | --------- | ------ | ----- | ---------------- |
| VCC   | 3v3       |        | 17    |                  |
| GND   | GND       |        | 20    |                  |
| CS    | SPIO CE0  | GPIO5  | 29    |                  |
| RESET |           | GPIO24 | 18    |                  |
| DC    |           | GPIO25 | 22    |                  |
| SDI   | SPI0 MOSI | GPIO10 | 19    | Tied to T_DIN    |
| SCK   | SPI0 SCLK | GPIO11 | 23    | Tied to T_CLK    |
| LED   |           | GPIO23 | 16    | 100 ohm resistor |
| SDO   | SPI0 MISO | GPIO9  | 21    | Tied to T_DO     |
| T_CLK | SPI0 SCLK | GPIO11 | 23    | Tied to SCK      |
| T_CS  | SPI0 CE1  | GPIO6  | 31    |                  |
| T_DIN | SPI0 MOSI | GPIO10 | 19    | Tied to SDI      |
| T_DO  | SPI0 MISO | GPIO9  | 21    | Tied to SDO      |
| T_IRQ |           | GPIO22 | 15    |                  |

### Software
First, enable SPI:
* `sudo raspi-config`
* Interface Options
* SPI
* Yes

Then [install the Adafruit CircuitPython Blinka library](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi):
```sh
sudo apt update && sudo apt install -y python3-pip
sudo apt install --upgrade -y python3-setuptools
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
```

Then install the TFT and XPT libraries:
```sh
pip3 install adafruit-circuitpython-rgb-display
pip3 install xpt2046-circuitpython
```
